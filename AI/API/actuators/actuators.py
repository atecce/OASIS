class actuator:

	def __init__(self, pin):

		self.path = "/sys/devices/virtual/gpio/gpio" + pin + "/value" 

	def read(self): 

		state = open(self.path).read()

		return state

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

for i in pump: print pump[i].read()

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
