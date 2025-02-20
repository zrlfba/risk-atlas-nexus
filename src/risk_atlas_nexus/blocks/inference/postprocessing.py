import json
import re
from risk_atlas_nexus.toolkit.logging import configure_logger
from typing import Any, List
from risk_atlas_nexus.blocks.inference.params import TextGenerationInferenceOutput

logger = configure_logger(__name__)

POSTPROCESSORS_REGISTRY = {}


def register(name):
    def decorate(fn):
        assert (
            name not in POSTPROCESSORS_REGISTRY
        ), f"Processor '{name}' conflicts with existing registered!"

        POSTPROCESSORS_REGISTRY[name] = fn
        return fn

    return decorate


def postprocess(func):
    def wrapper(*args, **kwargs):
        inference_response: List[TextGenerationInferenceOutput] = func(*args, **kwargs)
        if args[0].postprocessors:
            for processor in args[0].postprocessors:
                try:
                    for inference in inference_response:
                        inference.prediction = POSTPROCESSORS_REGISTRY[
                            processor
                        ]().apply(inference.prediction)
                except:
                    logger.debug("[{processor}] - Error in post processing.")
        return inference_response

    return wrapper


@register("clean_output")
class CleanOutput:

    def apply(self, text: Any) -> Any:
        return " ".join(str(text).strip().split())


@register("take_first_not_null")
class TakeFirstNonEmptyLine:

    def apply(self, text: Any) -> Any:
        parts = str(text).strip().split("\n")
        if len(parts) == 0:
            return ""
        return parts[0].strip()


@register("return_as_object")
class ReturnAsObject:

    def apply(self, text: Any) -> Any:
        if isinstance(text, str):
            try:
                return json.loads(str(text.strip().replace("'", '"')))
            except:
                return str(text).strip()
        return text


@register("take_first_word")
class TakeFirstWord:

    def apply(self, text: Any) -> Any:
        match = re.search(r"([-]*[0-9]+(\.([0-9]+))*)|([\w]+)", text)
        if match:
            return text[match.start() : match.end()]
        return ""
