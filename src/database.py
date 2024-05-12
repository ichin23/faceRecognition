import sqlite3 as sql

_name = "faceRecognition.db"

class Database:
    def __init__(self):
        sql.connect(_name)
