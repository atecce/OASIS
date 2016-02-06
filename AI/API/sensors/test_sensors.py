# need this for testing
import pytest

# import sensors by category
from I2C      import LL, DO, pH, EC, PAR, MO, O2
from one_wire import temp, RHTemp
from UART     import flow_meter, CO2
from USB      import camera

def test_camera():

	camera.read()

def test_CO2_sensor():

	observation = CO2.read()

	print observation

def test_dissolved_oxygen_sensor():

	observation = DO.read()

	print observation

def test_electrical_conductivity_sensors():

	observation = [EC[i].read() for i in EC]

	print observation

def test_flow_meters():

	observation = [flow_meter[i].read() for i in flow_meter] 

	print observation

def test_liquid_level_sensors():

	observation = [LL[i].read() for i in LL]

	print observation

def test_moisture_sensors():

	observation = [MO[i].read() for i in MO]

	print observation

def test_oxygen_sensor():

	observation = O2.read()

	print observation

def test_PAR_sensors():

	observation = [PAR[i].read() for i in PAR]

	print observation

def test_pH_sensors():

	observation = [pH[i].read() for i in pH]

	print observation

def test_relative_humidity_and_temperature_sensors():

	observation = [RHTemp[i].read() for i in RHTemp]

	print observation

def test_temperature_sensors():

	observation = [temp[i].read() for i in temp]

	print observation

# have not attempted implementation yet
#	def test_total_pressure_sensors(self):
#
#		observation = [TP[i].read() for i in TP]
#
#		print observation
