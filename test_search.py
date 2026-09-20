from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

from config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    AZURE_SEARCH_INDEX
)


search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)


results = search_client.search(
    search_text="Azure Blob Storage",
    top=3
)


for result in results:
    print("TITLE:", result.get("title"))
    print("CONTENT:", result.get("content"))
    print("-" * 60)