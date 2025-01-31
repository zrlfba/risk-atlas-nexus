import os
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import YAMLDumper
from typing import Optional

from importlib.metadata import version
from risk_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    Action,
    RiskTaxonomy,
)

from risk_atlas_nexus.blocks.risk_detector import AutoRiskDetector
from risk_atlas_nexus.blocks.risk_explorer import RiskExplorer
from risk_atlas_nexus.blocks.inference import InferenceEngine
from risk_atlas_nexus.ai_risk_ontology.schema import *
from risk_atlas_nexus.toolkit.data_utils import load_yamls_to_container
from risk_atlas_nexus.toolkit.logging import configure_logger

logger = configure_logger(__name__)


class RiskAtlasNexus:
    """A RiskAtlasNexus"""

    # Load the schema
    directory = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(directory, "ai_risk_ontology/schema/ai-risk-ontology.yaml")
    schema_view = SchemaView(yaml.safe_load(fn))

    def __init__(self, base_dir: str = None):
        """Create a new RiskAtlasNexus object

        Args:
            base_dir: str
                (Optional) add an alternative source of date
        """
        if base_dir is not None:
            if type(base_dir) != str:
                raise ValueError("Base directory must be a string", base_dir)
            if os.path.isdir(base_dir) == False:
                logger.error(f"Directory %s does not exist.", base_dir)
                raise FileNotFoundError("Base directory is not found", base_dir)

        ontology = load_yamls_to_container(base_dir)
        self._ontology = ontology
        self._risk_explorer = RiskExplorer(ontology)
        logger.info(f"Created RiskAtlasNexus instance. Base_dir: %s", base_dir)

    def export(cls, export_path):
        """Export RiskAtlasNexus configuration to file.

        Args:
            export_path: str
                The path to the directory where the artifact will be exported to.

        """
        if os.path.isdir(export_path) == False:
            logger.error(f"Directory %s does not exist.", export_path)
            raise FileNotFoundError("Export directory is not found", export_path)

        export_file_path = os.path.join(export_path, "ai-risk-ontology.yaml")

        with open(export_file_path, "+tw", encoding="utf-8") as output_file:
            print(YAMLDumper().dumps(cls._ontology), file=output_file)
            output_file.close()

    @classmethod
    def get_schema(cls):
        """Get schema

        Returns:
            schema
        """
        return cls.schema_view

    @classmethod
    def get_version(cls):
        """Get library version

        Returns:
            dict: Version number
        """
        response = {"version": version("risk_atlas_nexus")}
        return response

    def get_all_risks(cls, taxonomy=None):
        """Get all risk definitions from the LinkML

        Args:
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[Risk]
                Result containing a list of AI risks
        """
        if taxonomy is not None and type(taxonomy) != str:
            raise ValueError("Taxonomy must be a string", taxonomy)

        risk_instances = cls._risk_explorer.get_all_risks(taxonomy)
        return risk_instances

    def get_risk_by_tag(cls, tag):
        """Get risk definition from the LinkML, filtered by risk atlas tag

        Args:
            tag: str
                The string label identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Risk
                Result containing a list of AI risks
        """
        risk = cls._risk_explorer.get_risk_by_tag(tag=tag)
        return risk

    def get_risk_by_id(cls, id):
        """Get a risk definition from the LinkML, filtered by risk id

        Args:
            id: str
                The string label identifying the risk

        Returns:
            Risk
                Result containing a list of AI risks
        """
        risk = cls._risk_explorer.get_risk_by_id(id=id)
        return risk

    def get_related_risk_ids_by_atlas_tag(cls, tag, taxonomy=None):
        """Get related risk IDs from the LinkML, that are attached to a risk with risk atlas tag

        Args:
            tag: str
                The string label identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            List[str]
                Result containing a list of AI risk IDs
        """
        if taxonomy is not None and type(taxonomy) != str:
            raise ValueError("Taxonomy must be a string", taxonomy)

        related_risk_instances = cls._risk_explorer.get_related_risk_ids_by_atlas_tag(
            tag, taxonomy
        )
        return related_risk_instances

    def get_related_risks_by_atlas_tag(cls, tag, taxonomy=None):
        """Get related risk definitions from the LinkML, by risk atlas tag

        Args:
            tag: str
                The string label identifying the risk
            taxonomy: str
                The string label for a taxonomy

        Returns:
            List[Risk]
                Result containing a list of AI risks
        """
        if taxonomy is not None and type(taxonomy) != str:
            raise ValueError("Taxonomy must be a string", taxonomy)

        related_risk_instances = cls._risk_explorer.get_related_risks_by_atlas_tag(
            tag, taxonomy
        )
        return related_risk_instances

    def get_related_risk_ids_by_risk_id(cls, id, taxonomy=None):
        """Get related risk definitions from the LinkML, by risk atlas tag

        Args:
            id: str
                The string label identifying the risk
            taxonomy: str
                The string label for a taxonomy

        Returns:
            List[str]
                Result containing a list of AI risks IDs
        """
        if taxonomy is not None and type(taxonomy) != str:
            raise ValueError("Taxonomy must be a string", taxonomy)

        related_risk_instances = cls._risk_explorer.get_related_risk_ids_by_risk_id(
            id=id, taxonomy=taxonomy
        )
        return related_risk_instances

    def get_related_risks_by_risk_id(cls, id, taxonomy=None):
        """Get related risk definitions from the LinkML, by risk atlas tag

        Args:
            id: str
                The string label identifying the risk
            taxonomy: str
                The string label for a taxonomy

        Returns:
            List[Risk]
                Result containing a list of AI risks
        """
        if taxonomy is not None and type(taxonomy) != str:
            raise ValueError("Taxonomy must be a string", taxonomy)

        related_risk_instances = cls._risk_explorer.get_related_risks_by_risk_id(
            id=id, taxonomy=taxonomy
        )
        return related_risk_instances

    def get_risk_actions_by_risk_id(cls, id, taxonomy=None):
        """Get actions for a risk definition from the LinkML, filtered by risk id

        Args:
            id: str
                The string label identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Risk
                Result containing a list of AI risks
        """
        if taxonomy is not None and type(taxonomy) != str:
            raise ValueError("Taxonomy must be a string", taxonomy)

        actions = cls._risk_explorer.get_risk_actions_by_risk_id(
            id=id, taxonomy=taxonomy
        )
        return actions

    def get_all_actions(cls, taxonomy=None):
        """Get all risk definitions from the LinkML

        Args:
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[Action]
                Result containing a list of AI risks
        """
        if taxonomy is not None and type(taxonomy) != str:
            raise ValueError("Taxonomy must be a string", taxonomy)

        action_instances: list[Action] = cls._risk_explorer.get_all_actions(taxonomy)
        return action_instances

    def get_action_by_id(cls, id, taxonomy=None):
        """Get an action definition from the LinkML, filtered by action id

        Args:
            id: str
                The string id identifying the action
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Risk
                Result containing a list of AI risks
        """
        if taxonomy is not None and type(taxonomy) != str:
            raise ValueError("Taxonomy must be a string", taxonomy)

        action: Action | None = cls._risk_explorer.get_action_by_id(id=id)
        return action

    def identify_risks_from_usecase(
        cls,
        usecase,
        inference_engine: InferenceEngine,
        taxonomy: Optional[str] = None,
    ):
        """Identify potential risks from a usecase description

        Args:
            usecase: str
                A string describing an AI usecase
            inference_engine: InferenceEngine
                An LLM inference engine to infer risks from the usecase.
            taxonomy: str
                The string label for a taxonomy

        Returns:
            List[Risk]
                Result containing a list of AI risks
        """
        if taxonomy is not None and (type(taxonomy) != str):
            raise ValueError("Taxonomy must be a string", taxonomy)

        risk_detector = AutoRiskDetector.create(
            cls._ontology, inference_engine=inference_engine, taxonomy=taxonomy
        )

        return risk_detector.detect(usecase).prediction

    def get_all_taxonomies(cls):
        """Get all taxonomy definitions from the LinkML, optionally filtered by taxonomy

        Returns:
            List[Risk]
                Result containing a list of AI risks
        """
        taxonomy_instances: list[RiskTaxonomy] = cls._risk_explorer.get_all_taxonomies()
        return taxonomy_instances

    def get_taxonomy_by_id(cls, id):
        """Get taxonomy definitions from the LinkML filtered by taxonomy id

        Args:
            id: str
                The string id for a taxonomy

        Returns:
            List[RiskTaxonomy]
                Result containing a list of AI risks
        """
        taxonomy: RiskTaxonomy | None = cls._risk_explorer.get_taxonomy_by_id(id)
        return taxonomy
