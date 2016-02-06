# import sensors by category
from I2C      import LL, DO, pH, EC, TP, PAR, MO, O2
from one_wire import temp, RHTemp
from UART     import flow_meter, CO2
from USB      import camera

# initializing as set because no requirement for order that I can see
# always assume as little as you need to
# Einstein: "Make things as simple as possible, but no simpler."
# don't see a reason to assume order
sensor_suite = set()

# populate sensor suite

# one camera
sensor_suite.add(camera)

# six liquid level sensors
for i in {1, 2, 3, 4, 5, 6}: sensor_suite.add(LL[i])

# one dissolved oxygen sensor
sensor_suite.add(DO)

# two pH sensors
for i in {1, 2}: sensor_suite.add(pH[i])

# two electrical conductivity sensors
for i in {1, 2}: sensor_suite.add(EC[i])

# two total pressure sensors
for i in {1, 2}: sensor_suite.add(TP[i])

# two PAR sensors
for i in {1, 2}: sensor_suite.add(PAR[i])

# four moisture sensors
for i in {1, 2, 3, 4}: sensor_suite.add(MO[i])

# one oxygen sensor
sensor_suite.add(O2)

# five temperature sensors
for i in {1, 2, 3, 4, 5}: sensor_suite.add(temp[i])

# three relative humidity and temperature sensors
for i in {1, 2, 3}: sensor_suite.add(RHTemp[i])

# two flow meter sensors
for i in {1, 2}: sensor_suite.add(flow_meter[i])

# one CO2 sensor
sensor_suite.add(CO2)
