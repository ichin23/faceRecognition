import cv2
from faceRecognition import FaceRecognition
from database import Database
from application import Application


video_capture = cv2.VideoCapture(0)
db = Database()
fr = FaceRecognition(db)
app=Application(db, fr, video_capture)

PROCESS_THIS_FRAME=True

while True:
    if not app.running:
        if app.full_stop:
            break
        app.root.update()
        continue
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame=cv2.flip(frame, 1)
    # Only process every other frame of video to save time
    if PROCESS_THIS_FRAME and frame is not None :
        fr.process_frame(frame)

    PROCESS_THIS_FRAME = not PROCESS_THIS_FRAME

    # Display the resulting image
    #cv2.imshow('Video', frame)
    if frame is not None and app.running:
        app.update(fr.show_frame(frame))

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
#cv2.destroyAllWindows()

