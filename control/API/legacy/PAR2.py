#!/usr/bin/env python

import smbus
import time
bus = smbus.SMBus(2) # bus 2 is i2c bus on pins 17, 18
results = bus.read_i2c_block_data(0x21,0xD0) # 0xD0 for PAR2 sensor connected to VIN6 channel of ADC with I2C Address 0x21
#results = [108, 119, 103, 130, 104, 110, 108, 200, 104, 180, 103, 130, 105, 165, 108, 135, 106, 146, 107, 139, 108, 190, 104, 173, 107, 30, 104, 130, 105, 176, 105, 161]
print "ADC Results from PAR2 sensor:"
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

parValue = analogVal*1000*0.5

print "PAR 2 Value is "+str(parValue)+"micro-mol m^-2 s^-1"
