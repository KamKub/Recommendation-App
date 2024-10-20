import chromadb
from dataset import get_combined_data, get_data_list

"""
comment
"""
def get_or_create_collection():
    chroma_client = chromadb.PersistentClient(path="movie_database")

    #movies for 100, movies_short for 5 movies
    collection_name = "movies" 

    if(len(chroma_client.list_collections()) == 0):
        create_new_collection()

    return chroma_client.get_collection(name=collection_name)

"""
comment
"""
def create_new_collection():
    chroma_client = chromadb.PersistentClient(path="movie_database")
    collection_name = "movies_short"

    collection = chroma_client.create_collection(name=collection_name)
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