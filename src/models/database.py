"""Group database functions"""

from pymongo import MongoClient
import numpy as np

class Database:
    """Create and manage the database for encodings from face recognition"""
    def __init__(self):
        client = MongoClient()
        self.client = client.faceRecognition

    def get_data(self):
        """Get name of a person based on image path
        :return map with name and encoding os people in database"""
        return {x["_id"]: (x["name"], np.array(x["encoding"])) for x in self.client.person.find()}

    def insert_person(self, name, encoding):
        """Insert a new person on database
        :param name: person name
        :param encoding: array of the face encoding"""
        self.client.person.insert_one({"name": name, "encoding": list(encoding)})

    def delete_person(self, id_person):
        self.client.person.delete_one({"_id": id_person})

    def close(self):
        """Close the database connection"""
        self.client.close()
