class sensor:

	def __init__ (self, units, sensor_range, required_resolution):

		self.function            = function
		self.units               = units
		self.sensor_range        = sensor_range
		self.required_resolution = required_resolution

	def read(self): pass

class EC(sensor):

	def __init__(self):

		self.function            = "Electrical Conductivity (Measuring Nutrient Deficit) in Growth Medium & Reservoir"
		
		# check this again
		self.units               = "micro-S-cm-l"	

		self.sensor_range        = (3, 3000)

		self.required_resolution = 1

class pH(sensor): 

	def __init__(self):

		self.function            = "pH in Growth Medium & Reservoir"
		
		# check this again
		self.units               = "pH"

		self.sensor_range        = (2, 12)

		self.required_resolution = .2

class temperature(sensor): 

	def __init__(self):

		self.function            = "Liquid Temperature in Reservoir (1) & Growth Medium (4)"
		
		self.units               = "C"

		self.sensor_range        = (0, 100)

		self.required_resolution = 1

class moisture(sensor): 

	def __init__(self):

		self.function            = "Volumetric Water Content in Growth Medium"
		
		self.units               = "%"

		self.sensor_range        = (0, 50)

		self.required_resolution = 1

class DO_probe(sensor): 

	def __init__(self):

		self.function            = "Dissolved Oxygen in Mixing Reservoir"
		
		self.units               = "mg/L"

		self.sensor_range        = (0, 15)

		self.required_resolution = .1

class liquid_level(sensor): 

	def __init__(self):

		self.function            = "Liquid Level in Mixing, Nutrient, pH, Leachate, & Condensate Tanks"
		
		self.units               = "cm"

		self.sensor_range        = (0, 40.5)

		self.required_resolution = 1.25

class flow_meter(sensor): 

	def __init__(self):

		self.function            = "Water Flow Rate Into & Out of Growth"
		
		self.units               = "gpm"

		self.sensor_range        = (.2, 2)

		self.required_resolution = .05

class RH_temp(sensor):

	def __init__(self):

		self.function            = "Internal (2) & External (1) Relative Humidity & Air Temperature"
		
		self.units               = "%", "C"

		self.sensor_range        = (5, 99)

		self.required_resolution = 1

class total_pressure(sensor):

	def __init__(self):

		self.function            = "Internal (1) & External (1) Total Atmospheric Pressure"
		
		self.units               = "kPA"

		self.sensor_range        = (30, 110)

		self.required_resolution = 1

class oxygen(sensor):

	def __init__(self):

		self.function            = "Internal (1) & External (1) O2 concentration"
		
		self.units               = "%"

		self.sensor_range        = (0, 100)

		self.required_resolution = 1

class CO2(sensor):

	def __init__(self):

		self.function            = "Internal (1) & External CO2 concentration"
		
		self.units               = "ppm"

		self.sensor_range        = (0, 2000)

		self.required_resolution = 100

class light_PAR(sensor):

	def __init__(self):

		self.function            = "Internal (1) & External (1) Photosynthetically Active Radiation (PAR)"
		
		self.units               = "micro-mol / (m**2 * s)"

		self.sensor_range        = (0, 2000)

		self.required_resolution = 2

class camera(sensor):

	def __init__(self):

		self.function            = "Plant Health Imagery"
		
		self.units               = "RGB"

		self.sensor_range        = (1, 255)

		self.required_resolution = "1k0x1k"

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
