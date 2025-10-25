"""
Helper module to create Azure OpenAI client with Entra ID authentication
This replaces the direct API key usage with Azure AD token authentication
"""
import os
from langchain_openai import AzureChatOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


def get_azure_llm(temperature=0, model_name="gpt-35-turbo", **kwargs):
    """
    Create an Azure OpenAI LLM instance with Entra ID authentication
    
    Args:
        temperature: Temperature for the model
        model_name: Deployment name in Azure OpenAI
        **kwargs: Additional arguments to pass to AzureChatOpenAI
    
    Returns:
        AzureChatOpenAI instance configured with Entra ID authentication
    """
    # Get Azure OpenAI endpoint from environment
    endpoint = os.getenv("ENDPOINT_URL", "https://ttt-openai-01.openai.azure.com/")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")
    
    # Initialize Azure token provider with Entra ID
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default"
    )
    
    # Create and return the Azure OpenAI client
    llm = AzureChatOpenAI(
        azure_endpoint=endpoint,
        azure_ad_token_provider=token_provider,
        api_version=api_version,
        azure_deployment=model_name,
        temperature=temperature,
        **kwargs
    )
    
    return llm