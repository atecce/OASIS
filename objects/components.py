import threading

class component(threading.Thread):

	dimensions        = dict()
	input_voltage     = tuple()
	flow_rate         = float()
	concentration     = float()
	outlet_pressure   = float()
	internal_pressure = float()

	def __init__(self):

		threading.Thread.__init__(self)

	def activate(self): pass

class oxygen_concentrator(component):

	# inches
	dimensions        = {"W": 18.375, "H": 26.375, "D": 14.375}

	# volts, alternating current
	input_voltage     = (120, "AC")

	# range of numbers (min, max) (L/min)
	flow_rate         = (0.5, 5)

	# percentage
	concentration     = .93

	# outlet pressure (psi)
	outlet_pressure   = (-4.5, 4.5)

	# not applicable
	internal_pressure = None

class nitrogen_tank(component):

	# inches
	dimensions        = {"H": 20, "OD": 7}

	# volts, alternating current
	input_voltage     = (120, "AC")

	# (L/s)
	flow_rate         = 0.5

	# percentage
	concentration     = .99

	# outlet pressure (psi)
	outlet_pressure   = 5

	# internal pressure (psi)
	internal_pressure = 1600

class carbon_dioxide_tank(component):

	# inches
	dimensions        = {"H": 20, "OD": 7}

	# volts, alternating current
	input_voltage     = (120, "AC")

	# (L/s)
	flow_rate         = 0.5

	# percentage
	concentration     = .99

	# (psi)
	outlet_pressure   = 5

	# (psi)
	internal_pressure = 700

class dehumidifier(component):
		
	# inches
	dimensions        = {"W": 5.7, "H": 8.7, "D": 5.3}

	# volts, alternating current
	input_voltage     = (120, "AC")

	# (mL/day)
	flow_rate         = 250

	# categories not applicable
	concentration     = None
	outlet_pressure   = None
	internal_pressure = None

class fogging_nozzle(component):

	# inches
	dimensions        = {"OD": .5625, "L": .9375}

	# volts, alternating current
	input_voltage     = (120, "AC")

	# (mL/s)
	flow_rate         = 9

	# (psi)
	outlet_pressure   = 40

	# categories not applicable
	concentration     = None
	internal_pressure = None

def display_components():

	O2_concentrator_test = oxygen_concentrator()
	N2_tank_test 	     = nitrogen_tank()
	CO2_tank_test 	     = carbon_dioxide_tank()
	dehumidifier_test    = dehumidifier()
	fogging_nozzle_test  = fogging_nozzle()

	components = (O2_concentrator_test, N2_tank_test, CO2_tank_test, dehumidifier_test, fogging_nozzle_test)

	for component in components: 
		
		print component.dimensions,    component.input_voltage,   component.flow_rate, \
		      component.concentration, component.outlet_pressure, component.internal_pressure

display_components()
