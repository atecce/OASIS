# need this to wait
import time

# need this for I2C's
import smbus

# need this for total pressure sensors
import Adafruit_BMP.BMP085 as BMP085

class I2C_sensor: 

	# default interface number and address for I2C sensors
	interface_number = 2
	register         = 0x52

	def __init__(self, name, table,  address):

		# name sensor
		self.name = name

		self.table = table

		# create bus with interface number
		self.bus = smbus.SMBus(self.interface_number) 

		# set address
		self.address = address

	def read(self):

		# write byte to the bus, (a request?)
		self.bus.write_byte(self.address, self.register)

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

		# probably shouldn't be a string though
		return results_string

	def calibrate_query(self):
					
		# ASCII				       	 C     a      l    ,     ?
		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x3F])
		time.sleep(5.4)
		
		results = bus.read_i2c_block_data(self.address, self.register)

		time.sleep(3)
		
		print results

	def calibrate_clear(self): 

		# ASCII					C      a     l      ,    c     l      e    a     r       
		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x63, 0x6C, 0x65, 0x61, 0x72])
		time.sleep(5)

		# get calibration info
		results = bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(5)

		print results

class pH_sensor(I2C_sensor):

	def calibrate_low(self):

		# ASCII			        	C      a     l    ,      l     o    w      ,    4     .     0     0
		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x6C, 0x6F, 0x77, 0x2C, 0x34, 0x2E, 0x30, 0x30])
		time.sleep(5)

		# get calibration info
		results = bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(5)
		
		print results

	def calibrate_mid(self):

		# ASCII					C      a     l      ,    m     i      d    ,     7     .     0    0 
		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x6D, 0x69, 0x64, 0x2C, 0x37, 0x2E, 0x30, 0x30])
		time.sleep(5)

		# get calibration info
		results = bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(5)

		print results
		
	def calibrate_high(self):

		# ASCII					C      a     l      ,    h     i      g     h     ,     1      0     .     0    0 
		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x68, 0x69, 0x67, 0x68, 0x2C, 0x31, 0x30, 0x2E, 0x30, 0x30])
		time.sleep(5)

		# get calibration info
		results = bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(5)

		print results

class dissolved_oxygen_sensor(I2C_sensor):

	def calibrate(self):

		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C]) #Cal (Calibrates the device to atmospheric oxygen levels)
		time.sleep(5)

		results=bus.read_i2c_block_data(self.address, self.register) #get calibration info
		time.sleep(3)

		print results

class electrical_conductivity_sensor(I2C_sensor):

	def calibrate_dry(self):

		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x64, 0x72, 0x79]) #Cal, dry
		time.sleep(5)

		results = bus.read_i2c_block_data(self.address, self.register) #get calibration info
		print results #print data

		for index, item in enumerate(results):

			if item == 0:

				end_val = index
				break

		results = results[1:end_val]
		results_string = ''.join(chr(i) for i in results)

		print results_string #print data

	def calibrate_low(self):

		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x6C, 0x6F, 0x77, 0x2C, 0x31, 0x32, 0x38, 0x38, 0x30]) #Cal, low, n
		time.sleep(5)

		results = bus.read_i2c_block_data(self.address, self.register) #read cal info
		print results #print data

	def calibrate_high(self):

		bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x68, 0x69, 0x67, 0x68, 0x2C, 0x38, 0x30, 0x30, 0x30, 0x30]) #Cal, high, n (80000)
		time.sleep(5)

		results = bus.read_i2c_block_data(self.address, self.register) #read cal info
		time.sleep(5)

		print results #print data

class total_pressure_sensor(I2C_sensor):

	def __init__(self, name, table, interface_number):

		# name sensor
		self.name = name

		self.table = table

		# set interface number
		self.interface_number = interface_number

	def read(self):

		# Copyright (c) 2014 Adafruit Industries
		# Author: Tony DiCola
		#
		# Permission is hereby granted, free of charge, to any person obtaining a copy
		# of this software and associated documentation files (the "Software"), to deal
		# in the Software without restriction, including without limitation the rights
		# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
		# copies of the Software, and to permit persons to whom the Software is
		# furnished to do so, subject to the following conditions:
		#
		# The above copyright notice and this permission notice shall be included in
		# all copies or substantial portions of the Software.
		#
		# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
		# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
		# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
		# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
		# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
		# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
		# THE SOFTWARE.

		# Can enable debug output by uncommenting:
		#import logging
		#logging.basicConfig(level=logging.DEBUG)

		# Default constructor will pick a default I2C bus.
		#
		# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
		# from the main GPIO header and the library will figure out the bus number based
		# on the Pi's revision.
		#
		# For the Beaglebone Black the library will assume bus 1 by default, which is
		# exposed with SCL = P9_19 and SDA = P9_20.

		# In MarsOASIS case, TP1 has SCL = P9_17 and SDA = P9_18 of bus 2.
		# In MarsOASIS case, TP2 has SCL = P9_21 and SDA = P9_22 of bus 1.
		sensor = BMP085.BMP085(busnum = self.interface_number) 

		# You can also optionally change the BMP085 mode to one of BMP085_ULTRALOWPOWER, 
		# BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES.  See the BMP085
		# datasheet for more details on the meanings of each mode (accuracy and power
		# consumption are primarily the differences).  The default mode is STANDARD.
		#sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

		return sensor.read_temperature(), sensor.read_pressure(), sensor.read_altitude(), sensor.read_sealevel_pressure()

# dissolved oxygen probe
DO = I2C_sensor("DO", "do_probe_and_circuitry", 0x61)

# pH probes
pH = {1: I2C_sensor("pH1", "ph_and_circuitry", 0x65),
      2: I2C_sensor("pH2", "ph_and_circuitry", 0x63)}

# electrical conductivity probes
EC = {1: I2C_sensor("EC1", "electrical_conductivity", 0x66),
      2: I2C_sensor("EC2", "electrical_conductivity", 0x64)}

# total pressure sensors
TP = {1: total_pressure_sensor("TP1", "total_pressure", 2),
      2: total_pressure_sensor("TP2", "total_pressure", 1)}
