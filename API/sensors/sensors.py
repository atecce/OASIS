# need these to interface with Beaglebone
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC  as ADC
import Adafruit_BBIO.UART as UART
from Adafruit_I2C import Adafruit_I2C
import Adafruit_DHT

class sensor():

	""" Each sensor has a name, a data communication type, a range, 
	    a required resolution, and a pin number """ 

	# these are constrained by the sensor type
	data_comm	    = str()
	sensor_range        = dict()
	connection          = str()
	required_resolution = float()

	# these are determined at construction
	def __init__ (self, name, pin):

		self.name = name
		self.pin  = pin

	# This method depends on quite a bit. Depending on the data communication
	# type and the sensor, it will use different libraries and return different 
	# values.
	def read(self): pass 

class EC(sensor):

	units		    = " micro-S-cm-l"
	data_comm	    = "I2C"
	sensor_range        = {"low": 3, "high": 3000}
	required_resolution = 1

class pH(sensor): 

	units		    = "pH"
	data_comm	    = "I2C"
	sensor_range        = {"low": 2, "high": 12}
	required_resolution = .2

class temperature(sensor): 

	units		    = "C"
	data_comm	    = "one-wire"
	sensor_range        = {"low": 0, "high": 100}
	required_resolution = 1

class moisture(sensor): 

	units		    = "%"
	data_comm	    = "ADC-I2C"
	sensor_range        = {"low": 0, "high": 50}
	required_resolution = 1

class DO_probe(sensor): 

	units		    = "mg/L"
	data_comm	    = "I2C"
	sensor_range        = {"low": 0, "high": 15}
	required_resolution = .1

class liquid_level(sensor): 

	units		    = "cm"
	data_comm	    = "ADC-I2C"
	sensor_range        = {"low": 0, "high": 40.5}
	required_resolution = 1.25

class flow_meter(sensor): 

	units		    = "gpm"
	data_comm	    = "UART"
	sensor_range        = {"low": .2, "high": 2}
	required_resolution = .05

class RH_temp(sensor):

	units		    = ("C", "%")
	data_comm	    = "one-wire"
	sensor_range        = {"low": 5, "high": 99}
	required_resolution = 1

class total_pressure(sensor):

	units		    = "kPA"
	data_comm	    = "I2C"
	sensor_range        = {"low": 30, "high": 110}
	required_resolution = 1

class oxygen(sensor):

	units		    = "%"
	data_comm	    = "ADC-I2C"
	sensor_range        = {"low": 0, "high": 100}
	required_resolution = 1

class CO2(sensor):

	units		    = "ppm"
	data_comm	    = "UART"
	sensor_range        = {"low": 0, "high": 2000}
	required_resolution = 100

class light_PAR(sensor):

	units		    = "micro-mol per meters-squared seconds"
	data_comm	    = "ADC-I2C"
	sensor_range        = {"low": 0, "high": 2000}
	required_resolution = 2

class camera(sensor):

	units		    = "RGB"
	data_comm	    = "USB"
	sensor_range        = {"low": 1, "high": 255}
	required_resolution = "1k0x1k"

# liquid tanks and plumbing
S101 =           EC("S101", 0x66)
S102 =           pH("S102", 0x65)
S103 =  temperature("S103", None)
S104 =     DO_probe("S104", 0x61)
S105 = liquid_level("S105", None)
S106 = liquid_level("S106", None)
S107 = liquid_level("S107", None)
S108 = liquid_level("S108", None)
S109 = liquid_level("S109", None)
S110 =   flow_meter("S110", None)
S111 =   flow_meter("S111", None)
S112 = liquid_level("S112", None)

# growth medium
S201 = temperature("S201", None)
S202 = temperature("S202", None)
S203 = temperature("S203", None)
S204 = temperature("S204", None)
S205 =          EC("S205", None)
S206 =          pH("S206", None)
S208 =    moisture("S208", None)
S209 =    moisture("S209", None)
S210 =    moisture("S210", None)
S211 =    moisture("S211", None)

# internal atmosphere
S301 =        RH_temp("S301", None)
S302 =        RH_temp("S302", "P8_9")
S303 = total_pressure("S303", 0x77)
S304 =         oxygen("S304", None)
S305 =            CO2("S305", None)
S306 =      light_PAR("S306", None)
S307 =         camera("S307", None)

# external environment
S401 =        RH_temp("S401", "P8_10")
S402 = total_pressure("S402", None)
S403 =      light_PAR("S403", None)

sensor_suite = (S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, 
	        S201, S202, S203, S204, S205, S206,       S208, S209, S210, S211,
	        S301, S302, S303, S304, S305, S306, S307,
	        S401, S402, S403)
