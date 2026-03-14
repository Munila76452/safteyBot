import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
print("Text splitter working")