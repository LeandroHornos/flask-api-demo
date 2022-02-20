from flask import Flask, jsonify
import json


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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
