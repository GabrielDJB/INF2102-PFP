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
from flask import Flask, request

# ------------------------------------------
# Initializing and configuring application
# ------------------------------------------

# Instantiating application
app = Flask(__name__)

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

    print(instance)

    # TODO: Returning server response w/ instance
    if request.method == "GET":
        return instance["text"]
    else:
        return "This service only supports GET protocols"