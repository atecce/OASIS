class actuator:

	def __init__(self, pin):

		# these are determined at construction
		self.pin = pin

	BBB_GPIO = {"P8_11": (45, "Heater"),
		    "P8_12": (44, "Chiller"),
		    "P8_14": (26, "O2_concentrator"),
		    "P8_16": (46, "Linear actuator"),
		    "P8_29": (87, "Pump 12"),
		    "P8_30": (89, "SOL1EN"),
		    "P8_31": (10, "SOL2EN"),
		    "P8_32": (11, "UV_filter"),
		    "P8_21": (62, "Pump 1"),
		    "P8_20": (63, "Pump 2"),
		    "P8_13": (23, "Pump 3"),
		    "P8_18": (65, "Pump 4"),
		    "P8_17": (27, "Pump 5"),
		    "P8_22": (37, "Pump 6"),
		    "P8_24": (33, "Pump 7"),
		    "P8_26": (61, "Pump 8"),
		    "P8_27": (86, "Pump 9"),
		    "P8_25": (32, "Pump 10"),
		    "P8_23": (36, "Pump 11"),
		    "P8_15": (47, "Linear actuator"),
		    "P8_34": (81, "Stepper motor directional"),
		    "P8_35": (8,  "Stepper motor enable"),
		    "P8_36": (80, "Stepper motor clock"),
		    "P8_45": (70, "Fan1"),
		    "P8_46": (71, "Fan2"),
		    "P9_16": (51, "LED")}

	def toggle(self): pass

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

EC_HSST = (1150, 1250)
pH_HSST = (5.5, 6)
day_temp_HSST = (23, 27)
night_temp_HSST = (18, 22)
soil_temp_HSST = (15, 20)
water_temp_HSST = (22, 24)
humidity_HSST = (50, 70)
pressure_HSST = (80, 84)
CO2_HSST = (1000, 2000)
PAR_HSST = (200, 250)
