# need this for testing
import random

# need these to interface with Beaglebone
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM  as PWM
import Adafruit_BBIO.ADC  as ADC
import Adafruit_BBIO.UART as UART
from Adafruit_I2C import Adafruit_I2C

class Sensor():

	""" Each sensor has a name, a pin number, a range, and a required resolution. """ 

	name	 	    = str()
	pin		    = str()
	sensor_range        = dict()
	connection          = str()
	required_resolution = float()

	def __init__ (self, name, pin, connection):

		# attributes of a sensor 
		self.name       = name
		self.pin        = pin
		self.connection = connection

		# set up the pin (only takes GPIO now)
		if connection == "GPIO": GPIO.setup(pin, GPIO.IN)

	def read(self): 

		# will read voltage from Beaglebone (for now assumes a random value for unimplemented sensors)
		if self.connection == "GPIO": x = GPIO.input(self.pin)
		else: 			      x = random.uniform(0, 3.3)

		# assumes the function from the voltage to the units of the sensor 
		# is a straight line connecting the two points of the range (y = mx + b)

		delta_y = self.sensor_range["high"] - self.sensor_range["low"]
		delta_x = 3.3

		m = delta_y / delta_x

		b = self.sensor_range["low"]

		y = m*x + b

		return y

class EC(sensor):

	# micro-S-cm-l
	sensor_range        = {"low": 3, "high": 3000}
	required_resolution = 1

class pH(sensor): 

	# pH 
	sensor_range        = {"low": 2, "high": 12}
	required_resolution = .2

class temperature(sensor): 

	# C
	sensor_range        = {"low": 0, "high": 100}
	required_resolution = 1

class moisture(sensor): 

	# %
	sensor_range        = {"low": 0, "high": 50}
	required_resolution = 1

class DO_probe(sensor): 

	# mg/L
	sensor_range        = {"low": 0, "high": 15}
	required_resolution = .1

class liquid_level(sensor): 

	# cm
	sensor_range        = {"low": 0, "high": 40.5}
	required_resolution = 1.25

class flow_meter(sensor): 

	# gpm
	sensor_range        = {"low": .2, "high": 2}
	required_resolution = .05

class RH_temp(sensor):

	# C
	sensor_range        = {"low": 5, "high": 99}
	required_resolution = 1

class total_pressure(sensor):

	# kPA
	sensor_range        = {"low": 30, "high": 110}
	required_resolution = 1

class oxygen(sensor):

	# %
	sensor_range        = {"low": 0, "high": 100}
	required_resolution = 1

class CO2(sensor):

	# ppm
	sensor_range        = {"low": 0, "high": 2000}
	required_resolution = 100

class light_PAR(sensor):

	# micro-mol per meters-squared seconds
	sensor_range        = {"low": 0, "high": 2000}
	required_resolution = 2

class camera(sensor):

	# RGB
	sensor_range        = {"low": 1, "high": 255}
	required_resolution = "1k0x1k"

S101 =           EC("S101", None,    None)
S102 =           pH("S102", None,    None)
S103 =  temperature("S103", "P8_03", "GPIO")
S104 =           DO("S104", None,    None)
S105 = liquid_level("S105", None,    None)
S106 = liquid_level("S106", None,    None)
S107 = liquid_level("S107", None,    None)
S108 = liquid_level("S108", None,    None)
S109 = liquid_level("S109", None,    None)
S110 =   flow_meter("S110", None,    None)
S111 =   flow_meter("S111", None,    None)
S112 = liquid_level("S112", None,    None)

S201 = temperature("S201", "P8_04", None)
S202 = temperature("S202", "P8_05", None)
S203 = temperature("S203", "P8_06", None)
S204 = temperature("S204", "P8_07", None)
S205 =          EC("S205", None,    None)
S206 =          pH("S206", None,    None)
S208 =    moisture("S208", None,    None)
S209 =    moisture("S209", None,    None)
S210 =    moisture("S210", None,    None)
S211 =    moisture("S211", None,    None)

S301 =        RH_temp("S301", "P8_08", None)
S302 =        RH_temp("S302", "P8_09", None)
S303 = total_pressure("S303", None,    None)
S304 =         oxygen("S304", None,    None)
S305 =            CO2("S305", None,    None)
S306 =      light_PAR("S306", None,    None)
S307 =         camera("S307", None,    None)

S401 =        RH_temp("S401", "P8_10", None)
S402 = total_pressure("S402", None,    None)
S403 =      light_PAR("S403", None,    None)

sensor_suite = (S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
	        S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
	        S301, S302, S303, S304, S305, S306, S307,
	        S401, S402, S403)
