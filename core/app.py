# set FLASK_APP=app.py
# flask run

from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Server running!"

@app.route("/inputs", methods=["POST"])
def fetchInputs():
    return request.get_data() 