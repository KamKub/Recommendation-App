from flask import Flask
from endpoints import *

"""
comment
"""
def create_app():
    app = Flask(__name__)
    app.add_url_rule("/query", methods=["GET"], view_func=hello_world)
    app.add_url_rule("/movies", methods=["GET"], view_func=get_movie_posters_and_id)
    app.add_url_rule("/movie_details", methods=["GET"], view_func=get_movie_metadata_by_id)
    app.add_url_rule("/chatbot", methods=["POST"], view_func=get_res_from_llm)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()