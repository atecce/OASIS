#!/usr/bin/env python

# need this to interact with BBB
import Adafruit_BBIO.GPIO

# need this for unit tests
import unittest

# need these for pins
from pins import P8, P9, GPIO

class sensor_test(unittest.TestCase):

	def test_GPIO_in(self):

		# for each pin in P9
		for number in P8: 
			
			# check if it's a GPIO
			if isinstance(P8[number], GPIO):

				# contruct pin name
				pin = "P8"+"_"+str(number)

				# display pin
				print "pin is " + pin 

				# set up pin
				Adafruit_BBIO.GPIO.setup(pin, Adafruit_BBIO.GPIO.IN)

				# print output of pin
				if Adafruit_BBIO.GPIO.input(pin): print pin + " is high" 
				else: print pin + " is low" 

				# clean out pin
				Adafruit_BBIO.GPIO.cleanup()

		# for each pin in P9
		for number in P9: 
			
			# check if it's a GPIO
			if isinstance(P9[number], GPIO):

				# contruct pin name
				pin = "P9"+"_"+str(number)

				# display pin
				print "pin is " + pin 

				# set up pin
				Adafruit_BBIO.GPIO.setup(pin, Adafruit_BBIO.GPIO.IN)

				# print output of pin
				if Adafruit_BBIO.GPIO.input(pin): print pin + " is high" 
				else: print pin + " is low" 

				# clean out pin
				Adafruit_BBIO.GPIO.cleanup()

if __name__ == "__main__": unittest.main()
