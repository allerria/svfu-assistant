from pony.orm import Database, Required, select, Optional

db = Database()


class Prepod(db.Entity):
    name = Required(str)
    phone = Optional(str)
    mail = Optional(str)
    img_url = Optional(str)
    address = Optional(str)


def get_prepods(q):
    prepods = select(prep for prep in Prepod if prep.name.startswith(q))[:].to_json()
    return prepods
