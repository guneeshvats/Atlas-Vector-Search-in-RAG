import pymongo
import json
import requests

connection_string = "mongodb+srv://guneeshvats:tSn9J331HDnUg9em@cluster0.xipbw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(connection_string)
db = client.sample_mflix
collection = db.movies

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
# will return the curso object with 5 results
# items  = collection.find().limit(5)

# for item in items:
#     print(item)
# We are successfully connected to our database

# Setting up the embedding creation function
# Hugging face token  - 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

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url, 
        headers = {"Authorization": f"Bearer {hf_token}"}, 
        json={"inputs": text})
    
    if response.status_code!=200:
        raise ValueError(f"Request failes with status code {response.status_code}: {response.text}")
    return response.json()

# print(generate_embedding("Guneesh Vats is awesome"))
for doc in collection.find({'plot':{"$exists": True}}).limit(50):
    doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
    collection.replace_one({'_id': doc['_id']}, doc)

# instead of replacing we can create a separate collection of only embeddings (depends on type of task)


# Creating a vector search index
