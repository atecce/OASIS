#!/usr/bin/env python

import smbus
import time
bus = smbus.SMBus(2) # bus 2 is i2c bus on pins 17, 18
results = bus.read_i2c_block_data(0x21,0xC0) # 0xC0 for MO3 sensor connected to VIN5 channel of ADC with I2C Address 0x21
#results = [108, 119, 103, 130, 104, 110, 108, 200, 104, 180, 103, 130, 105, 165, 108, 135, 106, 146, 107, 139, 108, 190, 104, 173, 107, 30, 104, 130, 105, 176, 105, 161]
print "ADC Results from MO3 sensor:"
print results
sensordata = []
for i in range(len(results)):
	#print "i value:"
	#print i
	if i%2 == 0:
		#print "inside if condition:"
		a = bin(results[i])
		if(len(a)>5):
			a = a[len(a)-4:] # To get last 4 characters in the binary string
		#print a

		b = bin(results[i+1])[2:]
		#print b

		len(b)

		if(len(b)<8):
			for j in range(len(b), 8):
				b='0'+b;

		c = a + b

		#print int(c,2)
		sensordata.append(int(c,2))

print "\r\nLength of SensorData:"
print len(sensordata)
print "SensorData:"+str(sensordata)
sensordata.sort()
print "Sorted SensorData:"+str(sensordata)

sensorVal = (sensordata[7] +  sensordata[8])/(2.0)
print "Chosen Sensor ADC Value:"+ str(sensorVal)
analogVal = (sensorVal/4095.0)*3.3
print "Chosen Sensor Analog Value in V:"+str(analogVal)

VWC=0 #VWC(Volumetric Water Content) = 0
if (analogVal>=0 and analogVal<1.1):
	VWC=10*analogVal-1
if (analogVal>=1.1 and analogVal<1.3):
	VWC=25*analogVal-17.5
if (analogVal>=1.3 and analogVal<=1.82):
	VWC=48.08*analogVal-47.5
if (analogVal>=1.8 and analogVal<=2.2):
	VWC=26.32*analogVal-7.89

print "Volumetric Water Content is "+str(VWC)+"%"
