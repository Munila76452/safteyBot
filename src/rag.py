import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings

def load_txt_documents(folder):
    docs = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                docs.append(
                    Document(
                        page_content=text,
                        metadata={"source": file}
                    )
                )
    return docs
def build_vector_db():

    docs = load_txt_documents("data/Project")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    import os
    from langchain_openai import AzureOpenAIEmbeddings

    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        azure_deployment="text-embedding-3-small",
        api_version="2024-12-01-preview"
    )

    db = Chroma.from_documents(chunks, embeddings)
    return db

def retrieve_context(db, question):

    results = db.similarity_search(question, k=3)

    context = "\n".join([doc.page_content for doc in results])

    return context
