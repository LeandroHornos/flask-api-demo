from flask import Flask, jsonify
import json

from jinja2 import Undefined


# Mock Database

# I use a randomly generated json of users
# from mockaroo.com as a sample database

with open("mock-users.json") as usersFile:
    data = json.load(usersFile)
    print(data[-1])

# Flask App
app = Flask(__name__)

# Routes


@app.route("/ping")
def ping():
    return jsonify({"message:": "Pong"})


@app.route("/allusers")
def allUsers():
    return jsonify(data)


@app.route("/userbyid/<string:user_id>")
def userById(user_id):
    id = int(user_id)
    user = getUserById(id, data)
    return jsonify(user)


# Helper functions
def getUserById(id, users):
    print("id:", id)
    match = {"user": Undefined, "message": "not found"}
    for user in users:
        if user["id"] == id:
            match = {"user": user, "message": "user found"}
            break
    return match


if __name__ == "__main__":
    app.run(debug=True, port=5000)
