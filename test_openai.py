from openai import AzureOpenAI

from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION
)


print("Endpoint:", AZURE_OPENAI_ENDPOINT)
print("Deployment:", AZURE_OPENAI_DEPLOYMENT)
print("API Version:", AZURE_OPENAI_API_VERSION)
print("API Key Loaded:", bool(AZURE_OPENAI_API_KEY))


client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION
)


response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)


print("\nAzure OpenAI Response:")
print(response.choices[0].message.content)