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
    d = path.run_pathfinder()
    return jsonify(d)

@app.route("/inputs", methods=["POST"])
def fetchInputs():
    d = path.run_pathfinder()
    path.adjust_path()
    return jsonify(d)
    # return request.get_data()
