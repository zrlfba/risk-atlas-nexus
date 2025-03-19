import json
import re
from risk_atlas_nexus.toolkit.logging import configure_logger
from typing import Any, List, Union
from risk_atlas_nexus.blocks.inference.params import TextGenerationInferenceOutput

logger = configure_logger(__name__)

POSTPROCESSORS_REGISTRY = {}

JSON_STRIP_CHARS = " \n\r\t`"


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
        inference_response: Union[
            TextGenerationInferenceOutput, List[TextGenerationInferenceOutput]
        ] = func(*args, **kwargs)
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


@register("list_of_str")
class ListOfStr:

    def apply(self, text: str) -> List[str]:

        # Strip whitespace,newlines,backtick from the start and end
        text = str(text.strip(JSON_STRIP_CHARS).replace("'", '"'))

        # Remove newlines characters inside the returned value
        text = text.replace("\n", "")

        if isinstance(text, str):
            try:
                list_of_text = json.loads(text)
                if not isinstance(list_of_text, List):
                    raise ()
            except:
                list_of_text = re.findall(r'"(.*?)"', text)

        if isinstance(list_of_text, List):
            list_of_text = [text.strip() for text in list_of_text]

        return list_of_text


@register("clean_output")
class CleanOutput:

    def apply(self, text: Any) -> Any:
        return " ".join(str(text).strip(JSON_STRIP_CHARS).split())
