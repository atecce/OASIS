import urllib2,urllib
import subprocess
import sys
import cv2

fo = open("test.txt", "wb");
fo.write("Camera Successful!!!");
print "Hello Welcome to Python Testing.. !!!"

print "Number of Arguments:",(len(sys.argv))
print "Arguments are:",(sys.argv)
for i in range(len(sys.argv)):
	print "Argument %d is: %s" % (i,sys.argv[i])

print "Second Argument is:",(sys.argv[1])


cam=cv2.VideoCapture(0)
ret, frame=cam.read()
cv2.imwrite("IMG_"+str(sys.argv[1])+".jpg",frame)
cam.release()
cv2.destroyAllWindows()
