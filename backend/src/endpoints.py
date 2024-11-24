from database import get_or_create_collection
from chatbot import chatbot
from flask import request, abort, jsonify
import json
import re

"""
comment
"""
def hello_world():
    if "query" not in request.json.keys():
        abort(400, description="Missing query in the request.")

    query_text = request.json["query"]
    collection = get_or_create_collection()
    results = collection.query(query_texts=[query_text], n_results=1)

    return json.dumps(results["documents"][0], indent=4)

"""
comment
check if movie with that id exists !
"""
def get_movie_metadata_by_id():
    number = request.args.get('id')
    id = str("id" + number)
    collection = get_or_create_collection()
    results = collection.get(
        ids=[id],
        include=["metadatas"]
    )

    for key, value in results["metadatas"][0].items():
        if isinstance(value, str):
            if value.lower() == "true":
                results["metadatas"][0][key] = True
            elif value.lower() == "false":
                results["metadatas"][0][key] = False
        if bool(re.fullmatch(r'[0-9.]+', value)):
            results["metadatas"][0][key] = float(value)
    return jsonify(results["metadatas"][0])

"""
comment
"""
def get_movie_posters_and_id():
    page = request.args.get('page')
    
    if not page:
        abort(400, description="Missing page number in the request.")
    if not page.isdigit():
        abort(400, description="Page must be a number")

    collection = get_or_create_collection()
    results = collection.get(
        ids=[f"id{int(page)*50 + x}" for x in range(0,50)],
        include=["metadatas"]
    )
    output = {id_: {"poster_path": metadata['poster_path'], "title": metadata['name']} for id_, metadata in zip(results["ids"], results["metadatas"])}
    return json.dumps(output)

"""
comment
"""
def get_res_from_llm():
    query = request.get_json().get('query')
    if not query:
        abort(400, description="Missing query value in the request.")
    answer_body = chatbot.invoke_llm(query)
    print(answer_body)
    response_dict = {"response": answer_body[answer_body.find('Answer:') + len('Answer:'):]}
    return json.dumps(response_dict)