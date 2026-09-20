from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential

from config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY
)

client = SearchIndexClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)

print("\nAvailable Azure AI Search indexes:\n")

for index in client.list_indexes():
    print(index.name)