
import time
import json

import requests as requests
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
from random import randint

client = MongoClient("mongodb+srv://mukesh:hello123@finalproject.t1pva.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.bitcoin

r = requests.get("https://api.nomics.com/v1/prices?key=3ceb712731b63f951a9bf1de3236dc88")
if r.status_code == 200:
    bitcoin_data = r.json()
    result = db.universal.insert_many(bitcoin_data)
    print(bitcoin_data)


@app.route('/')
def hello_world():
    return 'Data Programming Final Project'
if __name__ == '__main__':
    app.run()
