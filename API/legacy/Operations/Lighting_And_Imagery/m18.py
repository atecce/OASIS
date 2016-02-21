import urllib2,urllib
import Adafruit_BBIO.PWM as PWM
import sys

fo = open("test.txt", "wb");
fo.write("M18 (LED Brightness) Successful!!!");
print "Hello Welcome to Python Testing.. !!!"

print "Number of Arguments:",(len(sys.argv))
print "Arguments are:",(sys.argv)
for i in range(len(sys.argv)):
	print "Argument %d is: %s" % (i,sys.argv[i])

#print "Second Argument is:",(sys.argv[1])

PWM.start("P9_16",float(sys.argv[1]),1000,0) #to start PWM of selected duty cycle %, 1000Hz frequency


