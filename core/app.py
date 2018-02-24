# set FLASK_APP=app.py
# flask run

from flask import Flask
from flask import request
from flask import json
from flask import jsonify
import path


app = Flask(__name__)

@app.route("/")
def hello():
    d = path.run_pathfinder()
    return jsonify(d)

@app.route("/inputs", methods=["POST"])
def fetchInputs():
    if request.headers['Content-Type'] == 'application/json':
        answer = {
            "test":"Test2",
            "test3": 6
        }
        return json.jsonify(answer)
