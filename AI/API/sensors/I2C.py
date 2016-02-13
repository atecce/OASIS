# need this to wait
import time

# need this for I2C's
import smbus

# need this for total pressure sensors
import Adafruit_BMP.BMP085 as BMP085

class I2C_sensor: 

	# default interface number and address for I2C sensors
	bus_number = 2
	register   = 0x52

	def __init__(self, name, table,  address):

		# name sensor
		self.name = name

		# corresponding table in database
		self.table = table

		# create bus with bus number
		self.bus = smbus.SMBus(self.bus_number) 

		# set address
		self.address = address

	def read(self):

		# request reading
		self.bus.write_byte(self.address, self.register)
		time.sleep(1)

		# read response
		results = self.bus.read_i2c_block_data(self.address, self.register)
		time.sleep(1)

		# iterate through index and item
		for index, item in enumerate(results):

			# 0 indicates a terminating character (why not ASCII?)
			if item == 0:
				
				# set stopping index
				end_val = index
				break

		# parse results (first character just returns status)
		results = results[1:end_val]

		# beautiful list comprehension Sairam 
		# iterates through the string, converts them all to characters, and concatenates them in one line
		results_string = ''.join(chr(i) for i in results)

		return float(results_string)

	def calibrate_query(self):
					
		# ASCII				       	 C     a      l    ,     ?
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x3F])
		time.sleep(1)
		
		results = self.bus.read_i2c_block_data(self.address, self.register)
		time.sleep(1)
		
		print results

	def calibrate_query_test(self):
					
		# ASCII				       
		self.bus.write_i2c_block_data(self.address, int('C'), [int('a'), int('l'), int(','), int('?')])
		time.sleep(1)
		
		results = self.bus.read_i2c_block_data(self.address, self.register)
		time.sleep(1)
		
		print results

	def calibrate_clear(self): 

		# ASCII					C      a     l      ,    c     l      e    a     r       
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x63, 0x6C, 0x65, 0x61, 0x72])
		time.sleep(1)

		# get calibration info
		results = self.bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(1)

		print results

class pH_sensor(I2C_sensor):

	def calibrate_low(self):

		# ASCII			        	C      a     l    ,      l     o    w      ,    4     .     0     0
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x6C, 0x6F, 0x77, 0x2C, 0x34, 0x2E, 0x30, 0x30])
		time.sleep(1)

		# get calibration info
		results = self.bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(1)
		
		print results

	def calibrate_mid(self):

		# ASCII					C      a     l      ,    m     i      d    ,     7     .     0    0 
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x6D, 0x69, 0x64, 0x2C, 0x37, 0x2E, 0x30, 0x30])
		time.sleep(1)

		# get calibration info
		results = self.bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(1)

		print results
		
	def calibrate_high(self):

		# ASCII					C      a     l      ,    h     i      g     h     ,     1      0     .     0    0 
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x68, 0x69, 0x67, 0x68, 0x2C, 0x31, 0x30, 0x2E, 0x30, 0x30])
		time.sleep(1)

		# get calibration info
		results = self.bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(1)

		print results

class dissolved_oxygen_sensor(I2C_sensor):

	def calibrate(self):

		# Cal (Calibrates the device to atmospheric oxygen levels)
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C]) 
		time.sleep(1)

		# get calibration info
		results = self.bus.read_i2c_block_data(self.address, self.register) 
		time.sleep(1)

		print results

class electrical_conductivity_sensor(I2C_sensor):

	def calibrate_dry(self):

		# Cal, dry
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x64, 0x72, 0x79]) 
		time.sleep(1)

		# get calibration info
		results = self.bus.read_i2c_block_data(self.address, self.register) 
		print results

		# iterate through index and item
		for index, item in enumerate(results):

			# 0 indicates a terminating character (why not ASCII?)
			if item == 0:
				
				# set stopping index
				end_val = index
				break

		# parse results (first character just returns status)
		results = results[1:end_val]

		# put results in a string
		results_string = ''.join(chr(i) for i in results)

		print results_string 

	def calibrate_low(self):

		# Cal, low, n
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x6C, 0x6F, 0x77, 0x2C, 0x31, 0x32, 0x38, 0x38, 0x30]) 
		time.sleep(1)

		# get calibration info
		results = self.bus.read_i2c_block_data(self.address, self.register)
		time.sleep(1)

		print results 

	def calibrate_high(self):

		# Cal, high, n (80000)
		self.bus.write_i2c_block_data(self.address, 0x43, [0x61, 0x6C, 0x2C, 0x68, 0x69, 0x67, 0x68, 0x2C, 0x38, 0x30, 0x30, 0x30, 0x30]) 
		time.sleep(1)

		# get calibration info
		results = self.bus.read_i2c_block_data(self.address, self.register)
		time.sleep(1)

		print results

class total_pressure_sensor(I2C_sensor):

	def __init__(self, name, table, bus_number):

		# name sensor
		self.name = name

		# corresponding table in database
		self.table = table

		# set interface number
		self.bus_number = bus_number

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
		sensor = BMP085.BMP085(busnum = self.bus_number) 

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
