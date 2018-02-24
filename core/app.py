# set FLASK_APP=app.py
# flask run

from flask import Flask
from flask import request
from flask import json
<<<<<<< HEAD
from flask_cors import CORS
=======
from flask import jsonify
import path


>>>>>>> 41f7d4cfbedeb1917d834dce66ae08dbeb67224f
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    d = path.run_pathfinder()
    return jsonify(d)

@app.route("/inputs", methods=["POST"])
def fetchInputs():
<<<<<<< HEAD
    return request.get_data() 
=======
    if request.headers['Content-Type'] == 'application/json':
        answer = {
            "test":"Test2",
            "test3": 6
        }
        return json.jsonify(answer)
>>>>>>> 41f7d4cfbedeb1917d834dce66ae08dbeb67224f
