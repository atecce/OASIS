# need this to chain SysID's together
from itertools import chain

# need this to wait
import time

# makes output more readable
lookup_key = {45: {1: "off", 0: "on"},
	      44: {1: "off", 0: "on"},
	      26: {1: "off", 0: "on"},	
	      87: {1: "off", 0: "on"},
	      89: {1: "off", 0: "on"},
	      10: {1: "off", 0: "on"},
	      11: {1: "off", 0: "on"},
	      62: {0: "off", 1: "on"},
	      63: {0: "off", 1: "on"},
	      23: {0: "off", 1: "on"},
	      65: {0: "off", 1: "on"},
	      27: {0: "off", 1: "on"},
	      37: {0: "off", 1: "on"},
	      33: {0: "off", 1: "on"},
	      61: {0: "off", 1: "on"},
	      86: {0: "off", 1: "on"},
	      32: {0: "off", 1: "on"},
	      36: {0: "off", 1: "on"},
	      70: {0: "low", 1: "high"},
	      71: {0: "low", 1: "high"},	
	      51: {0: "off", 1: "on"}}	

class GPIO:

	def __init__(self, table, pin):

		# assign table
		self.table = table

		# assign pin
		self.pin = pin

		# set path for device file with pin
		self.path = "/sys/devices/virtual/gpio/gpio" + str(pin) + "/value" 

	def check_status(self): 

		# open up the device
		device = open(self.path)

		# read in the value as an integer
		value = int(device.read().rstrip())

		# close the device
		device.close()

		# look up the state
		state = lookup_key[self.pin][value]

		return state

	def toggle(self):

		# open the device for reading
		device = open(self.path)

		# read in the value as an integer
		value = int(device.read().rstrip())

		# close the device
		device.close()

		# flip the switch
		if   value == 0: value = 1
		elif value == 1: value = 0
		else: print "throw error"

		# open the device for writing
		device = open(self.path, 'w')

		# write the new value
		device.write(str(value))

		# close the device
		device.close()
