from flask import Flask, jsonify, request
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


@app.route("/addnewuser", methods=["POST"])
def addNewUser():
    # Get the last id and use the next number as the new id
    sorted_data = sorted(data, key=lambda d: d['id'])
    new_id = sorted_data[-1]["id"] + 1
    # Get user data from request
    # Some validation should be done here
    new_user = request.json
    # add new id and save to "database"
    new_user["id"] = new_id
    data.append(new_user)
    with open('mock-users.json', 'w') as outfile:
        outfile.write(json.dumps(data))

    # Update users list

    return jsonify({"message": "success", "user": new_user})

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
