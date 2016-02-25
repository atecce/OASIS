import subprocess
INPUTS = [60,117,113,13,12,76,77,74,75,72,73,50,48,49,111,112,110,116,7]

print len(INPUTS)
#print INPUTS
for i in range(len(INPUTS)):
		e1 = 'echo '+str(INPUTS[i])+' > /sys/class/gpio/export'
		print e1
		subprocess.call(e1, shell=True)
		e2 = 'echo in > /sys/class/gpio/gpio'+str(INPUTS[i])+'/direction'
		print e2
		subprocess.call(e2, shell=True)