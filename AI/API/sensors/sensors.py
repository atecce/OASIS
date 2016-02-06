# import sensors by category
from ADC      import LL, MO, O2, PAR
from I2C      import DO, EC, pH, TP
from one_wire import temp, RHTemp
from UART     import CO2, flow_meter
from USB      import camera

# needs to be ordered when dumping observation
sensor_suite = list()

# populate sensor suite

# one camera
sensor_suite.append(camera)

# six liquid level sensors
for i in (1, 2, 3, 4, 5, 6): sensor_suite.append(LL[i])

# one dissolved oxygen probe
sensor_suite.append(DO)

# two pH sensors
for i in (1, 2): sensor_suite.append(pH[i])

# two electrical conductivity sensors
for i in (1, 2): sensor_suite.append(EC[i])

# two total pressure sensors
for i in (1, 2): sensor_suite.append(TP[i])

# two PAR sensors
for i in (1, 2): sensor_suite.append(PAR[i])

# four moisture sensors
for i in (1, 2, 3, 4): sensor_suite.append(MO[i])

# one oxygen sensor
sensor_suite.append(O2)

# five temperature sensors
for i in (1, 2, 3, 4, 5): sensor_suite.append(temp[i])

# three relative humidity and temperature sensors
for i in (1, 2, 3): sensor_suite.append(RHTemp[i])

# two flow meters
for i in (1, 2): sensor_suite.append(flow_meter[i])

# one CO2 sensor
sensor_suite.append(CO2)

for sensor in sensor_suite: 

	try:
	
		print sensor.read()

	except IOError: print sensor

	except AttributeError: print sensor
