#!/usr/bin/python2.7

#setup
from SimpleCV import *
import time

cam = Camera()
display = Display((600,800))

print cam.getAllProperties()


#time.sleep(5)
img = cam.getImage()
img.save(display)

#logo = Image('logo')

time.sleep(5)
img = cam.getImage()
img.save(display)

#logo.show()
#time.sleep(5)

#x.show  will resize the window

while display.isNotDone():

		#get  the image
        print "in the loop"
        img = cam.getImage()
		
        #Add a box to the pic
        facelayer = DrawingLayer((img.width, img.height))
        facebox_dim = (50,50)
        center_point = (img.width / 2, img.height / 2)
        facebox = facelayer.centeredRectangle(center_point, facebox_dim)
        img.addDrawingLayer(facelayer)
        img.applyLayers()

		
        if display.mouseLeft:
                break
        #img.show()
        img.scale(800, 600)
        
        img.show()
        print "saved"


