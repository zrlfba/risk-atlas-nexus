# Standard Library
from os import listdir
from os.path import isfile, join
from pathlib import Path

# Third Party
from linkml_runtime.dumpers import YAMLDumper
from linkml_runtime.loaders import YAMLLoader
from pydantic import BaseModel
from sssom.parsers import MetadataType, parse_sssom_table

# Local
from risk_atlas_nexus.ai_risk_ontology import Container, Risk

SCHEMA_DIR = "src/risk_atlas_nexus/ai_risk_ontology/schema/"
DATA_DIR = "src/risk_atlas_nexus/data/knowledge_graph/"
MAP_DIR = "src/risk_atlas_nexus/data/mappings/"
PREFIX_MAP = {"ibmairisk": "", "owaspai": "owasp-", "nistai": ""}
DATA_MAP = {
    "ibmairisk": "risk_atlas_data.yaml",
    "owaspai": "owasp_llm_2.0_data.yaml",
    "nistai": "nist_ai_rmf_data.yaml"
}


class RiskMap(BaseModel):
    src_risk_id: str
    target_risk_id: str
    relationship: str

    def __init__(self, src_risk_id: str, target_risk_id: str, relationship: str):
        src_index = src_risk_id.find(":")
        src_id = PREFIX_MAP[src_risk_id[:src_index]] + src_risk_id[src_index + 1:] if src_index > -1 else src_risk_id
        target_index = target_risk_id.find(":")
        target_id = PREFIX_MAP[
            target_risk_id[:target_index]] + target_risk_id[target_index + 1:] if target_index > -1 else target_risk_id
        super().__init__(src_risk_id=src_id, target_risk_id=target_id, relationship=relationship)


def import_mappings(file_name: str) -> tuple[MetadataType, dict[str, list[RiskMap]]]:
    mapping = parse_sssom_table(file_path=file_name)
    map_types = mapping.df["predicate_id"].unique().tolist()
    maps_by_type = {
        map_type:
        mapping.df.loc[mapping.df["predicate_id"] == map_type].apply(lambda item: RiskMap(
            **{
                "src_risk_id": item["subject_id"],
                "target_risk_id": item["object_id"],
                "relationship": item["predicate_id"]
            }),
                                                                     axis=1).to_list()
        for map_type in map_types
    }
    source_id = str(mapping.df["subject_id"].iloc[0])
    mapping.metadata["source"] = source_id[:source_id.find(":")]
    target_id = str(mapping.df["object_id"].iloc[0])
    mapping.metadata["target"] = target_id[:target_id.find(":")]
    return mapping.metadata, maps_by_type


def import_risks(provider_name: str) -> list[Risk]:
    file_name = DATA_DIR + DATA_MAP[provider_name]
    container = YAMLLoader().load(source=file_name, target_class=Container)
    return container.risks


if __name__ == "__main__":
    mapping_files = [file_name for file_name in listdir(MAP_DIR) if isfile(join(MAP_DIR, file_name))]
    for file_name in mapping_files:
        metadata, risk_maps = import_mappings(MAP_DIR + file_name)
        output_file = DATA_DIR + Path(file_name).stem + "_data.yaml"
        source_risks = import_risks(metadata.get("source"))
        target_risk_ids = [risk.id for risk in import_risks(metadata.get("target"))]
        output_risks = [Risk(id=risk.id) for risk in source_risks]
        for risk in output_risks:
            related_maps = {
                map_type: [
                    risk_map.target_risk_id for risk_map in risk_maps[map_type]
                    if risk_map.src_risk_id == risk.id and risk_map.target_risk_id in target_risk_ids
                ]
                for map_type in risk_maps.keys()
            }
            for map_type in related_maps.keys():
                if related_maps[map_type]:
                    slot_name = map_type.split(":")[-1]
                    risk.__setattr__(slot_name, related_maps[map_type])
        with open(output_file, "+tw", encoding="utf-8") as output_file:
            print(YAMLDumper().dumps(Container(risks=output_risks)), file=output_file)
            output_file.close()
