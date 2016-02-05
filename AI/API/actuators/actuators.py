class actuator:

	def __init__(self, name):#, pin):

		# these are determined at construction
		self.name = name

class GPIO_actuator(actuator): 

	BBB_GPIO = {"P9_12": 60,
		    "P9_25": 117,
		    "P9_28": 113,
		    "P9_19": 13,
		    "P9_20": 12,
		    "P8_39": 76,
		    "P8_40": 77,
		    "P8_41": 74,
		    "P8_42": 75,
		    "P8_43": 72,
		    "P8_44": 73,
		    "P9_14": 50,
		    "P9_15": 48,
		    "P9_23": 49,
		    "P9_29": 111,
		    "P9_30": 112,
		    "P9_31": 110,
		    "P9_41": 116,
		    "P9_42": 7,
		    "P8_33": 9,
		    "P9_27": 115,
		    "P8_11": (45, "Heater"),
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

class PWM_actuator(actuator): pass

F1 = actuator("F1")
F2 = actuator("F2")
F3 = actuator("F3")
F4 = actuator("F4")
F5 = actuator("F5")

M01 = actuator("M01")
M02 = actuator("M02")
M03 = actuator("M03")

M05 = actuator("M05")
M06 = actuator("M06")
M07 = actuator("M07")
M08 = actuator("M08")
M09 = actuator("M09")
M10 = actuator("M10")
M11 = actuator("M11")
M12 = actuator("M12")

M15 = actuator("M15")
M16 = actuator("M16")
M17 = actuator("M17")
M18 = actuator("M18")
M19 = actuator("M19")

P01 = actuator("P01")
P02 = actuator("P02")
P03 = actuator("P03")
P04 = actuator("P04")
P05 = actuator("P05")
P06 = actuator("P06")
P07 = actuator("P06")
P08 = actuator("P08")
P09 = actuator("P09")
P10 = actuator("P10")
P11 = actuator("P11")
P12 = actuator("P12")

R01 = actuator("R01")
R02 = actuator("R02")

T01 = actuator("T01")
T02 = actuator("T02")
T03 = actuator("T03")
T04 = actuator("T04")
T05 = actuator("T05")
T06 = actuator("T06")
T07 = actuator("T07")
T08 = actuator("T08")
T09 = actuator("T09")

V02 = actuator("V02")
V03 = actuator("V03")
V04 = actuator("V04")
V05 = actuator("V05")

V07 = actuator("V07")

Z01 = actuator("Z01")
Z02 = actuator("Z02")
Z03 = actuator("Z03")
Z04 = actuator("Z04")
Z05 = actuator("Z05")
Z06 = actuator("Z06")
Z07 = actuator("Z06")
Z08 = actuator("Z08")
Z09 = actuator("Z09")
Z10 = actuator("Z10")
Z11 = actuator("Z11")
Z12 = actuator("Z12")
Z13 = actuator("Z13")

actuator_suite = (F1,  F2,  F3,  F4,  F5,
		  M01, M02, M03,      M05, M06, M07, M08, M09, M10, M11, M12,           M15, M16, M17, M18, M19,
		  P01, P02, P03, P04, P05, P06, P07, P08, P09, P10, P11, P12,
		  R01, R02,
		  T01, T02, T03, T04, T05, T06, T07, T08, T09,
		       V02, V03, V04, V05,      V07, 
		  Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z09, Z10, Z11, Z12, Z13)

print len(actuator_suite)

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
