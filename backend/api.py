from models import *
from app import app
from prepod_parser import get_prepod_schedule, get_schedule2
from flask import request


@app.route("/search")
def search_prepod():
    q = request.args.get("q")
    print(q)
    prepods = get_prepods(q)
    return prepods


@app.route("/schedule/<id>")
def get_schedule_prep(id):
    return get_prepod_schedule(id)


@app.route("/schedule2/<group_name>")
def get_schedule(group_name):
    return get_schedule2(group_name)
