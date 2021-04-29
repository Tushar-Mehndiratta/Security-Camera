[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)   

# Webcam-Security-Camera
This python program will allow you to detect any motion that occurs in front of the builtin webcam and send a snip of the motion to the owner's mail ID.

#### Requirement:
1. Python3
2. OpenCV(libraries)


#### Main Logic: 
Videos can be treated as stack of pictures called frames. Here i am comparing different frames(pictures) to the first frame which should be static(No movements initially). We compare two images by comparing the intensity value of each pixels.

#### Analysis of all windows
After running the code there 4 new window will appear on screen. Output of each frame is added in this repository.

1. Gray Frame: In Gray frame the image is a bit blur and in grayscale we did so because, In gray pictures there is only one intensity value whereas in RGB(Red, Green and Blue) image thre are three intensity values. So it would be easy to calculate the intensity difference in grayscale.

2. Difference Frame: Difference frame shows the difference of intensities of first frame to the current frame.

3. Threshold Frame: If the intensity difference for a particular pixel is more than 30(in my code) then that pixel will be white and if the difference is less than 30 that pixel will be black.

4. Color Frame: In this frame you can see the color images in color frame along with green contour around the moving objects.
