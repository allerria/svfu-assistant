from api import *
from app import app

if __name__ == '__main__':
    db.bind(**app.config['PONY'])
    db.generate_mapping(create_tables=True)
    app.run(host='0.0.0.0')
