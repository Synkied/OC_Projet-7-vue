from flask import Flask
from flask_cors import CORS

app = Flask(__name__)


# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
