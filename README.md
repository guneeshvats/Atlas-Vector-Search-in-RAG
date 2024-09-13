# Semantic Search for Movie Recommendation
Atlas Vector Search in RAG


```
pip install pymongo
```

Since we are using a sample movie dataset from the MongoDB Atlas Server. 
Lets get connected to the mongo Atlas Database through our local environment. 


Go to your project > Drivers > connection string in place of <Your MongoDB URI> and in this string replace the password with your actual password

For the embedding creation funcion we are using a free model from hugging face: `sentence-transformers/all-MiniLM-L6-v2`

```
pip install sentence-transformers
```

In the dataset there is a summary of the plot in the `plot` field. 
First we will generate embeddings of those plot themes. 
Once we generate embeddings we can see the dataset is connected to mongoDB Atlas server we can see a new field there
![image](https://github.com/user-attachments/assets/dd77b1a8-a514-4551-8496-b96bd66c43a9)


Then we do this 

![image](https://github.com/user-attachments/assets/39b2e64a-ff66-413d-bbf1-c2e41668a539)
