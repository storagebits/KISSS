# K.I.S.S.S. - Keep It Simple Slide Scanner


![KISSS - Keep It Simple Slide Scanner](https://github.com/storagebits/KISSS/blob/master/images/intro.jpg?raw=true)

## About this project
K.I.S.S.S. Keep It Simple Slide Scanner is an other DIY slide scanner project. Here you'll find informations about 

It uses a simple projector lens trick which allows a DSLR to capture a slide by photographing it directly from the projector instead from the projected picture.

IMAGE PROJECTOR 

My dad was doing a lot (LOT) of photographies

IMAGE STOCK 

## Hardware components
 - Slide projector with wired remote
 - DSLR photo camera
 - Raspberry Pi 4
 - Relay module
 - Few Dupont wires
 - Tripod
 
## Software components
 - Raspbian (now called Raspberry Pi OS)
	 - Raspbian is a [Debian](https://en.wikipedia.org/wiki/Debian "Debian")-based [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") for [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi "Raspberry Pi"). [https://www.raspberrypi.org/downloads/raspberry-pi-os/]
- Gphoto 2
	- [**gPhoto2**](http://www.gphoto.org/proj/)  is a free, redistributable, ready to use set of digital camera software applications for Unix-like systems, written by a whole team of dedicated volunteers around the world. It supports more than  [2500 cameras](http://www.gphoto.org/proj/libgphoto2/support.php)
	- Check if your DSLR is supported here : [http://www.gphoto.org/proj/libgphoto2/support.php](http://www.gphoto.org/proj/libgphoto2/support.php)
	- I suggest this automated installer for installation : https://github.com/gonzalo/gphoto2-updater/  . This script allows to install last development and last stable releases of gphoto2 and libgphoto2 based on git repositories
- Python 3
- OpenCV2 python library

## Circuit

## How it works

## Samples


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
eyJoaXN0b3J5IjpbNTgxMjAxNTcsLTEzNzIzMjkyMTgsMjA0Mj
g3MTI0LDIxNjI2ODUyMiwtMTQ0MDk1ODc4MCwtNDAwNDA3OTgy
LDEwNjUwNzg5OTVdfQ==
-->