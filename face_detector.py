# import Libraries
import os
import sys
import cv2

# Create a function to capture human face in front of camera
# and draw a square around the face.


def detector():

    cap = cv2.VideoCapture(0)
    # VideoCapture will capture the first frame that your camera captures
    # as soon as this function is called. And store that in cap variable

    # We are using here haarcascade classifiers.
    # This code line loads the face_cascade classifier.
    face_cascade = cv2.CascadeClassifier(os.path.dirname(
        sys.argv[0]) + '/haarcascade_frontalface_alt2.xml')

    # Start an infinite loop so that we get a continuous real time series of
    # frame for observation
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # If there is any face on the camera, our cascade classifier will
        # return the position of the faces (if more than one) that are
        # in the screen else returns None.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)

        # Loop over the faces and draws a Square of 2px on the face!
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # To stop the program, and close the output screen,
        # press 'q' button through keyboard.
        # Script will leave the loop.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When Everything is done release the capture
    cap.release()
    cv2.destroyAllWindows()


# Calling detector function
detector()
