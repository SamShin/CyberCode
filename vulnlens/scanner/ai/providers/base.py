"""
Base AI provider.
"""
# Imports

class BaseAIProvider:
    def __init__(self, api_key: str, model_name: str):
        pass
    def complete(self, prompt: str) -> str:
        '''Abstract method to complete a prompt.'''
        pass
