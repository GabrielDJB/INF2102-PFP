# -------------------------------------------------------------------
# APP.PY file
#
# Author: Gabriel D. J. Barbosa
#
# Description:
#  File implementing back-end API services. Built on Flask and
#  dependent on different libraries, described in requirements.txt.
# -------------------------------------------------------------------

# Importing libraries
from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_cors import CORS

# ------------------------------------------
# Initializing and configuring application
# ------------------------------------------

# Instantiating application and CORS
app = Flask(__name__)
CORS(app)

# Instantiating database client on server start
client = MongoClient()


# ------------------
# Routing services
# ------------------

# Default Service
@app.route('/')
def index():

    db = client["focus-chat"] # Zooming to collection
    collection = db["test"]
    instance = collection.find_one() # Retrieving an instance

    # Creating response dict to be turned into JSON
    response = {}

    # Returning server response w/ instance
    if request.method == "GET":
        response["text"] = instance["text"]
        return jsonify(response)
    else:
        response["text"] = "This service only supports GET protocols"
        return jsonify(response)