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

#class test_I2C_sensors:

def test_dissolved_oxygen_sensor():

	observation = DO.read()

	print observation

def test_electrical_conductivity_sensors():

	observation = [EC[i].read() for i in EC]

	print observation

def test_pH_sensors():

	observation = [pH[i].read() for i in pH]

	print observation

def test_total_pressure_sensors():

	observation = [TP[i].read() for i in TP]

	print observation

#class test_one_wire_sensors:

def test_relative_humidity_and_temperature_sensors():

	observation = [RHTemp[i].read() for i in RHTemp]

	print observation

def test_temperature_sensors():

	observation = [temp[i].read() for i in temp]

	print observation

#class test_UART_sensors:

def test_CO2_sensor():

	observation = CO2.read()

	print observation

def test_flow_meters():

	observation = [flow_meter[i].read() for i in flow_meter] 

	print observation

#class test_USB:

def test_camera():

	camera.read()
