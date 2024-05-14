"""Group database functions"""

from pymongo import MongoClient
import numpy as np

class Database:
    """Create and manage the database for encodings from face recognition"""
    def __init__(self):
        # Crie uma conexão usando o MongoClient. Você pode importar o MongoClient ou usar o PyMongo.MongoClient
        client = MongoClient()
        
        # Crie o banco de dados para nosso exemplo (usaremos o mesmo banco de dados ao longo do tutorial
        self.client = client.faceRecognition

    def get_data(self):
        "Get name of a person based on image path"
        return {x["name"]: np.array(x["encoding"]) for x in self.client.person.find({}, {"_id": 0})}
 
    def insert_person(self, name, encoding):
        """Insert a new person on database"""
        self.client.person.insert_one({"name": name, "encoding": list(encoding)})

    def close(self):
        self.client.close()