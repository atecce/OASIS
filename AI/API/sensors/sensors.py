# import sensors by category
from ADC      import LL, MO, O2, PAR
from I2C      import DO, EC, pH, TP
from one_wire import temp, RHTemp
from UART     import CO2, flow_meter
from USB      import camera

# populate sensor suite

S = {"101":   I2C_sensor("electrical_conductivity", 0x66),
     "102":   I2C_sensor("ph_and_circuitry",        0x65),
     "103":  temperature("liquid_temp", "28-00000673a8a7"),
     "104":   I2C_sensor("do_probe_and_circuitry",  0x61),
     "105": liquid_level("liquid_level", 0x80), 
     "106": liquid_level("liquid_level", 0xA0),
     "107": liquid_level("liquid_level", 0xC0),
     "108": liquid_level("liquid_level", 0xE0),
     "109": liquid_level("liquid_level", 0xD0),
     "110":   flow_meter("flow_meter_and_circuitry", 1),
     "111":   flow_meter("flow_meter_and_circuitry", 4),
     "112": liquid_level("liquid_level", 0xF0),

     "201": temperature("liquid_temp", "28-0000065f27cc"), 
     "202": temperature("liquid_temp", "28-0000065eb57a"),
     "203": temperature("liquid_temp", "28-000006747f7f"),
     "205":  I2C_sensor("electrical_conductivity", 0x64),
     "206":  I2C_sensor("ph_and_circuitry",	   0x63),
     "208":    moisture("moisture", 0x80),
     "209":    moisture("moisture", 0xA0),
     "210":    moisture("moisture", 0xC0),
     "211":    moisture("moisture", 0xE0),

     "301":    RH_and_temp("rh_and_air_temp", 'P8_8'),
     "302":    RH_and_temp("rh_and_air_temp", 'P8_9'),
     "303": total_pressure("total_pressure", 2),
     "304": 	    oxygen("O2"),
     "305":     CO2_sensor("CO2", 5),
     "306":            PAR("light", 0xF0),

     "401":    RH_and_temp("rh_and_air_temp", 'P8_10'),
     "402": total_pressure("total_pressure", 1),
     "403": 	       PAR("light", 0xD0)}

# two electrical conductivity sensors
for i in (1, 2): sensor_suite.append(EC[i])

# two pH sensors
for i in (1, 2): sensor_suite.append(pH[i])

# four temperature sensors
for i in (1, 2, 3, 4): sensor_suite.append(temp[i])

# four moisture sensors
for i in (1, 2, 3, 4): sensor_suite.append(MO[i])

# one dissolved oxygen probe
sensor_suite.append(DO)

# six liquid level sensors
for i in (1, 2, 3, 4, 5, 6): sensor_suite.append(LL[i])

# two flow meters
for i in (1, 2): sensor_suite.append(flow_meter[i])

# three relative humidity and temperature sensors
for i in (1, 2, 3): sensor_suite.append(RHTemp[i])

# two total pressure sensors
for i in (1, 2): sensor_suite.append(TP[i])

# one oxygen sensor
sensor_suite.append(O2)

# one CO2 sensor
sensor_suite.append(CO2)

# two PAR sensors
for i in (1, 2): sensor_suite.append(PAR[i])

# one camera
sensor_suite.append(camera)

for sensor in sensor_suite: 

	try:
	
		print sensor.name, sensor.table, sensor.read()

	except IOError: print "IOError"

	#except AttributeError: print "AttributeError"
