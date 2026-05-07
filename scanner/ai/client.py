"""AI client for making LLM API calls (Anthropic, OpenAI, etc.)."""

# from typing import Optional
# import os


class AIClient:
    """Client for making API calls to LLM providers."""

    def __init__(self, api_key: str, model_name: str, endpoint: str = None):
        """
        Initialize AI client with API credentials.

        Args:
            api_key: API key for LLM provider
            model_name: Model name/identifier
            endpoint: Optional custom endpoint URL
        """
        pass

    def call_model(self, prompt: str, max_tokens: int = 1024) -> str:
        """
        Make a call to the LLM with the given prompt.

        Args:
            prompt: Prompt text to send to model
            max_tokens: Maximum tokens in response

        Returns:
            Model response text
        """
        pass

    def call_model_structured(self, prompt: str, json_schema: dict = None) -> dict:
        """
        Make a structured call to the LLM expecting JSON response.

        Args:
            prompt: Prompt text to send to model
            json_schema: Optional JSON schema for response validation

        Returns:
            Parsed JSON response as dictionary
        """
        pass
