#!/usr/bin/env python

import cv2
import imutils
import numpy as np

# Read the image, convert it into grayscale, and make in binary image for threshold value of 1.
img = cv2.imread('/home/pi/projects/KISSS/images/before_crop.jpg')
resized = imutils.resize(img, width=600)
ratio = img.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)

# show the output image
cv2.imshow("Image", thresh)
cv2.waitKey(0)

# Now find contours in it. There will be only one object, so find bounding rectangle for it.
contours,hierarchy,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#_,contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)

# Now crop the image, and save it into another file.
crop = img[y:y+h,x:x+w]
cv2.imwrite('/home/pi/projects/KISSS/images/after_crop.jpg',crop)
