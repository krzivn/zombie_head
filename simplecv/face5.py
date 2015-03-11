#!/usr/bin/python2.7
print "Starting"

#setup
from SimpleCV import *
import time
display = Display()
cam = Camera()


print "loading haar"
haarcascade = SimpleCV.HaarCascade('face.xml') 
print "load attempted"

img = cam.getImage()
img.listHaarFeatures()

print cam.getAllProperties()


img.show()
time.sleep(5)

print "face detection start"
faces = img.findHaarFeatures(haarcascade)
print "face detection done"

print "I found a face at " + str(faces.coordinates())

img.show()
time.sleep(5)
    
while display.isNotDone():

		#get  the image
        img = cam.getImage()
        print "face detection start"
        faces = img.findHaarFeatures(haarcascade)
        print "face detection done"
        #Find a face
        if faces:
            #face = faces.sortArea()
            #face.draw(SimpleCV.Color.RED, 1)
            print "I found a face at " + str(faces.coordinates())
        
        #Show the image
        img.show()
        


