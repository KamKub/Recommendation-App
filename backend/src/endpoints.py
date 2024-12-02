from database import get_or_create_collection, get_data_from_collection
from chatbot import chatbot
from cbf import Cbf_model
from flask import request, abort, jsonify
import json
import re

"""
comment
"""
def get_movie_metadata_by_id():
    number = request.args.get('id')
    id = str("id" + number)
    collection = get_or_create_collection("tv_series_rag", "l2")
    results = get_data_from_collection(collection=collection, ids=id)

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

    collection = get_or_create_collection("tv_series_rag", "l2")
    results = get_data_from_collection(collection=collection, ids=[f"id{int(page)*50 + x}" for x in range(0,50)])
    output = {id_: {"poster_path": metadata['poster_path'], "title": metadata['name']} for id_, metadata in zip(results["ids"], results["metadatas"])}
    return json.dumps(output)

"""
comment
"""
def get_res_from_llm():
    query = request.get_json().get('query')

    if not query:
        abort(400, description="Missing query value in the request.")
    
    get_or_create_collection("tv_series_rag", "l2") 
    answer_body = chatbot.invoke_llm(query)
    print(answer_body)
    response_dict = {"response": answer_body[answer_body.find('Answer:') + len('Answer:'):]}
    return json.dumps(response_dict)

"""
comment
"""
def get_cbf_rec():
    user_id = request.args.get('id')

    if not user_id:
        abort(400, description="Missing id number in the request.")
    if not user_id.isdigit():
        abort(400, description="Id must be a number")

    cbf_model = Cbf_model(user_id=int(user_id))
    series = cbf_model.recommend_series()    
    return series.head().to_dict(orient='records')