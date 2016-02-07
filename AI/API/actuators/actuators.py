class actuator:

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
		      70: None,	
		      71: {0: "low", 1: "high"},	
		      51: {0: "off", 1: "on"}}	

	def __init__(self, pin):

		self.pin = pin

		self.path = "/sys/devices/virtual/gpio/gpio" + str(pin) + "/value" 

	def check_status(self): 

		value = int(open(self.path).read().rstrip())

		state = self.lookup_key[self.pin][value]

		return state

	def toggle(self):

		device = open(self.path)

		value = int(device.read().rstrip())

		device.close()

		if   value == 0: value = 1
		elif value == 1: value = 0
		else: print "throw error"

		device = open(self.path, 'w')

		device.write(str(value))

		device.close()

heater = actuator(45)
chiller = actuator(44)
O2_concentrator = actuator(26)

pump = {1:  actuator(62),
	2:  actuator(63),
	3:  actuator(23),
	4:  actuator(65),
	5:  actuator(27),
	6:  actuator(37),
	7:  actuator(33),
	8:  actuator(61),
	9:  actuator(86),
	10: actuator(32),
	11: actuator(36),
	12: actuator(87)}

fan = {1: actuator(70),
       2: actuator(71)}

LED = actuator(51)

LED.toggle()
print LED.check_status()

EC_HSST         = (1150, 1250)
pH_HSST         = (5.5, 6)
day_temp_HSST   = (23, 27)
night_temp_HSST = (18, 22)
soil_temp_HSST  = (15, 20)
water_temp_HSST = (22, 24)
humidity_HSST   = (50, 70)
pressure_HSST   = (80, 84)
CO2_HSST 	= (1000, 2000)
PAR_HSST 	= (200, 250)
