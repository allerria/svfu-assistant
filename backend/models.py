from pony.orm import Database, Required, select, Optional
import json

db = Database()


class Prepod(db.Entity):
    name = Required(str)
    phone = Optional(str)
    mail = Optional(str)
    img_url = Optional(str)
    address = Optional(str)


def get_prepods(q):
    result = {"prepods": [p.to_dict() for p in Prepod.select(lambda p: q.lower() in p.name.lower())]}
    return json.dumps(result)


def get_prepod(id):
    id = int(id)
    return json.dumps(Prepod[id].to_dict())
