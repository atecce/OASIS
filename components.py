class component:

	def __init__(self, dimensions, input_voltage, flow_rate, concentration, outlet_pressure, internal_pressure):

		self.dimensions        = dimensions
		self.input_voltage     = input_voltage
		self.flow_rate         = flow_rate
		self.concentration     = concentration
		self.outlet_pressure   = outlet_pressure
		self.internal_pressure = internal_pressure

	def activate(self): pass

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

	def activate(self): pass

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
