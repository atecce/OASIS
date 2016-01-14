class component:

#	# unfinished general template
#	dimensions = tuple([int() for i in range(len(dimensions))])
#
#	AC_DC = {"AC", "DC"}
#	input_voltage = (120, AC_DC)

	def __init__(self, dimensions, input_voltage, flow_rate, concentration, outlet_pressure, internal_pressure):

		self.dimensions        = dimensions
		self.input_voltage     = input_voltage
		self.flow_rate         = flow_rate
		self.concentration     = concentration
		self.outlet_pressure   = outlet_pressure
		self.internal_pressure = internal_pressure

class oxygen_concentrator(component):

	def __init__(self):

		# inches
		self.dimensions        = {"W": 18.375, "H": 26.375, "D": 14.375}

		# volts, alternating current
		self.input_voltage     = (120, "AC")

		# range of numbers (min, max) (L/min)
		self.flow_rate         = (0.5, 5)

		# percentage
		self.concentration     = .93

		# outlet pressure (psi)
		self.outlet_pressure   = (-4.5, 4.5)

		# not applicable
		self.internal_pressure = None

class nitrogen_tank(component):

	def __init__(self):

		# inches
		self.dimensions        = {"H": 20, "OD": 7}

		# volts, alternating current
		self.input_voltage     = (120, "AC")

		# (L/s)
		self.flow_rate         = 0.5

		# percentage
		self.concentration     = .99

		# outlet pressure (psi)
		self.outlet_pressure   = 5

		# internal pressure (psi)
		self.internal_pressure = 1600

class carbon_dioxide_tank(component):

	def __init__(self):

		# inches
		self.dimensions        = {"H": 20, "OD": 7}

		# volts, alternating current
		self.input_voltage     = (120, "AC")

		# (L/s)
		self.flow_rate         = 0.5

		# percentage
		self.concentration     = .99

		# (psi)
		self.outlet_pressure   = 5

		# (psi)
		self.internal_pressure = 700

class dehumidifier(component):

	def __init__(self):

		# inches
		self.dimensions        = {"W": 5.7, "H": 8.7, "D": 5.3}

		# volts, alternating current
		self.input_voltage     = (120, "AC")

		# (mL/day)
		self.flow_rate         = 250

		# categories not applicable
		self.concentration     = None
		self.outlet_pressure   = None
		self.internal_pressure = None

class fogging_nozzle(component):

	def __init__(self):

		# inches
		self.dimensions        = {"OD": .5625, "L": .9375}

		# volts, alternating current
		self.input_voltage     = (120, "AC")

		# (mL/s)
		self.flow_rate         = 9

		# (psi)
		self.outlet_pressure   = 40

		# categories not applicable
		self.concentration     = None
		self.internal_pressure = None

def display_components():

	O2_concentrator_test = oxygen_concentrator()
	N2_tank_test 	     = nitrogen_tank()
	CO2_tank_test 	     = carbon_dioxide_tank()
	dehumidifier_test    = dehumidifier()
	fogging_nozzle_test  = fogging_nozzle()

	components = (O2_concentrator_test, N2_tank_test, CO2_tank_test, dehumidifier_test, fogging_nozzle_test)

	for component in components: print component.dimensions, component.input_voltage, component.flow_rate, component.concentration, component.outlet_pressure, component.internal_pressure

class sensor:

	def __init__ (self, units, sensor_range, required_resolution):

		self.function            = function
		self.units               = units
		self.sensor_range        = sensor_range
		self.required_resolution = required_resolution

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

class relative_humidity(sensor):

	def __init__(self):

		self.function            = "Internal (2) & External (1) Relative Humidity"
		
		self.units               = "%"

		self.sensor_range        = (5, 99)

		self.required_resolution = 1

class air_temperature(sensor):

	def __init__(self):

		self.function            = "Internal (2) & External (1) Air Temperature"
		
		self.units               = "C"

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


