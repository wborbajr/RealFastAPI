from pymongo import MongoClient
import pprint

MONGO_HOST = "127.0.0.1"
MONGO_PORT = "27017"
MONGO_DB = "realfastapi"
MONGO_USER = "real"
MONGO_PASS = "fastapi"

connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

pprint.pprint(db.collection_names())
