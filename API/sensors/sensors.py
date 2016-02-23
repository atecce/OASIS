from ADC import *
from I2C import *
from one_wire import *
from UART import *

# populate sensor suite by sensor category
sensor_suite = {'EC1': electrical_conductivity("electrical_conductivity",  0x66),
		'pH1':	       	    I2C_sensor("ph_and_circuitry",         0x65),
		'temp1':       	   temperature("liquid_temp",             "28-00000673a8a7"),
		'DO':          	    I2C_sensor("do_probe_and_circuitry",   0x61),
		'LL1': 	       	  liquid_level("liquid_level",             0x80),
		'LL2': 	       	  liquid_level("liquid_level",             0xA0),
		'LL3': 	       	  liquid_level("liquid_level",             0xC0),
		'LL4': 	       	  liquid_level("liquid_level",             0xE0),
		'LL5': 	       	  liquid_level("liquid_level",             0xD0),
		'flow_meter1': 	    flow_meter("flow_meter_and_circuitry", 1),
		'flow_meter2': 	    flow_meter("flow_meter_and_circuitry", 4),
		'LL6': 	          liquid_level("liquid_level",             0xF0),
		'temp2':           temperature("soil_temp",               "28-0000065f27cc"),
		'temp3':           temperature("soil_temp",               "28-0000065eb57a"),
		'temp4':           temperature("soil_temp",               "28-000006747f7f"),
		'EC2': electrical_conductivity("electrical_conductivity",  0x64),
		'pH2':	            I2C_sensor("ph_and_circuitry",	   0x63),
		'MO1':	              moisture("moisture",                 0x80),
		'MO2':	              moisture("moisture",                 0xA0),
		'MO3':	              moisture("moisture",                 0xC0),
		'MO4':	              moisture("moisture",                 0xE0),
		'RHT1':	           RH_and_temp("rh_and_air_temp",         "P8_8"),
		'RHT2':	           RH_and_temp("rh_and_air_temp",         "P8_9"),
		'TP1':	        total_pressure("total_pressure",           2),
		'O2':	                oxygen("O2"),
		'CO2':	                   CO2("CO2",                      5),
		'PAR1':	                   PAR("light",                    0xF0),
		'RHT3':	           RH_and_temp("rh_and_air_temp",         "P8_10"),
		'TP2':	        total_pressure("total_pressure",           1),
		'PAR2':                    PAR("light",                    0xD0)}

# populate sensor suite by SysID
S = {
     # liquid tanks and plumbing
     101: electrical_conductivity("electrical_conductivity",  0x66),
     102:              I2C_sensor("ph_and_circuitry",         0x65),
     103:             temperature("liquid_temp",             "28-00000673a8a7"),
     104:              I2C_sensor("do_probe_and_circuitry",   0x61),
     105:            liquid_level("liquid_level", 	      0x80), 
     106:            liquid_level("liquid_level", 	      0xA0),
     107:            liquid_level("liquid_level", 	      0xC0),
     108:            liquid_level("liquid_level", 	      0xE0),
     109:            liquid_level("liquid_level", 	      0xD0),
     110:              flow_meter("flow_meter_and_circuitry", 1),
     111:              flow_meter("flow_meter_and_circuitry", 4),
     112:            liquid_level("liquid_level", 	      0xF0),

     # growth medium
     201: 	       temperature("soil_temp", 	      "28-0000065f27cc"), 
     202: 	       temperature("soil_temp", 	      "28-0000065eb57a"),
     203: 	       temperature("soil_temp", 	      "28-000006747f7f"),
     205:  electrical_conductivity("electrical_conductivity",  0x64),
     206:  		I2C_sensor("ph_and_circuitry",	       0x63),
     208:  		  moisture("moisture", 		       0x80),
     209:  		  moisture("moisture", 		       0xA0),
     210:  		  moisture("moisture", 		       0xC0),
     211:  		  moisture("moisture", 		       0xE0),

     # internal atmosphere
     301:    RH_and_temp("rh_and_air_temp", "P8_8"),
     302:    RH_and_temp("rh_and_air_temp", "P8_9"),
     303: total_pressure("total_pressure",   2),
     304:         oxygen("O2"),
     305:            CO2("CO2", 5),
     306:            PAR("light", 0xF0),

     # external environment
     401:    RH_and_temp("rh_and_air_temp", "P8_10"),
     402: total_pressure("total_pressure",   1),
     403: 	     PAR("light", 	     0xD0)}
