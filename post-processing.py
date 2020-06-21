#!/usr/bin/env python3

################################################ LIBRARIES ################################################
import cv2 as cv
import numpy as np
import os
from os import walk
import sys

################################################ VARIABLES ################################################
# Folder where folders and pictures will be created
baseFolder = "/home/pi/Desktop/KISSS_Capture/"

# Cropping
cropping = 1
treeshold = 55

# Mirroring
mirroring = 1
HorizOrVert = "H"  # can be H or V 

# Rotating
rotating = 1
degrees = 90

# Polishing
polishing = 0

# Push to nextcloud
clouding = 1

j = 0

################################################ FUNCTIONS ################################################

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
                break
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
    return left
def detect_right_x_mid(treeshold, myimg):
    right = 0
    h,w,c = myimg.shape
    mid_h = int(h/2)
    for i in range(w-1, -1, -1):
        color = myimg[(mid_h,i)]
        avg = np.mean(myimg[(mid_h,i)])
        if avg >= treeshold :
            if right == 0 :
                right = i
                break
            if i >= right :
                right = i
                break
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
            break
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
            break

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
    return bottom

def cropper(img_source, dst_folder, img, lx, rx, ty, by):
    # TODO : factorise here pls
    crop_img=img[ty:by, lx:rx]

    if mirroring == 1:
        print("Flipping...")
        crop_img=cv.flip(crop_img, 1) # mirror

    if rotating == 1:
        print("Rotating...")
        crop_img=cv.rotate(crop_img, cv.ROTATE_180)

    if polishing == 1:
        print("Polishing...")
        # 1st method
        alow = crop_img.min()
        ahigh = crop_img.max()
        amax = 255
        amin = 0

        # calculate alpha, beta
        alpha = ((amax - amin) / (ahigh - alow))
        beta = amin - alow * alpha
        # perform the operation g(x,y)= α * f(x,y)+ β
        crop_img = cv.convertScaleAbs(crop_img, alpha=alpha, beta=beta)

        
        # 2nd method
        # create new image with the same size and type as the original image
        #new_img = np.zeros(crop_img.shape, crop_img.dtype)

        # calculate stats
        #alow = crop_img.min()
        #ahigh = crop_img.max()
        #amax = 255
        #amin = 0

        # access each pixel, and auto adjust
        #for x in range(crop_img.shape[1]):
            #for y in range(crop_img.shape[0]):
                #a = crop_img[x, y]
                #new_img[x, y] = amin + (a - alow) * ((amax - amin) / (ahigh - alow))
    
        #crop_img = new_img
        

    # Write final image 
    cv.imwrite(dst_folder+'/'+img_source,crop_img)

    # Push to nexcloud
    if clouding == 1:
        print("Clouding...")
        if j == 1: # first image let's create folder
            os.system("./cloudmanager.sh mkdir Photos/DIAPOS/"+boxnbr)
            
        os.system("./cloudmanager.sh send "+dst_folder+"/"+img_source+" Photos/DIAPOS/"+boxnbr+"/")

def getImages():
    f = []
    for (dirpath, dirnames, filenames) in walk(sourceFolder):
        for file in sorted(filenames) :
            f.append(sourceFolder+"/"+file)
        break
    return f


################################################ MAIN ################################################
if __name__ == '__main__':     # Program start from here

      # Argument
      if len(sys.argv) != 2:
            print("Missing box number parameter")
            quit()

      boxnbr = str(sys.argv[1])

      sourceFolder = baseFolder+'/'+boxnbr+'/'
      destFolder = baseFolder+'/'+boxnbr+'/processed/'

      # Check if folders already exists
      if not os.path.exists(sourceFolder):
            print(sourceFolder+" doesn't exists !")
            quit()
      else:
            if not os.path.exists(destFolder):
                os.makedirs(destFolder)
            else:
                print(destFolder+" already exists !")
                quit()

      # cropping
      treeshold = 55
      images = getImages()

      j=1
      for i in images:
          print(str(j)+"/"+str(len(images))+"  picture : "+i)
          print("Cropping...")
          myimg = cv.imread(i)
          left_x = detect_left_x_mid(treeshold, myimg)
          right_x = detect_right_x_mid(treeshold, myimg)
          top_y = detect_top_y_mid(treeshold, myimg, left_x, right_x)
          bottom_y = detect_bottom_y_mid(treeshold, myimg, left_x, right_x)
          cropper(i.split("/")[-1], destFolder, myimg, left_x, right_x,top_y, bottom_y)
          j+=1
