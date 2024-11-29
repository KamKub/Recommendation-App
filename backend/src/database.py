import chromadb
from dataset import get_combined_data, get_data_list, get_combined_data_for_cbf

"""
comment
"""
def get_or_create_collection(collection_name, combined_data_format):
    chroma_client = chromadb.PersistentClient(path="tv_series_database")
    try:
        return chroma_client.get_collection(name=collection_name)
    except ValueError:
        create_new_collection(collection_name, combined_data_format)
        return chroma_client.get_collection(name=collection_name)

"""
comment
"""
def create_new_collection(collection_name, combined_data_format):
    chroma_client = chromadb.PersistentClient(path="tv_series_database")

    collection = chroma_client.create_collection(name=collection_name)
    add_data_to_database(collection, combined_data_format)
    
"""
comment
"""
def add_data_to_database(collection, combined_data_format):
    if(combined_data_format == 'cbf'):
        combined_data = get_combined_data_for_cbf()
    else:
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