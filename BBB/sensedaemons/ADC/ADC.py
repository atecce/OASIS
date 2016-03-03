# need this to wait
import time

# need this for I2C's
import smbus

# need this for total pressure sensors
import Adafruit_BMP.BMP085 as BMP085

# need this for parent class
from I2C import I2C_sensor

class ADC_sensor(I2C_sensor):

	# all ADC sensors have an interface number of 2
	interface_number = 2

	def __init__(self, address, register):

		# create bus with interface number
		self.bus = smbus.SMBus(self.interface_number) 

		# set address and register
		self.address  = address
		self.register = register

	def voltage(self):

		# 0x80 for MO1    sensor connected to VIN1 channel of ADC with I2C Address 0x21
		# 0xA0 for MO2    sensor connected to VIN3 channel of ADC with I2C Address 0x21
		# 0xC0 for MO3    sensor connected to VIN5 channel of ADC with I2C Address 0x21
		# 0xE0 for MO4    sensor connected to VIN7 channel of ADC with I2C Address 0x21
		# 0xB0 for O2 OX1 sensor connected to VIN4 channel of ADC with I2C Address 0x22
		# 0xF0 for PAR1   sensor connected to VIN8 channel of ADC with I2C Address 0x21
		# 0xD0 for PAR2   sensor connected to VIN6 channel of ADC with I2C Address 0x21
		# 0x80 for LL1    sensor connected to VIN1 channel of ADC with I2C Address 0x22
		# 0xA0 for LL2    sensor connected to VIN3 channel of ADC with I2C Address 0x22
		# 0xC0 for LL3    sensor connected to VIN5 channel of ADC with I2C Address 0x22
		# 0xE0 for LL4    sensor connected to VIN7 channel of ADC with I2C Address 0x22
		# 0xF0 for LL5    sensor connected to VIN8 channel of ADC with I2C Address 0x22
		# 0xD0 for LL6    sensor connected to VIN6 channel of ADC with I2C Address 0x22
		results = self.bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(5)
	
		# initialize list of data
		sensordata = list()

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

		return sensorVal, analogVal, actualAnalogVal
		
class liquid_level(ADC_sensor):

	# all liquid level sensors have an address 0x22
	address = 0x22

	def __init__(self, register):

		# create bus with interface number
		self.bus = smbus.SMBus(self.interface_number) 
		
		# set register value
		self.register = register

	# doesn't seem to be much different than parent class? why did Sairam only want to calculate resistance on liquid level?
	def read(self):

		# get raw data from parent class
		sensorVal, analogVal, actualAnalogVal = self.voltage()

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

class moisture(ADC_sensor):

	# all liquid level sensors have an address 0x21
	address = 0x21

	# each I2C device has an address, register, and interface number
	def __init__(self, register):

		# create bus with interface number
		self.bus = smbus.SMBus(self.interface_number) 

		# set register
		self.register = register

	def read(self):

		# get raw data from parent class
		sensorVal, analogVal, actualAnalogVal = self.voltage()

		# initialize volumetric water content to zero
		VWC = 0 

		# why these ranges? and why these equations?
		if   (analogVal <  1.1 and analogVal >= 0):    VWC =    10*analogVal - 1
		elif (analogVal >= 1.1 and analogVal <  1.3):  VWC =    25*analogVal - 17.5
		elif (analogVal >= 1.3 and analogVal <= 1.82): VWC = 48.08*analogVal - 47.5

		# return volumetric water content to zero
		return VWC

class oxygen(ADC_sensor):

	# address and register of O2 sensor are set
	address	 = 0x22
	register = 0xB0

	def __init__(self):

		# set bus with interface number
		self.bus = smbus.SMBus(self.interface_number) 

	def read(self):

		# get raw data from parent class
		sensorVal, analogVal, actualAnalogVal = self.voltage()

		# what determines this constant?
		gainVal = 40*5.86

		# convert to mV
		analogValmV = 1000*(analogVal/gainVal)

		# considering slope of linear line in the graph related to low range of sensor operation
		slope = (9.0-0.0)/(20.0-0.0)

		# y = mx => x = y/m
		O2Percent = (analogValmV)/slope

		# return to O2 percentage
		return O2Percent

class photosynthetically_active_radiation(ADC_sensor):

	# address of PAR sensor is set
	address = 0x21

	def __init__(self, register):

		# set bus with interface number
		self.bus = smbus.SMBus(self.interface_number) 

		# set and register
		self.register = register

	def read(self):

		# get raw data from parent class
		sensorVal, analogVal, actualAnalogVal = self.voltage()

		# straight line? why that constant?
		parValue = 1000*0.5*analogVal

		return parValue


