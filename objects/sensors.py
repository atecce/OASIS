# need this for testing
import random

import Adafruit_BBIO.GPIO as GPIO

class sensor():

	name	 	    = str()
	pin		    = int()
	units               = str()
	sensor_range        = dict()
	required_resolution = float()

	def __init__ (self, name, pin):

		self.name = name

		self.pin = pin

		GPIO.setup(pin, GPIO.IN)

	def read(self): 

		# will read voltage from Beaglebone (for now assumes a random value for testing)
		voltage = random.uniform(0, 3.3)

		# assumes the function from the voltage is a straight line connecting the two points (y = mx + b)
		return ((self.sensor_range["high"] - self.sensor_range["low"]) / 3.3) * voltage + self.sensor_range["low"]

class EC(sensor):

	# Electrical Conductivity (Measuring Nutrient Deficit) in Growth Medium & Reservoir

	# check this again
	units               = "micro-S-cm-l"	

	sensor_range        = {"low": 3, "high": 3000}
	required_resolution = 1

class pH(sensor): 

	# pH in Growth Medium & Reservoir

	units               = "pH"
	sensor_range        = {"low": 2, "high": 12}
	required_resolution = .2

class temperature(sensor): 

	# Liquid Temperature in Reservoir (1) & Growth Medium (4)

	units               = "C"
	sensor_range        = {"low": 0, "high": 100}
	required_resolution = 1

class moisture(sensor): 

	# Volumetric Water Content in Growth Medium

	units               = "%"
	sensor_range        = {"low": 0, "high": 50}
	required_resolution = 1

class DO_probe(sensor): 

	# Dissolved Oxygen in Mixing Reservoir

	units               = "mg/L"
	sensor_range        = {"low": 0, "high": 15}
	required_resolution = .1

class liquid_level(sensor): 

	# Liquid Level in Mixing, Nutrient, pH, Leachate, & Condensate Tanks

	units               = "cm"
	sensor_range        = {"low": 0, "high": 40.5}
	required_resolution = 1.25

class flow_meter(sensor): 

	# water Flow Rate Into & Out of Growth

	units               = "gpm"
	sensor_range        = {"low": .2, "high": 2}
	required_resolution = .05

class RH_temp(sensor):

	# Internal (2) & External (1) Relative Humidity & Air Temperature

	units               = "%", "C"
	sensor_range        = {"low": 5, "high": 99}
	required_resolution = 1

class total_pressure(sensor):

	# Internal (1) & External (1) Total Atmospheric Pressure"

	units               = "kPA"
	sensor_range        = {"low": 30, "high": 110}
	required_resolution = 1

class oxygen(sensor):

	# Internal (1) & External (1) O2 concentration"

	units               = "%"
	sensor_range        = {"low": 0, "high": 100}
	required_resolution = 1

class CO2(sensor):

	# Internal (1) & External CO2 concentration"

	units               = "ppm"
	sensor_range        = {"low": 0, "high": 2000}
	required_resolution = 100

class light_PAR(sensor):

	# Internal (1) & External (1) Photosynthetically Active Radiation (PAR)"

	units               = "micro-mol / (m**2 * s)"
	sensor_range        = {"low": 0, "high": 2000}
	required_resolution = 2

class camera(sensor):

	# Plant Health Imagery

	units               = "RGB"
	sensor_range        = {"low": 1, "high": 255}
	required_resolution = "1k0x1k"

S101 =           EC("S101", None)
S102 =           pH("S102", None)
S103 =  temperature("S103", "P8_03")
S104 =           EC("S104", None)
S105 = liquid_level("S105", None)
S106 = liquid_level("S106", None)
S107 = liquid_level("S107", None)
S108 = liquid_level("S108", None)
S109 = liquid_level("S109", None)
S110 =   flow_meter("S110", None)
S111 =   flow_meter("S111", None)
S112 = liquid_level("S112", None)

S201 = temperature("S201", "P8_04")
S202 = temperature("S202", "P8_05")
S203 = temperature("S203", "P8_06")
S204 = temperature("S204", "P8_07")
S205 =          EC("S205", None)
S206 =          pH("S206", None)
S208 =    moisture("S208", None)
S209 =    moisture("S209", None)
S210 =    moisture("S210", None)
S211 =    moisture("S211", None)

S301 =        RH_temp("S301", "P8_08")
S302 =        RH_temp("S302", "P8_09")
S303 = total_pressure("S303", None)
S304 =         oxygen("S304", None)
S305 =            CO2("S305", None)
S306 =      light_PAR("S306", None)
S307 =         camera("S307", None)

S401 =        RH_temp("S401", 'P8_10')
S402 = total_pressure("S402", None)
S403 =      light_PAR("S403", None)

sensor_suite = (S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
	        S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
	        S301, S302, S303, S304, S305, S306, S307,
	        S401, S402, S403)
