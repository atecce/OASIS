def set_system(status):

	if status == "initiate germination": 

		activate("P11")
		activate("P7")
		activate("F2")
		activate("M6")
		activate("M7")
		activate("P10", 10)

	elif status == "autonomous":

		water("start")
		mix("start")
		compose_gas("start")
		vapor_pressure("start")
		light("start")
		time_lapse("start")
		day_cycle("start")

	elif status == "stand by":

		water("stop")
		mix("stop")
		compose_gas("stop")
		vapor_pressure("stop")
		light("stop")
		time_lapse("stop")
		day_cycle("stop")

		# some stuff after this

def water():

	for k in range(208, 212): pass

# need to figure out optional arguments
def activate(component, time):

	if component == "P7":

		component.start_troubleshooting_and monitoring()
		component.start_heating_cooling()
		start_ph_conditioning()
		activate("P1")

	# this needs work
	elif component == "P1": 

		reading = float("inf")

		# threshold in cm
		while reading >= threshold: reading = read("S105")

		deactivate("P1")

		mixing_process()
	

def run_health_checks():

	health_data = read_health_sensors()

	if meets_condition: 

		set_system("stand by")

	else: system_shutdown()

def system_shutdown(error):

	raise error

	secure_components()

	turn_off_system()

def main(argv):

	set_system("initiaiting")
	run_health_checks()
	run_monitor_record()
