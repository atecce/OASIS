import subprocess
#OUTPUTS = [9,115,45,44,26,46,87,89,10,11,62,63,23,65,27,37,33,61,86,32,36,47,81,8,80,70,71,51]
OUTPUTS = {9:1,115:0,45:1,44:1,26:1,46:1,87:1,89:1,10:1,11:1,62:0,63:0,23:0,65:0,27:0,37:0,33:0,61:0,86:0,32:0,36:0,47:0,81:0,8:0,80:0,70:0,71:0,51:0}

print len(OUTPUTS)
#print OUTPUTS.keys()[0]
#print OUTPUTS.keys(0) 
#print OUTPUTS.keys(1)
#e = 'echo '+sys.argv[2]+' > /sys/class/gpio/gpio'+sys.argv[1]+'/value'

#For changing P9_19 to GPIO
""""e = 'echo bspm_P9_19_17 > /sys/devices/bone_capemgr.9/slots'
subprocess.call(e, shell=True)

#For changing P9_20 to GPIO
e = 'echo bspm_P9_20_17 > /sys/devices/bone_capemgr.9/slots'
subprocess.call(e, shell=True)"""

#For changing P9_21 to I2C SCL
e = 'echo bspm_P9_21_32 > /sys/devices/bone_capemgr.9/slots'
subprocess.call(e, shell=True)

#For changing P9_22 to I2C SDA
e = 'echo bspm_P9_22_32 > /sys/devices/bone_capemgr.9/slots'
subprocess.call(e, shell=True)



e = 'echo bspm_P8_20_17 > /sys/devices/bone_capemgr.9/slots'
subprocess.call(e, shell=True)
e = 'echo bspm_P8_21_17 > /sys/devices/bone_capemgr.9/slots'
subprocess.call(e, shell=True)
e = 'echo bspm_P8_24_17 > /sys/devices/bone_capemgr.9/slots'
subprocess.call(e, shell=True)
e = 'echo bspm_P8_25_17 > /sys/devices/bone_capemgr.9/slots'
subprocess.call(e, shell=True)
for i in range(len(OUTPUTS)):
		e1 = 'echo '+str(OUTPUTS.keys()[i])+' > /sys/class/gpio/export'
		print e1
		subprocess.call(e1, shell=True)
		e2 = 'echo out > /sys/class/gpio/gpio'+str(OUTPUTS.keys()[i])+'/direction'
		print e2
		subprocess.call(e2, shell=True)
		e3 = 'echo '+str(OUTPUTS[OUTPUTS.keys()[i]])+' > /sys/class/gpio/gpio'+str(OUTPUTS.keys()[i])+'/value'
		subprocess.call(e3, shell=True)
		print e3		
		e4 = 'chmod 664 /sys/class/gpio/gpio'+str(OUTPUTS.keys()[i])+'/value'
		subprocess.call(e4, shell=True)
		print e4
#print OUTPUTS
#subprocess.call(e, shell=True)