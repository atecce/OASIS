import subprocess
import sys
print "Number of Arguments:",(len(sys.argv))
print "Arguments are:",(sys.argv)
for i in range(len(sys.argv)):
	print "Argument %d is: %s" % (i,sys.argv[i])

#print "Second Argument is:",(sys.argv[1])
#print "Third Argument is:",(sys.argv[2])

e = 'echo '+sys.argv[2]+' > /sys/class/gpio/gpio'+sys.argv[1]+'/value'
print e
subprocess.call(e, shell=True)