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

        img_hsv = cv2.cvtColor(img_rgb,CV_BGR2HSV)
        for
