# need this to wait
import time

# need this for I2C's
import smbus

# need this for UART
import Adafruit_BBIO.UART as UART

class I2C_sensor: 

	# each I2C device has an address, register, and interface number
	address          = int()
	register	 = int()
	interface_number = int()

	def __init__(self, address, register, interface_number):

		# set address and register
		self.address  = address
		self.register = register

		# create bus with interface number
		self.bus = smbus.SMBus(interface_number) 

	def read(self):

		# actions punctuated by delays (is this necessary?)
		time.sleep(3)

		# write byte to the bus, (a request?)
		self.bus.write_byte(self.address, self.register) #R

		# actions punctuated by delays (is this necessary?)
		time.sleep(3)

		# read data into results(read response?)
		results = self.bus.read_i2c_block_data(self.address, self.register) #read cal info

		# actions punctuated by delays (is this necessary?)
		time.sleep(3)

		# what does enumerate do?
		for index, item in enumerate(results):

			# if first result?
			if item == 0:
				
				# is this a bit?
				end_val = index
				break

		# is this the end of a binary string?
		results = results[1:end_val]

		# beautiful list comprehension Sairam 
		# iterates through the string, converts them all to characters, and concatenates them in one line
		results_string = ''.join(chr(i) for i in results)

		# probably shouldn't be a list though
		return results_string

class ADC_sensor(I2C_sensor):

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

# may not be proper syntax, but it's python, set for proper indexing and creates a linked list

# tuple of liquid level sensors
LL = (None, liquid_level(0x22, 0x80, 2),	# LL1
	    liquid_level(0x22, 0xA0, 2),	# LL2
	    liquid_level(0x22, 0xC0, 2),	# LL3
	    liquid_level(0x22, 0xE0, 2),	# LL4
	    liquid_level(0x22, 0xD0, 2),	# LL5
	    liquid_level(0x22, 0xF0, 2))	# LL6

# dissolved oxygen probe
DO = I2C_sensor(0x61, 0x52, 2)			# DO

# pH probes
pH = (None, I2C_sensor(0x65, 0x52, 2),		# pH1
	    I2C_sensor(0x63, 0x52, 2))		# pH2

# electrical conductivity probes
EC = (None, I2C_sensor(0x66, 0x52, 2), 		# EC1
	    I2C_sensor(0x64, 0x52, 2))		# EC2

# total pressure sensors
#TP = (None, I2C_sensor(), 			# TP1
#	     I2C_sensor())			# TP2

# PAR sensors
PAR = (None, ADC_sensor(0x21, 0xF0, 2), 	# PAR1
	     ADC_sensor(0x21, 0xD0, 2))		# PAR2

# MO sensors
MO = (None, MO_sensor(0x21, 0x80, 2)		# MO1
	    MO_sensor(0x21, 0xA0, 2)		# MO2
	    MO_sensor(0x21, 0xC0, 2)		# MO3
	    MO_sensor(0x21, 0xE0, 2))		# MO4

# oxygen sensor
O2 = ADC_sensor(0x22, 0xB0, 2)
