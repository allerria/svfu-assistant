from api import *


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response


if __name__ == '__main__':
    db.bind(**app.config['PONY'])
    db.generate_mapping()
    app.run(host='0.0.0.0')
