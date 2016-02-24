# need this for test sensors
from test_API import test_sensor, test_RHTemp

# populate sensor suite
S = {
     # liquid tanks and plumbing		
     101:  test_sensor("electrical_conductivity", 1150, 1250),
     102:  test_sensor("ph_and_circuitry",         5.5,    6),     
     103:  test_sensor("liquid_temp", 		    22,   24),
#     104:   I2C_sensor("do_probe_and_circuitry",   0x61),
#     105: liquid_level("liquid_level", 	    0x80), 
#     106: liquid_level("liquid_level", 	    0xA0),
#     107: liquid_level("liquid_level", 	    0xC0),
#     108: liquid_level("liquid_level", 	    0xE0),
#     109: liquid_level("liquid_level", 	    0xD0),
#     110:   flow_meter("flow_meter_and_circuitry", 1),
#     111:   flow_meter("flow_meter_and_circuitry", 4),
#     112: liquid_level("liquid_level", 	    0xF0),


     # growth medium
     201: test_sensor("soil_temp", 15, 20), 
     202: test_sensor("soil_temp", 15, 20),
     203: test_sensor("soil_temp", 15, 20),
     205: test_sensor("electrical_conductivity", 1150, 1250),
     206: test_sensor("ph_and_circuitry",         5.5,    6),
#     208:    moisture("moisture", 0x80),
#     209:    moisture("moisture", 0xA0),
#     210:    moisture("moisture", 0xC0),
#     211:    moisture("moisture", 0xE0),

     # internal atmosphere
     301: test_RHTemp(),
     302: test_RHTemp(),
     303: test_sensor("total_pressure", 80, 84),
#     304:      oxygen("O2"),
     305: test_sensor("CO2",   1000, 2000),
     306: test_sensor("light",  200,  250),

     # external environment
     401: test_RHTemp(),
     402: test_sensor("total_pressure", 80,  84),
     403: test_sensor("light",         200, 250)}
