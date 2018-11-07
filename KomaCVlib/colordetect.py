import cv2
import numpy as np

class ColorDetect:
    def __init__(self,color_label=[],color_range=[]):
        self.color_label = color_label
        self.color_range = color_range
        if len(self.color_label) == 0:
            self.color_label = ["Red","Green","Blue"]
            self.color_range = [[0,255],[0,255],[0,255]]

    def DetectColorArea(self,img_rgb,color):
        if not color in self.color_label:
            print("Error: No color " + str(color) + " in color label")
            return False

        img_hsv = cv2.cvtColor(img_rgb,cv2.CV_BGR2HSV)
        img_medianBlur(img_hsv,7)
        lower_range = np.array([])
        upper_range = np.array([])

    def DetectWithCamera(self):
        cap = cv2.VideoCapture(0)
        while(1):

            # Take each frame
            _, frame = cap.read()

            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # define range of blue color in HSV
            lower_blue = np.array([110,50,50])
            upper_blue = np.array([130,255,255])

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue)

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame,frame, mask= mask)

            cv2.imshow('frame',frame)
            cv2.imshow('mask',mask)
            cv2.imshow('res',res)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()

colclass = ColorDetect()
colclass.DetectWithCamera()
