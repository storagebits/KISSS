#!/usr/bin/env python3

import cv2 as cv
import numpy as np
from os import walk


def detect_left_x_mid(treeshold, myimg):
    left = 0
    h,w,c = myimg.shape
    mid_h = int(h/2)
    # Detecting first photo pixel from the middle to avoid the circle light
    for i in range(0, w):
        color = myimg[(mid_h,i)]
        avg = np.mean(myimg[(mid_h,i)])
        if avg >= treeshold :
            if left == 0 :
                left = i
                break
            if i <= left :
                left = i
                    #print(str(i)+","+str(j)+"/"+str(h)+" - "+str(color)+" - "+str(avg)+ " - left : "+str(left))
                break
    #print("middle h left "+str(left))
    for i in range(left, 0, -1):
        a = False
        for j in range(0, h):
            color = myimg[(j,i)]
            avg = np.mean(myimg[(j,i)])
            if avg >= treeshold :
                if i <= left :
                    left = i
                    a = True
                    break
        if a == False:
            break
    #print(left)
    return left
def detect_right_x_mid(treeshold, myimg):
    right = 0
    h,w,c = myimg.shape
    mid_h = int(h/2)
    # Detecting first photo pixel from the middle to avoid the circle light
    for i in range(w-1, -1, -1):
        color = myimg[(mid_h,i)]
        avg = np.mean(myimg[(mid_h,i)])
        if avg >= treeshold :
            if right == 0 :
                right = i
                #print(str(i)+","+str(mid_h)+"/"+str(h)+" - "+str(color)+" - "+str(avg)+ " - right : "+str(right))
                break
            if i >= right :
                right = i
                #print(str(i)+","+str(mid_h)+"/"+str(h)+" - "+str(color)+" - "+str(avg)+ " - right : "+str(right))
                break
    #print("middle h right "+str(right))
    for i in range(right, w):
        a = False
        for j in range(0, h):
            color = myimg[(j,i)]
            avg = np.mean(myimg[(j,i)])
            if avg >= treeshold :
                if i >= right :
                    right = i
                    a = True
                    break
        if a == False:
            break
    #print(right)

    return right
def detect_top_y_mid(treeshold, myimg, left, right):
    top = 0
    h,w,c = myimg.shape
    mid_w = int(w/2)
    for i in range(0, h):
        color = myimg[(i,mid_w)]
        avg = np.mean(myimg[(i,mid_w)])
        if avg >= treeshold :
            top = i
            #print(str(i)+","+str(mid_h)+"/"+str(h)+" - "+str(color)+" - "+str(avg)+ " - right : "+str(right))
            break
    #print("middle w top "+str(top))
    for i in range(top, -1, -1):
        a = False
        for j in range(left, right+1):
            color = myimg[(i,j)]
            avg = np.mean(myimg[(i,j)])
            if avg >= treeshold :
                if j <= top :
                    top = j
                    a = True
                    break
        if a == False:
            break
    #print(top)
    return top
def detect_bottom_y_mid(treeshold, myimg, left, right):
    bottom = 0
    h,w,c = myimg.shape
    mid_w = int(w/2)

    for i in range(h-1, -1, -1):
        color = myimg[(i,mid_w)]
        avg = np.mean(myimg[(i,mid_w)])
        if avg >= treeshold :
            bottom = i
            #print(str(i)+","+str(mid_h)+"/"+str(h)+" - "+str(color)+" - "+str(avg)+ " - right : "+str(right))
            break
    #print("middle w bottom "+str(bottom))

    for i in range(bottom, h):
        a = False
        for j in range(left, right+1):
            color = myimg[(i,j)]
            avg = np.mean(myimg[(i,j)])
            if avg >= treeshold :
                if i >= bottom :
                    bottom = i
                    a = True
                    break
        if a == False:
            break
    #print(bottom)
    return bottom


def cropper(img_source, img, lx, rx, ty, by):
    crop_img=img[ty:by, lx:rx]
    cv.imwrite("/home/pi/Desktop/KISSS_Capture/002/cropped/"+img_source,crop_img)

def getImages():
    f = []
    for (dirpath, dirnames, filenames) in walk("/home/pi/Desktop/KISSS_Capture/002/"):
        for file in filenames :
            f.append("/home/pi/Desktop/KISSS_Capture/002/"+file)
        #f.extend(filenames)
        break
    return f


#images = ["DSC_001_7.jpg","DSC_002_3.jpg","DSC_002_4.jpg","DSC_002_6.jpg","DSC_002_19.jpg"]
print("Cropping")
treeshold = 55
images = getImages()

j=1
for i in images:
    print(str(j)+"/"+str(len(images))+"  picture : "+i)
    myimg = cv.imread(i)
    left_x = detect_left_x_mid(treeshold, myimg)
    right_x = detect_right_x_mid(treeshold, myimg)
    top_y = detect_top_y_mid(treeshold, myimg, left_x, right_x)
    bottom_y = detect_bottom_y_mid(treeshold, myimg, left_x, right_x)
    print(i.split("/")[6])
    cropper(i.split("/")[6], myimg, left_x, right_x,top_y, bottom_y)
    j+=1
