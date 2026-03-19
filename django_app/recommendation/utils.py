
from django.conf import settings
from pymongo import MongoClient
import sys

# With django-mongodb-backend, we rely on the ORM or the connection settings.
# This file is kept if you need raw access for advanced pipelines not supported by the backend yet.

def get_mongo_client():
    try:
        # Use the URI from settings
        uri = settings.DATABASES['default']['HOST']
        client = MongoClient(uri)
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}", file=sys.stderr)
        return None

def get_db():
    client = get_mongo_client()
    if client:
        db_name = settings.DATABASES['default']['NAME']
        return client[db_name]
    return None

def get_collection():
    db = get_db()
    if db is not None:
        collection_name = settings.DATABASES['default'].get('COLLECTION_NAME', 'recommendation_movies')
        return db[collection_name]
    return None
