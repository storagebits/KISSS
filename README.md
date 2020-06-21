# K.I.S.S.S. - Keep It Simple Slide Scanner

## About this project
K.I.S.S.S. Keep It Simple Slide Scanner is an other DIY slide scanner project. Here you'll find informations about how I went into this scanning project. It is provided "as is". For sure you'll need to adapt it to match your own installation.

It uses a simple projector lens trick which allows a DSLR to capture a slide by photographing it directly from the projector instead from the projected picture. 

![KISSS - Keep It Simple Slide Scanner](https://github.com/storagebits/KISSS/blob/master/images/final.jpg?raw=true)

My dad was doing a lot (LOT) of photographies, exclusively on slides. From the early 1960's up to the early 1990. Since 30 years, for many reasons, those slides and their memories are sleeping in the attic...  

![KISSS - Keep It Simple Slide Scanner](https://github.com/storagebits/KISSS/blob/master/images/slidestock.jpg?raw=true)

## AUTOMATION NEEDED

My goal was to capture those 10'000 slides. First to keep those memories in a safe place and then to have an easy way to watch them. 

## Hardware components
 - Slide projector with wired remote
 - DSLR photo camera with USB remote capabilities (see Gphoto2 below)
 - Raspberry Pi 
	 - I use model 4 but all of them should work. Keep in mind that if you do some post processing operations, the more cpu/ram it has, faster it'll run.
 - Relay module
 - Few Dupont wires
 - Tripod
 
## Software components
 - **Raspbian** (now called Raspberry Pi OS)
	 - Raspbian is a [Debian](https://en.wikipedia.org/wiki/Debian "Debian")-based [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") for [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi "Raspberry Pi"). [https://www.raspberrypi.org/downloads/raspberry-pi-os/]
- **Gphoto 2**
	- [**gPhoto2**](http://www.gphoto.org/proj/)  is a free, redistributable, ready to use set of digital camera software applications for Unix-like systems, written by a whole team of dedicated volunteers around the world. It supports more than  [2500 cameras](http://www.gphoto.org/proj/libgphoto2/support.php)
	- Check if your DSLR is supported here : [http://www.gphoto.org/proj/libgphoto2/support.php](http://www.gphoto.org/proj/libgphoto2/support.php)
	- I suggest this automated installer for installation : https://github.com/gonzalo/gphoto2-updater/  . This script allows to install last development and last stable releases of gphoto2 and libgphoto2 based on git repositories
- **Python**
	- Python was the best choice for many reasons. 
- **OpenCV library**
- **Nextcloud**

## Circuit

## How it works

 1. Capture
 2. Post processing

## Samples



Happy scanning ! and have fun digging into your memories ...
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ5MDk5MTQ3NiwtMjU3Mzg0MDc4LC05NT
YwMjQ0MjAsLTUwMjI4NTc4LC05NTk4OTUzMzEsLTEzNzIzMjky
MTgsMjA0Mjg3MTI0LDIxNjI2ODUyMiwtMTQ0MDk1ODc4MCwtND
AwNDA3OTgyLDEwNjUwNzg5OTVdfQ==
-->