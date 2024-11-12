from flask import Flask
import os
import json

app = Flask(__name__)
config_data = None

def loadConfigFile():
    global config_data
    if config_data is None:
        if os.path.exists("config.json"):
            with open("config.json", "r") as read_file:
                config_data = json.load(read_file)
        else:
            print("Error: Config file missing.")


def checkFile(name: str):
    if config_data:
        return name in config_data
    else:
        return "Error: Config file missing."

@app.route("/")
def hello():
    return "Welcome to my system, Please login"

@app.route("/login/<name>")
def login(name):
    flag = checkFile(name)
    if flag:
        return "Access granted to " + name
    else:
        return "Access denied to " + name

if __name__ == "__main__":
    loadConfigFile()
    app.run(host="0.0.0.0", port=80)