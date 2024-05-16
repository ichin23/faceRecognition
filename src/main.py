from threading import Thread
import cv2
import asyncio
from models.faceRecognition import FaceRecognition
from models.database import Database
from gui.application import Application

def update_camera(app):
    video_capture = cv2.VideoCapture(0)
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        frame=cv2.flip(frame, 1)
        # Only process every other frame of video to save time
        if process_this_frame and ret :
            asyncio.run(fr.process_frame(frame))
        process_this_frame = not process_this_frame

        # Display the resulting image
        if ret:
            #cv2.imshow('Video', fr.show_frame(frame))
            app.update(fr.show_frame(frame))



db = Database()
fr = FaceRecognition(db)
app=Application()

thread = Thread(target=update_camera, args=[app])
thread.daemon=True
thread.start()

app.root.mainloop()
