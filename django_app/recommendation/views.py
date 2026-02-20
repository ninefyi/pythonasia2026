
from django.shortcuts import render
from django.conf import settings
from .models import Movie
import voyageai

# Initialize Voyage Client
voyage_client = voyageai.Client(api_key=settings.VOYAGE_API_KEY)

def index(request):
    return render(request, 'recommendation/index.html')

def search_view(request):
    query = request.GET.get('q')
    if not query:
        return render(request, 'recommendation/index.html')

    # 1. Vector Search
    vector_results = []
    try:
        query_embedding = voyage_client.embed([query], model="voyage-large-2").embeddings[0]
        
        # Access the raw collection from the model
        # The official backend exposes the underlying collection via default_manager
        # specific implementation details might vary, but raw_aggregate is often supported or we use the connection
        from django.db import connection
        
        # Get the collection name from the model's meta
        collection_name = Movie._meta.db_table
        
        # For the official backend, we might need to access the database wrapper
        # To keep it robust, we can use the raw pymongo collection if accessible, OR
        # use the backend's vector search capabilities if they are exposed via ORM.
        # As of early versions, raw aggregation is the safest bet for hybrid pipelines.
        
        with connection.cursor() as cursor:
            # The cursor in django-mongodb-backend might behave differently. 
            # Let's try to get the PyMongo collection directly from the connection connection.
            # "connection.connection" usually gives the PyMongo client or database
            pass 

        # Let's assume standard PyMongo access for the complex pipeline
        # The backend sets 'pythonasia_workshop' as the DB name
        # We can construct strictly via PyMongo for the pipeline part to guarantee $vectorSearch works
        # This bypasses the ORM for the *search* but uses the ORM-managed collection.
        
        # Re-establishing a direct client for the Search Logic to ensure full Atlas Search support
        # without worrying about ORM limitations for $vectorSearch stage.
        # In a real app, you'd extract 'get_collection' from the django connection properly.
        from pymongo import MongoClient
        client = MongoClient(settings.DATABASES['default']['URI'])
        db = client[settings.DATABASES['default']['NAME']]
        collection = db[collection_name]

        vector_pipeline = [
            {
                "$vectorSearch": {
                    "index": "vector_index",
                    "path": "embedding",
                    "queryVector": query_embedding,
                    "numCandidates": 100,
                    "limit": 20
                }
            },
            {
                "$project": {
                    "_id": 1,
                    "title": 1,
                    "plot": 1,
                    "score": {"$meta": "vectorSearchScore"}
                }
            }
        ]
        vector_results = list(collection.aggregate(vector_pipeline))

        # 2. Keyword Search (Atlas Search)
        keyword_pipeline = [
            {
                "$search": {
                    "index": "default", 
                    "text": {
                        "query": query,
                        "path": ["title", "plot"]
                    }
                }
            },
            {
                "$limit": 20
            },
            {
                "$project": {
                    "_id": 1,
                    "title": 1,
                    "plot": 1,
                    "score": {"$meta": "searchScore"}
                }
            }
        ]
        keyword_results = list(collection.aggregate(keyword_pipeline))

    except Exception as e:
        print(f"Search failed: {e}")
        vector_results = []
        keyword_results = []

    # 3. Hybrid Fusion (RRF)
    k = 60
    doc_scores = {}

    for rank, doc in enumerate(vector_results):
        doc_id = str(doc['_id'])
        score = 1 / (k + rank + 1)
        if doc_id not in doc_scores:
            doc_scores[doc_id] = {"doc": doc, "score": 0}
        doc_scores[doc_id]["score"] += score

    for rank, doc in enumerate(keyword_results):
        doc_id = str(doc['_id'])
        score = 1 / (k + rank + 1)
        if doc_id not in doc_scores:
            doc_scores[doc_id] = {"doc": doc, "score": 0}
        doc_scores[doc_id]["score"] += score
        if "doc" not in doc_scores[doc_id]: 
             doc_scores[doc_id]["doc"] = doc

    final_results = sorted(doc_scores.values(), key=lambda x: x['score'], reverse=True)
    display_results = [item['doc'] for item in final_results[:20]]

    return render(request, 'recommendation/index.html', {"results": display_results, "query": query})
