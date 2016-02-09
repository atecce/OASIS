# need this to wait
import time

class actuator:

	# makes output more readable
	lookup_key = {45: {1: "off", 0: "on"},
		      44: {1: "off", 0: "on"},
		      26: {1: "off", 0: "on"},	
		      87: {1: "off", 0: "on"},
		      89: {1: "off", 0: "on"},
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

	def __init__(self, name, pin):

		# assign name and pin
		self.name = name
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

actuator_suite = list()

# one heater
actuator_suite.append(actuator("heater", 45))

# one chiller
actuator_suite.append(actuator("chiller", 44))

# one O2 concentrator
actuator_suite.append(actuator("O2 concentrator", 26))

# twelve pumps
pump = {1:  actuator("Pump 1",  62),
	2:  actuator("Pump 2",  63),
	3:  actuator("Pump 3",  23),
	4:  actuator("Pump 4",  65),
	5:  actuator("Pump 5",  27),
	6:  actuator("Pump 6",  37),
	7:  actuator("Pump 7",  33),
	8:  actuator("Pump 8",  61),
	9:  actuator("Pump 9",  86),
	10: actuator("Pump 10", 32),
	11: actuator("Pump 11", 36),
	12: actuator("Pump 12", 87)}

for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12): actuator_suite.append(pump[i])

# two fans
fan = {1: actuator("Fan 1", 70),
       2: actuator("Fan 2", 71)}

for i in (1, 2): actuator_suite.append(fan[i])

# overhead light
actuator_suite.append(actuator("Overhead light", 51))

# turn each actuator on and off
for actuator in actuator_suite:

	actuator.toggle()	
	print actuator.name, "is", actuator.check_status()
	time.sleep(3)
	actuator.toggle()	
	print actuator.name, "is", actuator.check_status()
	time.sleep(3)
