import chromadb
from dataset import get_combined_data, get_data_list

"""
comment
"""
def get_or_create_collection(collection_name, distance_method):
    chroma_client = chromadb.PersistentClient(path="tv_series_database")
    try:
        return chroma_client.get_collection(name=collection_name)
    except ValueError:
        create_new_collection(collection_name, distance_method)
        return chroma_client.get_collection(name=collection_name)

"""
comment
"""
def create_new_collection(collection_name, distance_method):
    chroma_client = chromadb.PersistentClient(path="tv_series_database")

    collection = chroma_client.create_collection(name=collection_name, metadata={"hnsw:space": distance_method})
    add_data_to_database(collection)
    
"""
comment
"""
def add_data_to_database(collection):
    combined_data = get_combined_data()
    data_list = get_data_list()
    data_length = len(combined_data)

    for i in range(0,data_length,5000):
        batch_size = min(5000, data_length - i)
        collection.add(
            documents=combined_data[i:i+batch_size],
            metadatas=data_list[i:i+batch_size],
            ids=[f"id{x}" for x in range(i,i+batch_size)],
        )

"""
comment
"""
def get_data_from_collection(collection,ids=None):
    if ids is None:
        return collection.get(
            include=["metadatas"]
        )
    else:
        return collection.get(
            ids=ids,
            include=["embeddings", "metadatas"]
        )