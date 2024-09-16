from flask import Flask,jsonify,request
from app.handler import db_handler 
import random

app = Flask(__name__)

# Replace this with env var in the future
PG_HOST_IP = "postgres"
PG_HOST_PORT = "5432"

@app.route("/", methods=["GET"])
def first_route():
    return "Hello Bastard", 200

@app.route("/2nd", methods=["GET"])
def second_route():
    return "Hello 2nd Bastard", 200

@app.route("/json", methods=["GET"])
def json_route():
    data = {"return":True}
    rand_num = random.randint(1,100)
    rand_uname = "user-"+str(rand_num)

    db = db_handler() 
    db.connect(PG_HOST_IP, 5432)
    db.insert_user(rand_uname, "pass", "nonadmin")
    db.close()

    return jsonify(data), 200

@app.route("/get_user", methods=["GET"])
def get_user():
    data = {"data":2000}

    db = db_handler() 
    db.connect(PG_HOST_IP, 5432)
    data = db.get_all_user()
    db.close()

    return jsonify(data), 200

@app.route("/gen_data", methods=["GET"])
def gen_data():
    db = db_handler() 
    db.connect(PG_HOST_IP, 5432)
    data = db.create_table()
    db.close()

    return jsonify(data), 200

@app.route("/dhcp_handler", methods=["POST"])
def dhcp_handler():
    status = {}

    return True
