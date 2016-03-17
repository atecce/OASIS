# need this for GPIO's
from GPIO import GPIO

# filter
F = {1: GPIO("UV_filter", 11)}

# valves
V = {3: GPIO("CO2_solenoid", 89),
     4: GPIO("N2_solenoid",  10)}

# miscellaneous
M = {1:  GPIO("heater",          45),
     2:  GPIO("chiller",         44),
     6:  GPIO("fan_1",           70),
     7:  GPIO("fan_2",           71),
     8:  GPIO("O2_concentrator", 26),
     18: GPIO("LED",		 51)}

# pumps
P = {1:  GPIO("main_pump", 	        62),
     2:  GPIO("condensate_pump",        63),
     3:  GPIO("nutrient_1_dosing",      23),
     4:  GPIO("nutrient_2_dosing",      65),
     5:  GPIO("pH_dosing", 	        27),
     6:  GPIO("nutrient_1_circulation", 37),
     7:  GPIO("air_bubbler",		33),
     8:  GPIO("filter_pump",		61),
     9:  GPIO("nutrient_2_circulation", 86),
     10: GPIO("humidifier_pump",	32),
     11: GPIO("main_tank_circulation",  36),
     12: GPIO("dehumidifier",		87)}
