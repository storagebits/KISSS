#!/usr/bin/env python

import cv2
import numpy as np

# Read the image, convert it into grayscale, and make in binary image for threshold value of 1.
img = cv2.imread('/home/pi/Desktop/KISSS_Capture/000/DSC_000_1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)

# Now find contours in it. There will be only one object, so find bounding rectangle for it.
#ncontours,hierarchy,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
_,contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)

# Now crop the image, and save it into another file.
crop = img[y:y+h,x:x+w]
cv2.imwrite('/home/pi/Desktop/KISSS_Capture/000/DSC_000_1_cropped.jpg',crop)
