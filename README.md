# K.I.S.S.S. - Keep It Simple Slide Scanner


![KISSS - Keep It Simple Slide Scanner](https://github.com/storagebits/KISSS/blob/master/images/intro.jpg?raw=true)

## About this project
K.I.S.S.S. Keep It Simple Slide Scanner is an other DIY slide scanner project. 
 

## Hardware components

 - Slide projector with wired remote
 - DSLR photo camera
 - Raspberry Pi
 - Relay module
 - Small electrical wires dupont style
 - Tripod
 
## Software components
 - Raspbian (now called Raspberry Pi OS)
	 - [https://www.raspberrypi.org/downloads/raspberry-pi-os/](https://www.raspberrypi.org/downloads/raspberry-pi-os/
- Gphoto2


## Alpha

## 
gphoto2 Install 

https://github.com/gonzalo/gphoto2-updater/
This script allows to install last development and last stable releases of gphoto2 and libgphoto2 based on git repositories

wget https://raw.githubusercontent.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh && chmod +x gphoto2-updater.sh && sudo ./gphoto2-updater.sh


Post processing Test

pi@raspberrypi:/Desktop/KISSS_Capture/001 $ time mogrify -flop *.jpg
real	4m39,927s
user	2m10,517s
sys	1m6,904s
pi@raspberrypi:/Desktop/KISSS_Capture/001 $ time mogrify -rotate 180 *.jpg
real	4m30,877s
user	2m13,308s
sys	1m8,788s
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU1MzM5MjgyMiwyMTYyNjg1MjIsLTE0ND
A5NTg3ODAsLTQwMDQwNzk4MiwxMDY1MDc4OTk1XX0=
-->