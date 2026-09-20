from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField
)
from azure.core.credentials import AzureKeyCredential

from config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    AZURE_SEARCH_INDEX
)


index_client = SearchIndexClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)


fields = [
    SimpleField(
        name="id",
        type="Edm.String",
        key=True
    ),

    SearchableField(
        name="title",
        type="Edm.String"
    ),

    SearchableField(
        name="content",
        type="Edm.String"
    )
]


index = SearchIndex(
    name=AZURE_SEARCH_INDEX,
    fields=fields
)


result = index_client.create_or_update_index(index)

print(f"Index created successfully: {result.name}")