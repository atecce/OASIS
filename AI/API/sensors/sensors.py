# need this to concatenate ranges for predictable sensor suite iteration
from itertools import chain

# import sensors by category
from ADC      import *
from I2C      import *
from one_wire import *
from UART     import *
from USB      import camera

# populate sensor suite
S = {101:   I2C_sensor("electrical_conductivity", 0x66),
     102:   I2C_sensor("ph_and_circuitry",        0x65),
     103:  temperature("liquid_temp", "28-00000673a8a7"),
     104:   I2C_sensor("do_probe_and_circuitry",  0x61),
     105: liquid_level("liquid_level", 0x80), 
     106: liquid_level("liquid_level", 0xA0),
     107: liquid_level("liquid_level", 0xC0),
     108: liquid_level("liquid_level", 0xE0),
     109: liquid_level("liquid_level", 0xD0),
     110:   flow_meter("flow_meter_and_circuitry", 1),
     111:   flow_meter("flow_meter_and_circuitry", 4),
     112: liquid_level("liquid_level", 0xF0),

     201: temperature("liquid_temp", "28-0000065f27cc"), 
     202: temperature("liquid_temp", "28-0000065eb57a"),
     203: temperature("liquid_temp", "28-000006747f7f"),
     205:  I2C_sensor("electrical_conductivity", 0x64),
     206:  I2C_sensor("ph_and_circuitry",	   0x63),
     208:    moisture("moisture", 0x80),
     209:    moisture("moisture", 0xA0),
     210:    moisture("moisture", 0xC0),
     211:    moisture("moisture", 0xE0),

     301:    RH_and_temp("rh_and_air_temp", 'P8_8'),
     302:    RH_and_temp("rh_and_air_temp", 'P8_9'),
     303: total_pressure("total_pressure", 2),
     304:         oxygen("O2"),
     305:            CO2("CO2", 5),
     306:            PAR("light", 0xF0),

     401:    RH_and_temp("rh_and_air_temp", 'P8_10'),
     402: total_pressure("total_pressure", 1),
     403: 	     PAR("light", 0xD0)}

# set of ID's sensors take
SysIDs = chain(range(101, 113), range(201, 204), range(205, 207), range(208, 212), range(301, 307), range(401, 404))

for SysID in SysIDs:

	try:
	
		print S[SysID], "S" + str(SysID), S[SysID].table, S[SysID].read()

	except IOError: print "IOError"

	#except AttributeError: print "AttributeError"
