# need this to chain SysID's together
from itertools import chain

# need this to wait
import time

class GPIO:

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
		state = self.lookup_key[self.pin][value]

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

F = {1: GPIO("UV filter", 11)}

print F[1].table, "is", F[1].check_status()

V = {3: GPIO("CO2 solenoid", 89),
     4: GPIO("N2 solenoid",  10)}

for SysID in range(3, 5):

	print V[SysID].table, "is", V[SysID].check_status()


M = {1:  GPIO("heater",          45),
     2:  GPIO("chiller",         44),
     6:  GPIO("fan 1",           70),
     7:  GPIO("fan 2",           71),
     8:  GPIO("O2 concentrator", 26),
     18: GPIO("LED",		 51)}

SysIDs = chain(range(1, 3), range(6, 9), range(18, 19))

for SysID in SysIDs:

	print M[SysID].table, "is", M[SysID].check_status()

P = {1:  GPIO("main pump", 	        62),
     2:  GPIO("condensate pump",        63),
     3:  GPIO("nutrient 1 dosing",      23),
     4:  GPIO("nutrient 2 dosing",      65),
     5:  GPIO("pH dosing", 	        27),
     6:  GPIO("nutrient 1 circulation", 37),
     7:  GPIO("air bubbler",		33),
     8:  GPIO("filter pump",		61),
     9:  GPIO("nutrient 2 circulation", 86),
     10: GPIO("humidifier pump",	32),
     11: GPIO("main tank circulation",  36),
     12: GPIO("dehumidifier",		87)}

for SysID in range(1, 13):

	print P[SysID].table, "is", P[SysID].check_status()
