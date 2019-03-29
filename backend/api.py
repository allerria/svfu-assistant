from models import *
from app import app
from flask import request, jsonify


@app.route("/search")
def search_prepod():
    q = request.args.get("q")
    print(q)
    prepods = get_prepods(q)
    return prepods
