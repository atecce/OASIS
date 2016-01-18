# need this for testing
import random

import threading

O = list()

class sensor(threading.Thread):

	function            = str()
	units               = str()
	sensor_range        = dict()
	required_resolution = float()

	def __init__ (self):

		threading.Thread.__init__(self)

	def read(self):

		return self.run()

	def run(self): 

		# will read voltage from Beaglebone (for now assumes a random value for testing)
		voltage = random.uniform(0, 3.3)

		print self.name
		print voltage, "volts"

		# assumes the function from the voltage is a straight line connecting the two points (y = mx + b)
		return (self.sensor_range["high"] / 3.3) * voltage + self.sensor_range["low"]

class EC(sensor):

	# Electrical Conductivity (Measuring Nutrient Deficit) in Growth Medium & Reservoir

	name 		    = "EC"
	
	# check this again
	units               = "micro-S-cm-l"	

	sensor_range        = {"low": 3, "high": 3000}
	required_resolution = 1

class pH(sensor): 

	# pH in Growth Medium & Reservoir

	name 		    = "pH"
	units               = "pH"
	sensor_range        = {"low": 2, "high": 12}
	required_resolution = .2

class temperature(sensor): 

	# Liquid Temperature in Reservoir (1) & Growth Medium (4)

	name 	            = "temperature"
	units               = "C"
	sensor_range        = {"low": 0, "high": 100}
	required_resolution = 1

class moisture(sensor): 

	# Volumetric Water Content in Growth Medium

	name 		    = "moisture"
	units               = "%"
	sensor_range        = {"low": 0, "high": 50}
	required_resolution = 1

class DO_probe(sensor): 

	# Dissolved Oxygen in Mixing Reservoir

	name 		    = "DO probe"
	units               = "mg/L"
	sensor_range        = {"low": 0, "high": 15}
	required_resolution = .1

class liquid_level(sensor): 

	# Liquid Level in Mixing, Nutrient, pH, Leachate, & Condensate Tanks

	name 		    = "liquid level"
	units               = "cm"
	sensor_range        = {"low": 0, "high": 40.5}
	required_resolution = 1.25

class flow_meter(sensor): 

	# water Flow Rate Into & Out of Growth

	name 		    = "flow meter"
	units               = "gpm"
	sensor_range        = {"low": .2, "high": 2}
	required_resolution = .05

class RH_temp(sensor):

	# Internal (2) & External (1) Relative Humidity & Air Temperature

	name 		    = "RH temp"
	units               = "%", "C"
	sensor_range        = {"low": 5, "high": 99}
	required_resolution = 1

class total_pressure(sensor):

	# Internal (1) & External (1) Total Atmospheric Pressure"

	name		    = "total pressure"
	units               = "kPA"
	sensor_range        = {"low": 30, "high": 110}
	required_resolution = 1

class oxygen(sensor):

	# Internal (1) & External (1) O2 concentration"

	name		    = "oxygen"
	units               = "%"
	sensor_range        = {"low": 0, "high": 100}
	required_resolution = 1

class CO2(sensor):

	# Internal (1) & External CO2 concentration"

	name		    = "CO2"
	units               = "ppm"
	sensor_range        = {"low": 0, "high": 2000}
	required_resolution = 100

class light_PAR(sensor):

	# Internal (1) & External (1) Photosynthetically Active Radiation (PAR)"

	name		    = "light PAR"
	units               = "micro-mol / (m**2 * s)"
	sensor_range        = {"low": 0, "high": 2000}
	required_resolution = 2

class camera(sensor):

	# Plant Health Imagery

	name		    = "camera"
	units               = "RGB"
	sensor_range        = {"low": 1, "high": 255}
	required_resolution = "1k0x1k"

def test_sensors(sensors):

	for sensor in sensors: 
		
		print sensor.read(), sensor.units
		print sensor.sensor_range
		print

S101 = EC()
S102 = pH()
S103 = temperature()
S104 = EC()
S105 = liquid_level()
S106 = liquid_level()
S107 = liquid_level()
S108 = liquid_level()
S109 = liquid_level()
S110 = flow_meter()
S111 = flow_meter()
S112 = liquid_level()

S201 = temperature()
S202 = temperature()
S203 = temperature()
S204 = temperature()
S205 = EC()
S206 = pH()
S208 = moisture()
S209 = moisture()
S210 = moisture()
S211 = moisture()

S301 = RH_temp()
S302 = RH_temp()
S303 = total_pressure()
S304 = oxygen()
S305 = CO2()
S306 = light_PAR()
S307 = camera()

S401 = RH_temp()
S402 = total_pressure()
S403 = light_PAR()

sensors = (S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
	   S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
	   S301, S302, S303, S304, S305, S306, S307,
	   S401, S402, S403)

print

test_sensors(sensors)
