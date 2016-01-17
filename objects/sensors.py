import threading

class sensor(threading.Thread):

	function            = str()
	units               = str()
	sensor_range        = tuple()
	required_resolution = float()

	def __init__ (self, units, sensor_range, required_resolution):

		threading.Thread.__init__(self)

	def read(self): pass

class EC(sensor):

	function            = "Electrical Conductivity (Measuring Nutrient Deficit) in Growth Medium & Reservoir"
	
	# check this again
	units               = "micro-S-cm-l"	

	sensor_range        = (3, 3000)
	required_resolution = 1

class pH(sensor): 

	function            = "pH in Growth Medium & Reservoir"
	units               = "pH"
	sensor_range        = (2, 12)
	required_resolution = .2

class temperature(sensor): 

	function            = "Liquid Temperature in Reservoir (1) & Growth Medium (4)"
	units               = "C"
	sensor_range        = (0, 100)
	required_resolution = 1

class moisture(sensor): 

	function            = "Volumetric Water Content in Growth Medium"
	units               = "%"
	sensor_range        = (0, 50)
	required_resolution = 1

class DO_probe(sensor): 

	function            = "Dissolved Oxygen in Mixing Reservoir"
	units               = "mg/L"
	sensor_range        = (0, 15)
	required_resolution = .1

class liquid_level(sensor): 

	function            = "Liquid Level in Mixing, Nutrient, pH, Leachate, & Condensate Tanks"
	units               = "cm"
	sensor_range        = (0, 40.5)
	required_resolution = 1.25

class flow_meter(sensor): 

	function            = "water Flow Rate Into & Out of Growth"
	units               = "gpm"
	sensor_range        = (.2, 2)
	required_resolution = .05

class RH_temp(sensor):

	function            = "Internal (2) & External (1) Relative Humidity & Air Temperature"
	units               = "%", "C"
	sensor_range        = (5, 99)
	required_resolution = 1

class total_pressure(sensor):

	function            = "Internal (1) & External (1) Total Atmospheric Pressure"
	units               = "kPA"
	sensor_range        = (30, 110)
	required_resolution = 1

class oxygen(sensor):

	function            = "Internal (1) & External (1) O2 concentration"
	units               = "%"
	sensor_range        = (0, 100)
	required_resolution = 1

class CO2(sensor):

	function            = "Internal (1) & External CO2 concentration"
	units               = "ppm"
	sensor_range        = (0, 2000)
	required_resolution = 100

class light_PAR(sensor):

	function            = "Internal (1) & External (1) Photosynthetically Active Radiation (PAR)"
	units               = "micro-mol / (m**2 * s)"
	sensor_range        = (0, 2000)
	required_resolution = 2

class camera(sensor):

	function            = "Plant Health Imagery"
	units               = "RGB"
	sensor_range        = (1, 255)
	required_resolution = "1k0x1k"

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
