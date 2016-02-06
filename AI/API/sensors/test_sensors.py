# need this for testing
import pytest

# import sensors by category
from ADC      import LL, MO, O2, PAR
from I2C      import DO, EC, pH, TP
from one_wire import RHTemp, temp
from UART     import CO2, flow_meter
from USB      import camera

#class test_ADC_sensors:

def test_liquid_level_sensors():

	observation = [LL[i].read() for i in LL]

	# check if in sensor range
	assert all(0 <= data <= 16 for data in observation)

def test_moisture_sensors():

	observation = [MO[i].read() for i in MO]

	# check if in sensor range
	assert all(0 <= data <= 50 for data in observation)

def test_oxygen_sensor():

	observation = O2.read()

	# check if in sensor range
	assert 0 <= observation <= 100

def test_PAR_sensors():

	observation = [PAR[i].read() for i in PAR]

	# check if in sensor range
	assert all(0 <= data <= 2000 for data in observation)

#class test_I2C_sensors:

def test_dissolved_oxygen_probe():

	observation = DO.read()

	# check if in sensor range
	assert 0 <= observation <= 15

def test_electrical_conductivity_sensors():

	observation = [EC[i].read() for i in EC]

	# check if in sensor range
	assert all(3 <= data <= 3000 for data in observation)

def test_pH_sensors():

	observation = [pH[i].read() for i in pH]

	# check if in sensor range
	assert all(2 <= data <= 12 for data in observation)

def test_total_pressure_sensors():

	observation = [TP[i].read() for i in TP]

	# check if in sensor range
	assert all(300 <= data <= 1100 for data in observation)

#class test_one_wire_sensors:

def test_relative_humidity_and_temperature_sensors():

	observation = [RHTemp[i].read() for i in RHTemp]

	# check if in sensor range
	assert all(5 <= data[0] <= 99 and -40 <= data[1] <= 80 for data in observation)
	
def test_temperature_sensors():

	observation = [temp[i].read() for i in temp]

	# check if in sensor range
	assert all(0 <= data <= 100 for data in observation)

#class test_UART_sensors:

def test_CO2_sensor():

	observation = CO2.read()

	# check if in sensor range
	assert 0 <= observation <= 2000

def test_flow_meters():

	observation = [flow_meter[i].read() for i in flow_meter] 

	# check if in sensor range
	assert all(0.2 <= data <= 2 for data in observation)
	
#class test_USB:

def test_camera():

	camera.read()
