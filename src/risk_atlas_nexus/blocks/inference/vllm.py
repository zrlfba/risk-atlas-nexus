import os
from typing import Any, Dict, List, Union

from dotenv import load_dotenv

from risk_atlas_nexus.blocks.inference.base import InferenceEngine
from risk_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    TextGenerationInferenceOutput,
    VLLMInferenceEngineParams,
)
from risk_atlas_nexus.blocks.inference.postprocessing import postprocess
from risk_atlas_nexus.metadata_base import InferenceEngineType
from risk_atlas_nexus.toolkit.job_utils import run_parallel
from risk_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)

# load .env file to environment
load_dotenv()


class VLLMInferenceEngine(InferenceEngine):

    _inference_engine_type = InferenceEngineType.VLLM
    _inference_engine_parameter_class = VLLMInferenceEngineParams

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        api_url = None
        if credentials:
            api_url = credentials.get(
                "api_url",
                os.environ.get(f"{self._inference_engine_type}_API_URL", None),
            )
            assert api_url, (
                f"To run {self._inference_engine_type} in offline mode, passed `credentials` must be None. To run in server mode, "
                f"pass only the `api_url` to credentials or set the env variable: '{self._inference_engine_type}_API_URL'"
            )

            logger.info(
                f"Detected {self._inference_engine_type} api url. {self._inference_engine_type} engine will execute requests on the server at {api_url}."
            )

            api_key = credentials.get(
                "api_key",
                os.environ.get(f"{self._inference_engine_type}_API_KEY", None),
            )

            return InferenceEngineCredentials(api_url=api_url, api_key=api_key)
        else:
            logger.info(
                f"Running {self._inference_engine_type} in offline mode. The model `{self.model_name_or_path}` will be downloaded if not available offline."
            )
            return None

    def create_client(self, credentials):
        if credentials:
            from openai import OpenAI

            return OpenAI(
                api_key=credentials["api_key"] if credentials["api_key"] else "-",
                base_url=f"{credentials['api_url']}/v1",
            )
        else:
            from vllm import LLM

            return LLM(
                model=self.model_name_or_path,
                trust_remote_code=True,
                max_model_len=4098,
            )

    @postprocess
    def generate(self, prompts: List[str]):
        from vllm import LLM, SamplingParams

        if isinstance(self.client, LLM):
            responses = []
            for response in self.client.generate(
                prompts=prompts,
                sampling_params=SamplingParams(**self.parameters),
                use_tqdm=True,
            ):
                responses.append(self._prepare_generate_output(response, offline=True))
            return responses
        else:
            response = self.client.completions.create(
                model=self.model_name_or_path,
                prompt=prompts,
                **self.parameters,
            )
            return [
                self._prepare_generate_output(choice, offline=False)
                for choice in response.choices
            ]

    def _prepare_generate_output(self, response, offline=True):
        return TextGenerationInferenceOutput(
            prediction=(response.outputs[0].text if offline else response.text),
            model_name_or_path=self.model_name_or_path,
            inference_engine=str(self._inference_engine_type),
        )

    @postprocess
    def chat(self, messages: List[Dict]):
        from vllm import LLM, SamplingParams

        if isinstance(self.client, LLM):
            responses = []
            for response in self.client.chat(
                messages=messages,
                sampling_params=SamplingParams(**self.parameters),
                use_tqdm=True,
            ):
                responses.append(self._prepare_chat_output(response, offline=True))
            return responses
        else:

            response = self.client.chat.completions.create(
                model=self.model_name_or_path,
                messages=messages,
                **self.parameters,
            )
            return self._prepare_chat_output(response, offline=False)

    def _prepare_chat_output(self, response, offline=True):
        return TextGenerationInferenceOutput(
            prediction=(
                response.outputs[0].text
                if offline
                else response.choices[0].message.content
            ),
            model_name_or_path=self.model_name_or_path,
            inference_engine=str(self._inference_engine_type),
        )
