# Standard
from enum import auto, Enum, unique
from typing import Any


@unique
class InferenceEngineType(str, Enum):
    """Enum to contain possible values for inference engine types"""

    RITS = "RITS"
    WML = "WML"
    VLLM = "VLLM"
    OLLAMA = "OLLAMA"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))

    def __str__(self):
        return self.name

@unique
class MappingMethod(str, Enum):
    """Enum to contain possible values for risk mapping methods"""
    SEMANTIC = "SEMANTIC"
    RITS_INFERENCE = "RITS_INFERENCE"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))

    def __str__(self):
        return self.name