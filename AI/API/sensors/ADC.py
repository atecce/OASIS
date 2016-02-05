# need this to wait
import time

# need this for I2C's
import smbus

# need this for camera
import cv2

# need this for UART
import Adafruit_BBIO.UART as UART

# need this for temperature
import Adafruit_DHT

# need this to read serial buffer
import serial

# what is this?
import struct 

class ADC_sensor:

	# each ADC device has an address, register, and interface number
	address    	 = int()
	register	 = int()
	interface_number = int()

	def __init__(self, address, register, interface_number):

		# set address and registers
		self.address  = address
		self.register = register

		# bus 2 is I2C bus on pins P9.17, P9.18
		self.bus = smbus.SMBus(interface_number) 

	def read(self):

		# 0x80 for LL1    sensor connected to VIN1 channel of ADC with I2C Address 0x22
		# 0xA0 for LL2    sensor connected to VIN3 channel of ADC with I2C Address 0x22
		# 0xC0 for LL3    sensor connected to VIN5 channel of ADC with I2C Address 0x22
		# 0xE0 for LL4    sensor connected to VIN7 channel of ADC with I2C Address 0x22
		# 0xF0 for LL5    sensor connected to VIN8 channel of ADC with I2C Address 0x22
		# 0xD0 for LL6    sensor connected to VIN6 channel of ADC with I2C Address 0x22
		# 0x80 for MO1    sensor connected to VIN1 channel of ADC with I2C Address 0x21
		# 0xA0 for MO2    sensor connected to VIN3 channel of ADC with I2C Address 0x21
		# 0xC0 for MO3    sensor connected to VIN5 channel of ADC with I2C Address 0x21
		# 0xE0 for MO4    sensor connected to VIN7 channel of ADC with I2C Address 0x21
		# 0xB0 for O2 OX1 sensor connected to VIN4 channel of ADC with I2C Address 0x22
		# 0xF0 for PAR1   sensor connected to VIN8 channel of ADC with I2C Address 0x21
		# 0xD0 for PAR2   sensor connected to VIN6 channel of ADC with I2C Address 0x21
		results = self.bus.read_i2c_block_data(self.address, self.register) 
	
		# initialize list of data
		sensordata = []

		# for each result
		for i in range(len(results)):

			# check only even numbers
			if i % 2 == 0:

				# convert result to binary string
				a = bin(results[i])

				# to get last 4 characters in the binary string
				if(len(a) > 5): a = a[len(a)-4:] 

				# (what is this binary string?)
				b = bin(results[i+1])[2:]

				# (and how is it split up?)
				if(len(b) < 8):

					# add prefix 0b?
					for j in range(len(b), 8): b = '0' + b

				# concatenation? or addition?
				c = a + b

				# append integer conversion to sensor data
				sensordata.append(int(c, 2))

		# sort the sensor data
		sensordata.sort()

		# get median
		sensorVal = (sensordata[7] + sensordata[8])/(2.0)

		# (4095 = 2**10 - 1), why not 4096?
		analogVal = (sensorVal/4095.0) * 3.3

		# difference between this and analogVal?
		actualAnalogVal = (3.3 - analogVal) / 2 + 1
		
class liquid_level(ADC_sensor):

	# doesn't seem to be much different than parent class? why did Sairam only want to calculate resistance on liquid level?
	def read(self):

		# resolution?
		RES = 2400

		# given? true for all? or just liquid level?
		supply_voltage = 5

		# current?
		I = (supply_voltage - actualAnalogVal) / RES

		# Ohm's Law
		resistance = actualAnalogVal / I

		# why are we returning resistance?
		return resistance

class MO_sensor(ADC_sensor):

	def read(self):

		# initialize volumetric water content to zero
		VWC = 0 

		# why these ranges? and why these equations?
		if   (analogVal <  1.1 and analogVal >= 0):    VWC =    10*analogVal - 1
		elif (analogVal >= 1.1 and analogVal <  1.3):  VWC =    25*analogVal - 17.5
		elif (analogVal >= 1.3 and analogVal <= 1.82): VWC = 48.08*analogVal - 47.5

		# return volumetric water content to zero
		return VWC

class O2_sensor(ADC_sensor):

	def read(self):

		# what determines this constant?
		gainVal = 40*5.86

		# convert to mV
		analogValmV = 1000*(analogVal/gainVal)

		# analog value in mV 
		return analogValmV

class PAR_sensor(ADC_sensor):

	def read(self):

		# straight line? why that constant?
		parValue = 1000*0.5*analogVal

		# probably shouldn't be returned as a string
		return str(parValue)
