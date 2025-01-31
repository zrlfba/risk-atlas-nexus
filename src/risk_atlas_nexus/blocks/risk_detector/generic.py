import json

from risk_atlas_nexus.blocks.inference import (
    InferencePromptParams,
    TextGenerationInferenceOutput,
)
from risk_atlas_nexus.blocks.risk_detector import RiskDetector


class GenericRiskDetector(RiskDetector):

    def detect(self, usecase: str) -> TextGenerationInferenceOutput:
        return self.inference_engine.generate(
            [
                InferencePromptParams(
                    query=self._prompt_template.format(
                        risks=json.dumps(
                            [
                                {"category": risk.name, "description": risk.description}
                                for risk in self._risks
                            ],
                            indent=4,
                        ),
                        query=usecase,
                    ),
                )
            ]
        )[0]
