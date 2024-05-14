import os
import face_recognition
import cv2

def getEncodings(images:str="images")->dict:
    images_encodings = {}
    for file in os.listdir(images):
        path = os.path.join(images, file)
        imageP = face_recognition.load_image_file(path)
        try:
            pess = face_recognition.face_encodings(imageP)[0]
            images_encodings[path] = pess
        except:
            pass

    return images_encodings

def showVideo(frame, face_locations, face_names ):
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
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

    # Display the resulting image
    cv2.imshow('Video', frame)
