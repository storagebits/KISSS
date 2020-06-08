#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os

RelayPin = 17    # pin17
 

def setup():

      GPIO.setmode(GPIO.BCM)     
      GPIO.setup(RelayPin, GPIO.OUT)
      GPIO.output(RelayPin, GPIO.HIGH)

def loop():
      
      raw_input("Calibrate your camera and press Enter when you're ready to start the scanner...")
      #print("Slide #1")
      #os.system('gphoto2 --capture-image-and-download --filename=/home/pi/Desktop/KISSS_Capture/000/DSC_001_1.jpg')

      for x in range(1, 51):
            
            #print 'Set relay off...'
            GPIO.output(RelayPin, GPIO.HIGH)
            #print("relay off 2sec")
            time.sleep(2)

            # take picture here
            print("Slide #%d" % (x))
            filename = 'DSC_001_%d.jpg'%(x,)
            os.system('gphoto2 --capture-image-and-download --filename=/home/pi/Desktop/KISSS_Capture/001/'+filename)

            GPIO.output(RelayPin, GPIO.LOW)
            #print("relay on , 1sec")
            time.sleep(1)

def destroy():

      GPIO.output(RelayPin, GPIO.HIGH)
      GPIO.cleanup()                    

if __name__ == '__main__':     # Program start from here

      os.system("cowsay \"KISSS - Keep It Simple Slide Scanner\"")
      setup()
      try:
            loop()
      except KeyboardInterrupt:  # Arret 'Ctrl+C'
            destroy()

      destroy()
