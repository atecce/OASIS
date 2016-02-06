# need this for temperature
import Adafruit_DHT

# doesn't seem like one wire sensors are standardized in any fashion
class one_wire_sensor: pass

class temperature(one_wire_sensor):

	def __init__(self, name, ID):

		self.name = name

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

	def __init__(self, name, pin):

		self.name = name

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
		#pin = 'P8_8'
		
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

# temperature sensors (temp5?)
temp = {1: temperature("temp1", "28-00000673a8a7"),
	2: temperature("temp2", "28-0000065f27cc"),
	3: temperature("temp3", "28-0000065eb57a"),
	4: temperature("temp4", "28-000006747f7f")}
	      
# relative humidity and temperature sensors, (RHTemp3?)
RHTemp = {1: RH_and_temp("RHTemp1", 'P8_8'),
	  2: RH_and_temp("RHTemp2", 'P8_9'),
	  3: RH_and_temp("RHTemp3", 'P8_10')}
