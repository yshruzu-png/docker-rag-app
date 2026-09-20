# Here is a simple Azure AI Search + Azure OpenAI RAG implementation

from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION,
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    AZURE_SEARCH_INDEX
)


openai_client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION
)


search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)


def retrieve_documents(question):

    results = search_client.search(
        search_text=question,
        top=3
    )

    documents = []

    for result in results:

        content = result.get("content", "")

        if content:
            documents.append(content)

    return documents


def generate_answer(question, documents):

    context = "\n\n".join(documents)

    prompt = f"""
You are an enterprise AI assistant.

Answer the user's question using the provided context.

If the answer is not available in the context,
say that the information is not available.

Context:
{context}

Question:
{question}
"""

    response = openai_client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": "You answer questions using retrieved enterprise documents."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def ask_rag(question):

    documents = retrieve_documents(question)

    answer = generate_answer(
        question,
        documents
    )

    return {
        "question": question,
        "documents": documents,
        "answer": answer
    }