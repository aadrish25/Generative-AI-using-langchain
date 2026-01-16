from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# create the list of documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills",
    "Sachin Tendulkar, also know as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record breaking double centuries.",
    "Jasprit Bumrah is an Indian bowler known for his unorthodox action and yorkers."
]

# user query
user_query = "Tell me about Bumrah"

# first convert the documents into embeddings
doc_embeddings = embedding.embed_documents(documents)

# query embedding
query_embedding = embedding.embed_query(user_query)

# then calculate similarity score of the query with all documents
similarity_scores=cosine_similarity([query_embedding],doc_embeddings)

# get the index of the max similarity score
answer_idx = np.argmax(similarity_scores[0])

# and exactly that index is our answer
answer = documents[answer_idx]

print(f"The answer is present in : {answer}")

