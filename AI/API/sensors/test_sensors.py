# need this for testing
import pytest

# import sensors by category
from I2C      import LL, DO, pH, EC, TP, PAR, MO, O2
from one_wire import temp, RHTemp
from UART     import flow_meter, CO2
from USB      import camera

class test_sensors:

	def test_camera(self):

		camera.read()

	def test_CO2_sensor(self):

		observation = CO2.read()

		print observation

	def test_dissolved_oxygen_sensor(self):

		observation = DO.read()

		print observation

	def test_electrical_conductivity_sensors(self):

		observation = [electrical_conductivity.read() for electrical_conductivity in EC]

		print observation

	def test_flow_meters(self):

		observation = [flow.read() for flow in flow_meter] 

		print observation

	def test_liquid_level_sensors(self):

		observation = [liquid_level.read() for liquid_level in LL]

		print observation

	def test_moisture_sensors(self):

		observation = [moisture.read() for moisture in MO]

		print observation

	def test_oxygen_sensor(self):

		observation = O2.read()

		print observation

	def test_PAR_sensors(self):

		observation = [PAR_value.read() for PAR_value in PAR]

		print observation

	def test_pH_sensors(self):

		observation = [pH_sensor.read() for pH_sensor in pH]

		print observation

	def test_relative_humidity_and_temperature_sensors(self):

		observation = [relative_humidity_and_temperature.read() for relative_humidity_and_temperature in RHTemp]

		print observation

	def test_temperature_sensors(self):

		observation = [temperature.read() for temperature in temp]

		print observation

	def test_total_pressure_sensors(self):

		observation = [total_pressure.read() for total_pressure in TP]

		print observation
