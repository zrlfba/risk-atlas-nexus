import os
from typing import Any, Dict, List, Union

from dotenv import load_dotenv

from risk_atlas_nexus.blocks.inference.base import InferenceEngine
from risk_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    RITSInferenceEngineParams,
    TextGenerationInferenceOutput,
)
from risk_atlas_nexus.blocks.inference.postprocessing import postprocess
from risk_atlas_nexus.metadata_base import InferenceEngineType
from risk_atlas_nexus.toolkit.job_utils import run_parallel


# load .env file to environment
load_dotenv()


class RITSInferenceEngine(InferenceEngine):

    _inference_engine_type = InferenceEngineType.RITS
    _inference_engine_parameter_class = RITSInferenceEngineParams

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        api_key = credentials.get(
            "api_key", os.environ.get(f"{self._inference_engine_type}_API_KEY", None)
        )
        assert api_key, (
            f"Error while trying to run {self._inference_engine_type}. "
            f"Please set the env variable: '{self._inference_engine_type}_API_KEY' or pass api_key to credentials."
        )

        api_url = credentials.get(
            "api_url", os.environ.get(f"{self._inference_engine_type}_API_URL", None)
        )
        assert api_url, (
            f"Error while trying to run {self._inference_engine_type}. "
            f"Please set the env variable: '{self._inference_engine_type}_API_URL' or pass api_url to credentials."
        )

        return InferenceEngineCredentials(api_key=api_key, api_url=api_url)

    def create_client(self, credentials):
        from openai import OpenAI

        return OpenAI(
            api_key=credentials["api_key"],
            base_url=f"{credentials['api_url']}/{self.model_name_or_path.split('/')[1]}/v1",
            default_headers={"RITS_API_KEY": credentials["api_key"]},
        )

    @postprocess
    def generate(self, prompts: List[str]) -> List[TextGenerationInferenceOutput]:
        response = self.client.completions.create(
            model=self.model_name_or_path,
            prompt=prompts,
            **self.parameters,
        )
        return [self._prepare_generate_output(choice) for choice in response.choices]

    def _prepare_generate_output(self, response):
        return TextGenerationInferenceOutput(
            prediction=response.text,
            model_name_or_path=self.model_name_or_path,
            inference_engine=str(self._inference_engine_type),
        )

    @postprocess
    def chat(self, messages: List[Dict]) -> TextGenerationInferenceOutput:
        response = self.client.chat.completions.create(
            messages=messages,
            model=self.model_name_or_path,
            **self.parameters,
        )
        return self._prepare_chat_output(response)

    def _prepare_chat_output(self, response):
        return TextGenerationInferenceOutput(
            prediction=response.choices[0].message.content,
            model_name_or_path=self.model_name_or_path,
            inference_engine=str(self._inference_engine_type),
        )
