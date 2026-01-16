from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of Paris"
]

vector_doc = embedding.embed_documents(texts=documents)

print(vector_doc)