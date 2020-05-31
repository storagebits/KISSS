#!/usr/bin/python3

import gphoto2 as gp

camera = gp.check_result(gp.gp_camera_new())
gp.check_result(gp.gp_camera_init(camera))
text = gp.check_result(gp.gp_camera_get_summary(camera))
print('Summary')
print('=======')
print(text.text)
gp.check_result(gp.gp_camera_exit(camera))


#import gphoto2 as gp

#camera = gp.Camera()
#camera.init()
#text = camera.get_summary()
#print('Summary')
#print('=======')
#print(str(text))
#camera.exit()

