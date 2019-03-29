from models import *
from app import app
from prepod_parser import get_prepod_schedule
from flask import request, jsonify


@app.route("/search")
def search_prepod():
    q = request.args.get("q")
    print(q)
    prepods = get_prepods(q)
    return prepods


@app.route("/schedule/<id>")
def get_schedule(id):
    return get_prepod_schedule(id)
