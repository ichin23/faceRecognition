from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
client = MongoClient("localhost", 27017)

db=client["faceRecognition"]

#db.person.delete_many({"_id": ObjectId('664683f7dd7130e004956e1f')})
for person in db.person.find():
	pprint.pprint(person)

#db.pessoas.insert_one({"nome": "Pedro", "encoding": []})

