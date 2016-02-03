#!/usr/bin/env python

import smbus
import time
bus = smbus.SMBus(2) # bus 2 is i2c bus on pins 17, 18
results = bus.read_i2c_block_data(0x22,0x80) # 0x80 for LL1 sensor connected to VIN1 channel of ADC with I2C Address 0x22
#results = [108, 119, 103, 130, 104, 110, 108, 200, 104, 180, 103, 130, 105, 165, 108, 135, 106, 146, 107, 139, 108, 190, 104, 173, 107, 30, 104, 130, 105, 176, 105, 161]
print "ADC Results from LL sensor on LL1 channel:"
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

actualAnalogVal = (3.3 - analogVal)/(2) + 1;

RES=2400;
supply_voltage=5;
I=(supply_voltage-actualAnalogVal)/RES;
resistance=actualAnalogVal/I;
#resistance=1500-resistance;
print "resistance is "
print resistance
water_level = (2100 - resistance)/(150);
#water_level=-(resistance-1500)/140;
#water_level=resistance/140;	

#water_level=8-water_level;
print "Water Level in inches is:" + str(water_level);
#inches	res
#0 - 2100
#4 - 1500
#8 - 900

