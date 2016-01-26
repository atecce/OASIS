import urllib2,urllib
import subprocess
import sys

fo = open("test.txt", "wb");
fo.write("P12/Dehumidifier Successful!!!");
print "Hello Welcome to Python Testing.. !!!"

print "Number of Arguments:",(len(sys.argv))
print "Arguments are:",(sys.argv)
for i in range(len(sys.argv)):
	print "Argument %d is: %s" % (i,sys.argv[i])

#print "Second Argument is:",(sys.argv[1])
#print "Third Argument is:",(sys.argv[2])

e = 'echo '+sys.argv[1]+' > /sys/class/gpio/gpio87/value'
print e
subprocess.call(e, shell=True)