from flask import Flask
from endpoints import *

"""
comment
"""
def create_app():
    app = Flask(__name__)
    app.add_url_rule("/tv_series", methods=["GET"], view_func=get_tv_series_posters_and_id)
    app.add_url_rule("/tv_series_details", methods=["GET"], view_func=get_tv_series_metadata_by_id)
    app.add_url_rule("/chatbot", methods=["POST"], view_func=get_res_from_llm)
    app.add_url_rule("/cbf", methods=["GET"], view_func=get_cbf_rec)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()