# need this for GPIO's
from GPIO import GPIO

# filter
F = {1: GPIO("UV filter", 11)}

# valves
V = {3: GPIO("CO2 solenoid", 89),
     4: GPIO("N2 solenoid",  10)}

# miscellaneous
M = {1:  GPIO("heater",          45),
     2:  GPIO("chiller",         44),
     6:  GPIO("fan 1",           70),
     7:  GPIO("fan 2",           71),
     8:  GPIO("O2 concentrator", 26),
     18: GPIO("LED",		 51)}

# pumps
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
