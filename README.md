# K.I.S.S.S. - Keep It Simple Slide Scanner

# About this project
K.I.S.S.S. Keep It Simple Slide Scanner is an other DIY slide scanner project. Here you'll find informations about how I went into this scanning project. It is provided "as is". For sure you'll need to adapt it to match your own installation.

It uses a simple projector lens trick by adding a white midsole between  lenses which will illuminate the slides. It then allows a DSLR to capture a slide by photographing it directly from the projector instead from the projected picture. 

![KISSS - Keep It Simple Slide Scanner](https://github.com/storagebits/KISSS/blob/master/images/final.jpg?raw=true)

It uses a Raspberry Pi which control the slide projector via a simple relay module and a DSLR camera to capture the slides. Then it does some post processing operations and send it straight to the cloud ! oh yeah

My dad was doing a lot (LOT) of photographies, exclusively on slides. From the early 1960's up to the 1990's. During this time he did more than 10'000 photos. Not a bad score at a time where you had to go to corner shop to develop them!  Since 30 years, for many reasons, those slides and their memories are sleeping in a attic...  

![KISSS - Keep It Simple Slide Scanner](https://github.com/storagebits/KISSS/blob/master/images/slidestock.jpg?raw=true)

Now you understand why I needed some automations to accomplish this task :-)
   
My goal was to capture those 10'000 slides. First to keep all those memories in a safe place and also to have an easy and confortable way to watch them. Resulting scan quality is beyond my expectations. Far more than acceptable for display, maybe not enough for print. It depends of many factors. With this DIY scanner It takes about 3 minutes to scan a 50 slides's rack. With some optimizations (like working exclusively in RAM) it could even take a single minute. 

# Hardware components
 - **Slide projector with wired remote**
	 - Wired remote from those times are easily "hackable". They're just made of electrical contacts. I kept the original 6 DIN connector which go to the projector and plugged the other side to a relay instead of the remote.
	
<center><a href="https://github.com/storagebits/KISSS/blob/master/images/remote1.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/remote1.jpg?raw=true" align="left" width="200" ></a>

<a href="https://github.com/storagebits/KISSS/blob/master/images/remote2.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/remote2.jpg?raw=true" align="left" width="200" ></a>
 </center>
 <br><br><br><br><br><br><br><br><br><br><br><br><br><br>

 
 - **DSLR photo camera with USB remote capabilities** (see Gphoto2 below)
	 - I use a Canon 700d with a 70-300mm TAMARON lens in macro mode. I put every settings in manual mode except ISO. 
	 <p><a href="https://github.com/storagebits/KISSS/blob/master/images/canon700d.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/canon700d.jpg?raw=true" align="left" width="200" ></a>
<a href="https://github.com/storagebits/KISSS/blob/master/images/tamron.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/tamron.jpg?raw=true" align="left" width="200" ></a>
 </p>
 <br><br><br><br><br><br><br><br><br>
	 
 - **Raspberry Pi** 
	 - I use a Raspberry 4 but all of them should work. Keep in mind that if you do some post processing operations, the more cpu/ram it has, faster it'll run !
	 <p><a href="https://github.com/storagebits/KISSS/blob/master/images/raspberry4.jpg.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/raspberry4.jpg?raw=true" align="left" width="200" ></a>
 </p>
 <br><br><br><br><br><br><br><br><br>

 - **Relay module**
	 - A simple relay module which is used to control the slide projector from the Raspberry Pi's GPIO.
	 <p><a href="https://github.com/storagebits/KISSS/blob/master/images/relay-module.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/relay-module.jpg?raw=true" align="left" width="200" ></a>
 </p>
 <br><br><br><br><br><br><br><br><br>
 
 - **Few Dupont wires**
	 - Classics female to female Dupont wires to plug the Raspberry Pi GPIOs to the relay module.
	 <p><a href="https://github.com/storagebits/KISSS/blob/master/images/dupont-female.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/dupont-female.jpg?raw=true" align="left" width="200" ></a>
 </p>
 <br><br><br><br><br><br><br><br><br>

 - **A tripod**
	 - Optional but very useful depending on your setup. 
 	 <p><a href="https://github.com/storagebits/KISSS/blob/master/images/tripod.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/tripod.jpg?raw=true" align="left" width="200" ></a> 
 </p>
 <br><br><br><br><br><br><br><br><br>
 
# Software components
 - **Raspbian** (now called Raspberry Pi OS)
	 - Raspbian is a [Debian](https://en.wikipedia.org/wiki/Debian "Debian")-based [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") for [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi "Raspberry Pi"). [https://www.raspberrypi.org/downloads/raspberry-pi-os/]

- **Python**
	- Python was the best choice for many reasons... Ease of use, tons of libraries to manage the Rasp , the post processing stuffs and the cloud interaction.

- **Gphoto 2**
	- [**gPhoto2**](http://www.gphoto.org/proj/)  is a free, redistributable, ready to use set of digital camera software applications for Unix-like systems, written by a whole team of dedicated volunteers around the world. It supports more than  [2500 cameras](http://www.gphoto.org/proj/libgphoto2/support.php)
	- Check if your DSLR is supported here : [http://www.gphoto.org/proj/libgphoto2/support.php](http://www.gphoto.org/proj/libgphoto2/support.php)
	- I suggest this automated installer to have the lastest bits of this wonderful software : https://github.com/gonzalo/gphoto2-updater/  . This script allows to install last development and last stable releases of gphoto2 and libgphoto2 based on git repositories

- **OpenCV library**
	- OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. I use it in the post processing stage for multiple purposes : intelligent cropping (thx mec!) , mirroring , rotating, "final polish" , etc...

- **Nextcloud**
	- Nextcloud offers the industry-leading, on-premises content collaboration platform. Since I use this software since many years to store all my files and especially pictures, it was a natural choice to use it at final stage to push all my scans into it. I love the way I can browse my content, from my computer , my phone , my TV using Kodi through the webdav access , or whatever ... it has it all !

# Circuit
<a href="https://github.com/storagebits/KISSS/blob/master/images/KISSS-schema.png?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/KISSS-schema.png?raw=true">



# Getting started
K.I.S.S.S. is just made of 2 main scripts. The "capture script" called **KISSS.py** and the post processing script called post-processing.py

 **1. Setup your hardware**
		Install all your hardware on a table and wire everything. 
		Put the projector ON with a sample slide.
		VERY IMPORTANT STEP : calibrate your camera with the sample slide. Be sure 
 **2. Setup the KISSS.py script**
		 There are 2 variables to edit at the begining of the script :
		 *baseFolder* : Base folder where folders and pictures will be created
		 *relayPin* : Raspberry GPIO pin where you plugged the relay which manage projector remote
 **4. Capture**
		 You're now ready for the capture. Just launch KISSS.py 
 5. Post processing
	Cropping TODO
	Mirroring TODO
	Rotating TODO
	Polishing TODO
 6. Enjoy your memories in the cloud
	TODO

# Samples
Here are some samples of my scans. More to come ...

<a href="https://github.com/storagebits/KISSS/blob/master/images/exemple-italy-old.jpg?raw=true" target="_blank"><img src="https://github.com/storagebits/KISSS/blob/master/images/exemple-italy-old.jpg?raw=true" align="left" width="200" ></a>
<a href="https://github.com/storagebits/KISSS/blob/master/images/exemple-lille.jpg?raw=true"><img src="https://github.com/storagebits/KISSS/blob/master/images/exemple-lille.jpg?raw=true" align="left" width="200" ></a>
<a href="https://github.com/storagebits/KISSS/blob/master/images/exemple-calais.jpg?raw=true"><img src="https://github.com/storagebits/KISSS/blob/master/images/exemple-calais.jpg?raw=true" align="left" width="200" ></a>

<br><br><br><br><br><br><br><br><br><br>

#  Happy scanning ! and have fun digging into your memories !
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYyMjcxNzMwNyw5MTkyNTExMSwtMTYxOT
I1MDk5MCwyMDU0OTE0NzU3LDI2NjYxNTU4Myw1Njc0NDM3OTMs
LTcwNTUwMDUwNSwtMTEyMzY5NzExMywtODM1NzMwODU0LDE4ND
Q4Mzk5OTYsMzg5Mzg4Mjc2LDIxMTUwMTUxNDgsLTEyMDA0NDMz
NDcsLTE0Njc2NTY5NzEsMTg0MjMxODExOCwxMjU3MTExNzc1LD
EzNzgwOTE5MDMsLTIwMTgwMDM5NDMsMTk4MzM2NzEyNywtNjM4
MTk3Mzc2XX0=
-->