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

      #while True:
      for x in range(1, 49):
            
            #print 'relay off...'
            GPIO.output(RelayPin, GPIO.HIGH)
            time.sleep(2)

            print("Slide #%d" % (x))
            GPIO.output(RelayPin, GPIO.LOW)
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
