# need this for testing
import pytest

# import sensors by category
from ADC      import *
from I2C      import *
from one_wire import *
from UART     import *
from USB      import camera

#class test_ADC_sensors:

def test_liquid_level_sensors():

	LL = {1: liquid_level("liquid_level", 0x80), 
	      2: liquid_level("liquid_level", 0xA0),
	      3: liquid_level("liquid_level", 0xC0),
	      4: liquid_level("liquid_level", 0xE0),
	      5: liquid_level("liquid_level", 0xD0),
	      6: liquid_level("liquid_level", 0xF0)}

	observation = [LL[i].read() for i in LL]

	# check if in sensor range
	assert all([0 <= data <= 16 for data in observation])

def test_moisture_sensors():

	MO = {1: moisture("moisture", 0x80),
	      2: moisture("moisture", 0xA0),
	      3: moisture("moisture", 0xC0),
	      4: moisture("moisture", 0xE0)}

	observation = [MO[i].read() for i in MO]

	# check if in sensor range
	assert all([0 <= data <= 50 for data in observation])

def test_oxygen_sensor():
     
	O2 = oxygen("O2")

	observation = O2.read()

	# check if in sensor range
	assert 0 <= observation <= 100

def test_PAR_sensors():

	light = {1: PAR("light", 0xF0),
		 2: PAR("light", 0xD0)}

	observation = [light[i].read() for i in light]

	# check if in sensor range
	assert all([0 <= data <= 2000 for data in observation])

#class test_I2C_sensors:

def test_dissolved_oxygen_probe():

	sensor = I2C_sensor("do_probe_and_circuitry",  0x61)

	observation = DO.read()

	# check if in sensor range
	assert 0 <= observation <= 15

def test_electrical_conductivity_sensors():

	EC = {1: I2C_sensor("electrical_conductivity", 0x66),
	      2: I2C_sensor("electrical_conductivity", 0x64)}

	observation = [EC[i].read() for i in EC]

	# check if in sensor range
	assert all([3 <= data <= 3000 for data in observation])

def test_pH_sensors():

	pH = {1: I2C_sensor("ph_and_circuitry", 0x65),
	      2: I2C_sensor("ph_and_circuitry",	0x63)}
	      
	observation = [pH[i].read() for i in pH]

	# check if in sensor range
	assert all([2 <= data <= 12 for data in observation])

def test_total_pressure_sensors():

	TP = {1: total_pressure("total_pressure", 2),
	      2: total_pressure("total_pressure", 1)}

	observation = [TP[i].read() for i in TP]

	# check if in sensor range
	assert all([300 <= data <= 1100 for data in observation])

#class test_one_wire_sensors:

def test_relative_humidity_and_temperature_sensors():
	
	RHTemp = {1: RH_and_temp("rh_and_air_temp", 'P8_8'),
		  2: RH_and_temp("rh_and_air_temp", 'P8_9'),
		  3: RH_and_temp("rh_and_air_temp", 'P8_10')}

	observation = [RHTemp[i].read() for i in RHTemp]

	# check if in sensor range
	assert all([5 <= data[0] <= 99 and -40 <= data[1] <= 80 for data in observation])
	
def test_temperature_sensors():

	temp = {1: temperature("liquid_temp", "28-00000673a8a7"),
		2: temperature("liquid_temp", "28-0000065f27cc"), 
		3: temperature("liquid_temp", "28-0000065eb57a"),
		4: temperature("liquid_temp", "28-000006747f7f")}

	observation = [temp[i].read() for i in temp]

	# check if in sensor range
	assert all([0 <= data <= 100 for data in observation])

#class test_UART_sensors:

def test_CO2_sensor():

	# set up sensor
	sensor = CO2("CO2", 5)

	observation = CO2.read()

	# check if in sensor range
	assert 0 <= observation <= 2000

def test_flow_meters():

	flow = {1: flow_meter("flow_meter_and_circuitry", 1),
		2: flow_meter("flow_meter_and_circuitry", 4)}
     
	observation = [flow[i].read() for i in flow] 

	# check if in sensor range
	assert all([0.2 <= data <= 2 for data in observation])
	
#class test_USB:

def test_camera():

	camera.read()
