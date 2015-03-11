#!/usr/bin/python2.7

#setup
from SimpleCV import *
import time

cam = Camera()
display = Display()


#time.sleep(5)
img = cam.getImage()
img.save(display)

logo = Image('logo')

time.sleep(5)

logo.show()
time.sleep(5)

while display.isNotDone():
        img = cam.getImage()
        if display.mouseLeft:
                break
        img.show()

