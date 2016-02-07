# import sensors by category
from ADC      import LL, MO, O2, PAR
from I2C      import DO, EC, pH, TP
from one_wire import temp, RHTemp
from UART     import CO2, flow_meter
from USB      import camera

# needs to be ordered when dumping observation
sensor_suite = list()

# populate sensor suite (same order as submission document)

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
