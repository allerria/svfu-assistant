from api import *

if __name__ == '__main__':
    db.bind(**app.config['PONY'])
    db.generate_mapping()
    app.run(host='0.0.0.0')
