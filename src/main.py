from threading import Thread
import cv2
import logging
from pynput.keyboard import Listener, Key
from models.faceRecognition import FaceRecognition
from models.database import Database
from models.interface import Main_Interface
from gui.application import Application

logger = logging.getLogger(__name__)
logging.basicConfig(filename="faceRecognition.log",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    encoding='utf-8',
                    level=logging.DEBUG)

def on_press(key):
    print(key)
    if key == Key.f1:
        app.root.deiconify()
        app.root.focus_force()
        app.open=True

def update_camera(app):
    video_capture = cv2.VideoCapture(0)
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        frame=cv2.flip(frame, 1)
        # Only process every other frame of video to save time
        if process_this_frame and ret :
            fr.process_frame(frame)
        process_this_frame = not process_this_frame

        # Display the resulting image
        if ret:
            #cv2.imshow('Video', fr.show_frame(frame))
            app.update(fr.show_frame(frame))


db = Database()
fr = FaceRecognition(db, logger)
interface = Main_Interface(db, fr)
app=Application(interface)

thread = Thread(target=update_camera, args=[app])
thread.daemon=True
thread.start()

listener = Listener(on_press=on_press)
listener.start()

print("Press [F1] to open the GUI")

app.root.mainloop()
