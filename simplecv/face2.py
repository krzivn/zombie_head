#!/usr/bin/python2.7

from SimpleCV import *
import time

cam = Camera()
display = Display()
img = cam.getImage()
img.save(display)

time.sleep(15)

