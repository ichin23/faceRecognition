import face_recognition
import cv2
import numpy as np
import time

class FaceRecognition():

    def __init__(self, db, logger):
        self.db =db
        self.logger = logger

        self.get_names()

        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True
        self.last_face = None

    def get_names(self):
        """Save persons of database on memory"""
        self.data = self.db.get_data()
        self.known_face_encodings  = [x[1] for x in self.data.values()]
        self.known_names = [x[0] for x in self.data.values()]

    def ids(self):
        return list(self.data.keys())

    def process_frame(self, frame):
        """Find and compare faces on frame"""
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color to RGB color (which face_recognition uses)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

        # Find all the faces and face encodings in the current frame of video
        self.face_locations = face_recognition.face_locations(rgb_small_frame)
        self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
        
        self.face_names = []
        for face_encoding in self.face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_names[first_match_index]
            
            self.logger.info(f"Face found: {name}")
            print(name)
            self.face_names.append(name)
        return self.face_names

    def get_encoding(self, img):
        """return the face encoding from the face on img array"""
        return face_recognition.face_encodings(img)[0]

    def show_frame(self, frame) -> np.array:
        """Select face on frame"""
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return frame
