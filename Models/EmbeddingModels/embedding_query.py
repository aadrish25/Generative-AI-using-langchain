from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

# create an embedding object
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

query = "Delhi is the capital of India"

vector = embedding.embed_query(text=query)

print(str(vector))