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

		return results_string

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
		
class UART_sensor:

	def __init__(self, UART_number):

		# initiate sensor with a UART value
		UART.setup("UART" + str(UART_number))

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

		print "resistance is "
		print resistance

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

class CO2_sensor(UART_sensor):

	def read(self):

		# what determines this list of hexadecimel numbers?
		data = [0xfe, 0x44, 0x00, 0x08, 0x02, 0x9f, 0x25]

		# what does struct do? why 7B? what's the asterisk do?
		d = struct.pack("7B", *data)

		# is this a port to a terminal somewhere? why? why does the baudrate = 9600?
		ser = serial.Serial(port = "/dev/ttyO5", baudrate = 9600)

		# this was commented out. why was it ultimately unnecessary to initialize the serial class?
		#serial.begin(9600)

		# why is this delay necessary?
		time.sleep(1)

		# wait for some buffer to be non empty?
		while(ser.inWaiting() == 0):

			# write one byte at a time? why are we writing? a request?
			ser.write(d)

			# why is this delay necessary?
			time.sleep(1)

		# read in some buffer?
		A = ser.read(ser.inWaiting())

		# third bit times 2^8 (a byte) + fourth bit divided by 10^4
		percent = (ord(A[3])*256 + ord(A[4]))/10000.0

		# return percentage, probably shouldn't be a string
		return str(percent)

class flow_meter(UART_sensor):

		# flow meters

		# need to setup UART1 at boot, does not set up immediately
		# UART1 corresponds to ttyO1 in adafruit libraries
		# to manually enable use:
		# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
		# ls /dev/tty*   in terminal 

		# baudrate corresponds to flow meter circuit baud rate 
		ser = serial.Serial(port = "/dev/ttyO1", baudrate = 38400)

		# open serial port
		ser.open()

		# turn on LEDs. Green = power, red = instruction received/data transmit, 
		# amber = one rotation of meter blades
		ser.write("L1\r")

		# why is this delay necessary?
		time.sleep(.4)

		# write model number TurboFlow 226000
		ser.write("T1\r")

		# why is this delay neccesary?
		time.sleep(0.4)

		# return num of chars in receive buffer
		num = ser.inWaiting()

		# read Turboflow
		model_num = ser.read(num)

		# why is this delay necessary?
		time.sleep(0.4)

		# what are we writing?
		ser.write("R\r")

		# why is this delay necessary?
		time.sleep(2)

		# return num of chars in receive buffer
		num = ser.inWaiting()

		# returns entire serial buffer?
		single_flow_reading = ser.read(num)
		
		# need to setup UART1 at boot, does not set up immediately
		# UART1 corresponds to ttyO1 in adafruit libraries
		# to manually enable use:
		# echo BB-UART1 > /sys/devices/bone_capemgr.*/slots 
		# ls /dev/tty*   in terminal 

		# baudrate corresponds to flow meter circuit baud rate 
		ser = serial.Serial(port = "/dev/ttyO4", baudrate = 38400)

		print "Flow Meter Values:"
		print "Model Num is ", model_num
		print "Flow rate [total vol] [LPM] [LPH]:", single_flow_reading

		# close serial port
		ser.close()

# doesn't seem like one wire sensors are standardized in any fashion
class one_wire_sensor(sensor): pass

class temperature(one_wire_sensor):

	def __init__(self, ID):

		# note all the pins P8.3, P8.4, P8.5, P8.6 are shorted for intefacing all temp sensors on one-wire protocol

		# reading data from Temp 1 device with device ID:28-00000673a8a7 connected to P8.3 
		# reading data from Temp 2 device with device ID:28-0000065f27cc connected to P8.4 
		# reading data from Temp 3 device with device ID:28-0000065eb57a connected to P8.5 
		# reading data from Temp 4 device with device ID:28-000006747f7f connected to P8.6

		# set path of sensor
		self.path = "/sys/bus/w1/devices/" + ID + "/w1_slave" 

	def read(self):

		# get raw reading from device file
		raw = open(self.path, "r").read()

		# what is this?
		lastelement = raw.split("t=")[-1]

		# return parsed 
		return str(float(lastelement)/1000)

class RH_and_temp(one_wire_sensor):

	def __init__(self, pin):

		# each relative humidity and temperature sensor has a pin
		self.pin = pin

	def read(self):

		# Copyright (c) 2014 Adafruit Industries
		# Author: Tony DiCola
		
		# Permission is hereby granted, free of charge, to any person obtaining a copy
		# of this software and associated documentation files (the "Software"), to deal
		# in the Software without restriction, including without limitation the rights
		# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
		# copies of the Software, and to permit persons to whom the Software is
		# furnished to do so, subject to the following conditions:
		
		# The above copyright notice and this permission notice shall be included in all
		# copies or substantial portions of the Software.
		
		# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
		# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
		# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
		# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
		# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
		# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
		# SOFTWARE.
		
		# Sensor should be set to Adafruit_DHT.DHT11,
		# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
		sensor = Adafruit_DHT.DHT22
		
		# Example using a Beaglebone Black with DHT sensor
		# connected to pin P8_11.
		pin = 'P8_8'
		
		# Try to grab a sensor reading.  Use the read_retry method which will retry up
		# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
		humidity, temperature = Adafruit_DHT.read_retry(sensor, self.pin)
		
		# Note that sometimes you won't get a reading and
		# the results will be null (because Linux can't
		# guarantee the timing of calls to read the sensor). 
		# If this happens try again!
		
		# if humidity and temperature return something
		if humidity is not None and temperature is not None:

			# returns a printed tuple in units Celsius, %
			return '{0:0.1f}, {1:0.1f}'.format(temperature, humidity)

		# pretty sure I'd want to raise an error here
		else: print 'Failed to get reading. Try again!'

class USB_sensor(sensor): 

	def __init__(self):

		# set camera?
		self.camera = cv2.VideoCapture(0)

	def read(self):

		# ret and frame? what does read return?
		ret, frame = self.camera.read()

		# write to a file, why do we need frame?
		cv2.imwrite("image1.jpeg", frame)

		# release the camera
		self.camera.release()

		# close cv2?
		cv2.destroyAllWindows()

# liquid tanks and plumbing
S101 =      I2C_sensor(0x66, 0x52, 2)		# EC1
S102 =      I2C_sensor(0x65, 0x52, 2)		# pH1
S103 = temperature("28-00000673a8a7")	# temp1
S104 =      I2C_sensor(0x61, 0x52, 2)		# DO
S105 =      liquid_level(0x22, 0x80, 2)	        # LL1
S106 =      liquid_level(0x22, 0xA0, 2)	        # LL2
S107 =      liquid_level(0x22, 0xC0, 2)	        # LL3
S108 =      liquid_level(0x22, 0xE0, 2)	        # LL4
S109 =      liquid_level(0x22, 0xF0, 2)	        # LL5
S110 =      UART_sensor(1)			# flow_met1
S111 =      UART_sensor(4)			# flow_met2
S112 = 	    liquid_level(0x22, 0xD0, 2)		# LL6

# growth medium
S201 = temperature("28-0000065f27cc")	# temp2
S202 = temperature("28-0000065eb57a")	# temp3
S203 = temperature("28-000006747f7f")	# temp4
#S204 = one_wire_sensor()			# temp5
S205 = I2C_sensor(0x64, 0x52, 2)		# EC2
S206 = I2C_sensor(0x63, 0x52, 2)		# pH2
S208 = MO_sensor(0x21, 0x80, 2)		# MO1
S209 = MO_sensor(0x21, 0xA0, 2)		# MO2
S210 = MO_sensor(0x21, 0xC0, 2)		# MO3
S211 = MO_sensor(0x21, 0xE0, 2)		# MO4

# internal atmosphere
S301 = RH_and_temp('P8_8')			# RHTemp1
S302 = RH_and_temp('P8_9')			# RHTemp2
#S303 = I2C_sensor()				# TP1
S304 = ADC_sensor(0x22, 0xB0, 2)		# O2
#S305 = UART_sensor(5)				# C02
S306 = ADC_sensor(0x21, 0xF0, 2)		# PAR1
S307 = USB_sensor()				# camera

# external environment
#S401 = one_wire_sensor("P8_10")		# RHTemp3
#S402 = I2C_sensor()				# TP2
#S403 = ADC_sensor(0x21, 0xD0, 2)		# PAR2

# test EC1
#S101.read()

# test pH1
#S102.read()

# test temp1
#S103.read()

# test DO
#S104.read()

# test LL1
#S105.read()

# test LL2
#S106.read()

# test LL3
#S107.read()

# test LL4
#S108.read()

# test LL5
#S109.read()

# test flow meter 1
#S110.read()

# test flow meter 2
#S111.read()

# test LL6
#S112.read()

# test temp2
#S201.read()

# test temp3
#S202.read()

# test temp4
#S203.read()

# test EC2
#S205.read()

# test pH2
#S206.read()

# test MO1
#S208.read()

# test MO2
#S209.read()

# test MO3
#S210.read()

# test MO4
#S211.read()

# test RHTemp1
S301.read()

# test O2
#S304.read()

# test PAR1
#S306.read()

# test camera
#S307.read()
