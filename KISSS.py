#!/usr/bin/env python3

################################################ LIBRARIES ################################################
import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys
import signal
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd


################################################ VARIABLES ################################################
# Folder where folders and pictures will be created
baseFolder = "/home/pi/Desktop/KISSS_Capture/"

# Raspberry pin where you plugged the relay which manage projector remote
relayPin = 17    # pin17

# LCD configuration

lcd_rs = digitalio.DigitalInOut(board.D25)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d7 = digitalio.DigitalInOut(board.D22)
lcd_d6 = digitalio.DigitalInOut(board.D27)
lcd_d5 = digitalio.DigitalInOut(board.D5)
lcd_d4 = digitalio.DigitalInOut(board.D6)
lcd_backlight = digitalio.DigitalInOut(board.D13)

lcd_columns = 16
lcd_rows = 2

 
################################################ FUNCTIONS ################################################
def setup():

      GPIO.setmode(GPIO.BCM)     
      GPIO.setup(relayPin, GPIO.OUT)
      GPIO.output(relayPin, GPIO.HIGH)

def loop():

      lcd.clear()
      lcd.message = "Calibrate camera\nand press enter..."
      input("Calibrate your camera and press Enter when you're ready to start the scanner...")

      # Loop over a 50 sliders rack
      for x in range(1, 51):
            
            GPIO.output(relayPin, GPIO.HIGH)
            time.sleep(2)

            # take picture here
            print("Slide #%d" % (x))
            lcd.clear()
            lcd.message = "Slide XXX"

            filename = 'DSC_'+boxnbr+'_%03d.JPG'%(x,)
            print("destination : "+destFolder+'/'+filename)
            os.system('gphoto2 --capture-image-and-download --filename='+destFolder+'/'+filename)

            GPIO.output(relayPin, GPIO.LOW)
            time.sleep(1)

def destroy():

      GPIO.output(relayPin, GPIO.HIGH)
      GPIO.cleanup()                    

def mquit():

      print("Exiting ...")
      lcd.clear()
      lcd.message = "Exiting..."
      time.sleep(1)
      lcd.clear()
      quit()

# Kill the gphoto process that starts whenever we turn on the camera or reboot the raspberry pi
def killGphoto2Process():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # Search for the process we want to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # Kill that process!
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)

def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Wrong key...")


################################################ MAIN ################################################
if __name__ == '__main__':     # Program start from here

      lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
      lcd.message = "KISSS\nInitializing..."
      
      # Welcome
      print("______________________________________")
      print("< KISSS - Keep It Simple Slide Scanner >")
      print("--------------------------------------")
      print("\   ^__^")
      print("\  (oo)\_______")
      print("   (__)\       )\/\ ")
      print("       ||----w |")
      print("       ||     ||")
      print(" ")

      # Argument
      if len(sys.argv) != 2:
            print("Missing box number parameter")
            mquit()

      boxnbr = str(sys.argv[1])

      destFolder = baseFolder+'/'+boxnbr+'/'
      # Check if dest folrder already exists
      if not os.path.exists(destFolder):
            os.makedirs(destFolder)
      else:
            if not yes_or_no(destFolder+" already exists !!! PHOTOS MAY BE OVERWRITTEN !!!\r\nAre you sure you want to continue with this directory ? "):
                mquit()

      # kill gphoto instance to avoid "busy" locks 
      killGphoto2Process()

      # Setup GPIO
      setup()

      # Main loop
      try:
            loop()
      except KeyboardInterrupt:  # Arret 'Ctrl+C'
            destroy()

      destroy()
