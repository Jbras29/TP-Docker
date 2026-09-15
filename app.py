import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

mongo_client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
database = mongo_client[os.getenv("MONGO_DATABASE", "flask_demo")]
collection = database["objects"]

@app.route("/")
def hello_world():
    object_to_insert = {"message": "Hello, MongoDB!"}
    inserted = collection.insert_one(object_to_insert)
    saved_object = collection.find_one({"_id": inserted.inserted_id})

    return f"<p>Objet écrit puis lu depuis MongoDB : {saved_object['message']}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)