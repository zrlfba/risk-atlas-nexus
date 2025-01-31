from abc import ABC, abstractmethod
from typing import Optional

from risk_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    Container,
    RiskTaxonomy,
)
from risk_atlas_nexus.blocks.inference.base import InferenceEngine
from risk_atlas_nexus.blocks.inference.params import TextGenerationInferenceOutput
from risk_atlas_nexus.blocks.risk_detector.templates import (
    GG_PROMPT_TEMPLATE,
    IBM_PROMPT_TEMPLATE,
    MIT_PROMPT_TEMPLATE,
    NIST_PROMPT_TEMPLATE,
    PROMPT_TEMPLATE,
)
from risk_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


class RiskDetector(ABC):

    def __init__(
        self,
        ontology: Container,
        inference_engine: InferenceEngine,
        taxonomy: Optional[str] = None,
    ):
        self.inference_engine = inference_engine
        self._ontology = ontology
        self._risks = self.get_risks_by_taxonomy_id(ontology, taxonomy)
        self._prompt_template = self.get_prompt_template_by_taxonomy_id(taxonomy)

    def get_risks_by_taxonomy_id(
        self, ontology: Container, taxonomy_id: Optional[str] = None
    ):
        taxonomy_id = taxonomy_id if taxonomy_id else "ibm-risk-atlas"
        taxonomies = list(
            filter(
                lambda taxonomy: taxonomy.id == taxonomy_id,
                ontology.taxonomies,
            )
        )

        if len(taxonomies) > 0:
            taxonomy: RiskTaxonomy = taxonomies[0]
            logger.info(
                f"Selected taxonomy is {str(taxonomy.name)}. For more info: {taxonomy.url}"
            )

            return list(
                filter(
                    lambda risk: risk.isDefinedByTaxonomy == taxonomy.id,
                    ontology.risks,
                )
            )
        else:
            raise Exception(
                f"Risk Taxonomy: {taxonomy_id} not found. Available taxonomies: {[taxonomy.id for taxonomy in ontology.taxonomies]}"
            )

    def get_prompt_template_by_taxonomy_id(self, taxonomy_id: Optional[str] = None):
        if taxonomy_id == "ibm-risk-atlas":
            return IBM_PROMPT_TEMPLATE
        elif taxonomy_id == "mit-ai-risk-repository":
            return MIT_PROMPT_TEMPLATE
        elif taxonomy_id == "nist-ai-rmf":
            return NIST_PROMPT_TEMPLATE
        elif taxonomy_id == "ibm-granite-guardian":
            return GG_PROMPT_TEMPLATE
        else:
            return PROMPT_TEMPLATE

    @abstractmethod
    def detect(self, usecase: str) -> TextGenerationInferenceOutput:
        raise NotImplementedError
