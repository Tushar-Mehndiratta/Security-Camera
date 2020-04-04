# import Libraries
import os
import sys
import cv2
import time
import pandas
from datetime import datetime


# Create a function to capture human face in front of camera
# and draw a square around the face.


def detector():

    first_frame = None
    status_list = [None, None]
    times = []

    df = pandas.DataFrame(columns=["Start", "End"])

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

        status = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)

        # To store first image/frame of video
        if first_frame is None:
            first_frame = gray
            continue

        # Calculate the difference between the first frame and other frames
        delta_frame = cv2.absdiff(first_frame, gray)

        # Provides a threshold value, such that it will convert
        # the difference value with less than 30 to black.
        # If the difference is greater than 30 it will convert
        # those pixels to white

        # Define the contour area.
        # Basically, add the borders.
        (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Remove noises and shadows. Basically it will keep only that
        # part white, which has area greater than 1000 pixels.
        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            # Status changes when object becomes visible
            status = 1

        # Creates a rectangular box around the object in the frame
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        status_list.append(status)

        status_list = status_list[-2:]
        # Record datetime in a list when change occurs
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())

        # Loop over the faces and draws a Square of 2px on the face!
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 3)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # To stop the program, and close the output screen,
        # press 'q' button through keyboard.
        # Script will leave the loop.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for i in range(0, len(times), 2):
        # Store time values in DataFrame
        df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

    # Write a DataFrame to a CSV file
    df.to_csv("Times.csv")

    # When Everything is done release the capture
    cap.release()
    cv2.destroyAllWindows()


# Calling detector function
detector()
