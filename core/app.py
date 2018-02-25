# set FLASK_APP=app.py
# flask run

from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS
from flask import jsonify
import path

app = Flask(__name__)
CORS(app)

@app.route("/inputs", methods=["POST"])
def fetchInputs():
    return jsonify(path.run_pathfinder())
    # return request.get_data()
