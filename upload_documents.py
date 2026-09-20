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


documents = [
    {
        "id": "1",
        "title": "Azure Blob Storage",
        "content": (
            "Azure Blob Storage is Microsoft's object storage service "
            "for storing large amounts of unstructured data such as "
            "documents, images, videos and backups."
        )
    },
    {
        "id": "2",
        "title": "Azure Machine Learning",
        "content": (
            "Azure Machine Learning is a cloud service used to train, "
            "deploy and manage machine learning models."
        )
    },
    {
        "id": "3",
        "title": "Azure AI Search",
        "content": (
            "Azure AI Search is a cloud search service that can provide "
            "keyword, semantic and vector search capabilities for "
            "enterprise applications and RAG solutions."
        )
    }
]


result = search_client.upload_documents(documents)

print("Documents uploaded successfully.")

for item in result:
    print(item.key, item.succeeded)