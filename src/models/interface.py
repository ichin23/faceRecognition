from threading import Thread
import cv2

class Main_Interface:
    def __init__(self, db, fr):
        self.db = db
        self.fr =fr

    def get_encoding(self, img):
        return self.fr.get_encoding(img)

    def get_names(self):
        return self.fr.known_names

    def refresh_names(self):
        self.fr.get_names()

    def insert_person(self, name, encoding):
        self.db.insert_person(name, encoding)

    def delete_on_index(self, i):
        self.db.delete_person(self.fr.ids()[i])
