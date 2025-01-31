import dataclasses
from typing import Any, Dict, List, Literal, Optional, TypedDict, Union


class InferenceEngineCredentials(TypedDict):
    api_key: str
    api_url: str
    space_id: Optional[str] = None  # only used for WML engine
    project_id: Optional[str] = None  # only used for WML engine


class RITSInferenceEngineParams(TypedDict):
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    max_tokens: Optional[int] = None
    seed: Optional[int] = None
    stop: Union[Optional[str], List[str]] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    top_logprobs: Optional[int] = 20
    logit_bias: Optional[Dict[str, int]] = None
    logprobs: Optional[bool] = True
    n: Optional[int] = None
    parallel_tool_calls: Optional[bool] = None
    service_tier: Optional[Literal["auto", "default"]] = None


class WMLInferenceEngineParams(TypedDict):
    decoding_method: Optional[Literal["greedy", "sample"]] = None
    length_penalty: Optional[Dict[str, Union[int, float]]] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    random_seed: Optional[int] = None
    repetition_penalty: Optional[float] = None
    min_new_tokens: Optional[int] = None
    max_new_tokens: Optional[int] = None
    stop_sequences: Optional[List[str]] = None
    time_limit: Optional[int] = None
    truncate_input_tokens: Optional[int] = None
    prompt_variables: Optional[Dict[str, Any]] = None
    return_options: Optional[Dict[str, bool]] = None


@dataclasses.dataclass(kw_only=True)
class InferencePromptParams:
    query: str
    instructions: Optional[str] = None
    examples: Optional[str] = None


@dataclasses.dataclass(frozen=True, kw_only=True)
class TextGenerationInferenceOutput:
    """Contains the prediction results and metadata for the inference.

    Args:
        prediction (Any): model ouput

        input_tokens (int) : number of input tokens to the model.

        output_tokens (int) : number of output tokens to the model.

        stop_reason (str): stop reason for text generation, for example "eos" (end of string).

        seed (int): seed used by the model during generation.

        input_text (str): input to the model.

        model_name (str): the model_name as kept in the InferenceEngine.

        inference_engine (str): The label stating the type of the InferenceEngine.
    """

    prediction: Union[str, List[Dict[str, Any]]]
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    stop_reason: Optional[str] = None
    seed: Optional[int] = None
    input_text: Optional[str] = None
    model_name_or_path: Optional[str] = None
    inference_engine: Optional[str] = None
