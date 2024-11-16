from flask import Flask
import os
import json
import logging
from printcolors import printGreen, printRed, printBlack

#comment pr1

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s|%(name)s| %(levelname)s|%(message)s',
    handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()  
    ]
    )

app = Flask(__name__)
config_data = None

def loadConfigFile():
    global config_data
    if config_data is None:
        if os.path.exists("config.json"):
            logging.info("Loading configuration file.")
            with open("config.json", "r") as read_file:
                config_data = set(json.load(read_file))
            logging.info("Configuration loaded successfully.")
            logging.info(f"Supported names: {config_data}")
        else:
            logging.error("Error: Config file missing.")

def checkFile(name: str):
    if config_data:
        logging.info(f'Checking if the name: {name} is a valid domain')
        return name in config_data
    else:
        logging.warning('No config file available.')
        return "Error: Config file missing."

@app.route("/")
def hello():
    logging.info("Accessed the home page.")
    return "Welcome to my system, Please login"

@app.route("/login/<name>")
def login(name):
    logging.info(f'Login attempt for name: {name}')
    flag = checkFile(name)
    if flag:
        logging.info(f'Access granted to {name}')
        return printGreen("Access granted to " + name)
    else:
        logging.warning(f'Access denied to {name}')
        return printRed("Access denied to " + name)

@app.route("/addName/<new_name>")
def addName(new_name: str):
    global config_data
    if config_data:
        logging.info("Loading configuration file to update name.")
        config_data.add(new_name)
        if os.path.exists('config.json'):
            with open('config.json', 'w') as config_file:
                json.dump(list(config_data), config_file)
        return printGreen(f'Name: {new_name} added successfully')
        logging.info("Configuration updated successfully.")
        logging.info(f"Updated  names: {config_data}")
        
    

if __name__ == "__main__":
    loadConfigFile()
    logging.info("Starting the Flask app.")
    app.run(host="0.0.0.0", port=80)
