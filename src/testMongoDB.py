from pymongo import MongoClient
import pprint
client = MongoClient("localhost", 27017)

db=client["faceRecognition"]

#db.person.delete_many({"name": "Pedro"})
for person in db.person.find():
	pprint.pprint(person)

#db.pessoas.insert_one({"nome": "Pedro", "encoding": []})

