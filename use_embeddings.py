import pymongo
import json
import requests

connection_string = "mongodb+srv://guneeshvats:tSn9J331HDnUg9em@cluster0.xipbw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(connection_string)
db = client.sample_mflix
collection = db.movies

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url, 
        headers = {"Authorization": f"Bearer {hf_token}"}, 
        json={"inputs": text})
    
    if response.status_code!=200:
        raise ValueError(f"Request failes with status code {response.status_code}: {response.text}")
    return response.json()

query = "imaginary characters from outer space at war"

results = collection.aggregate([
    {"$vectorSearch": {
        "queryVector": generate_embedding(query), 
        "path": "plot_embedding_hf",
        "numCandidates":100, 
        "limit":4,
        "index":"PlotSemanticSearch"
    }}
])

for document in results:
    print(f"movie name: {document["title"]}, \n Movie Plot: {document["plot"]}\n")