from flask import Flask
from pony.flask import Pony
from backend.config import config

app = Flask(__name__)
app.config.update(config)

Pony(app)
