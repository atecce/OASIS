#Mixing process


def leachateDump():
	pre_filterP8.activate()
	temp = False
	while temp == False:
		if T9_level_S112 < HSST_M22 or (S105+S113) > HSST_N21:
			pre_filterP8.deactivate()
			temp = True
		#read sensors	
	return

def condensateDump():
	if T3_level_S106 > HSST_M26:
		condensateP2.activate()
		temp = False
		while temp == False:
			if T3_level_S106 <= HSST_M26:
				condensateP2.deactivate()
				#read sensors
	return


def nutrientConditioning():
	while:
		if EC_S101 < HSST_K12:
			#activate for HSST_J12 seconds:
				NTR1P1.activate()
				NTR2P4.activate()
		else:
			return

def pHConditioning():
	while:
		if pH_S109 > HSST_L16:
			#activate for HSST_J16 seconds:
				pHP5.activate()
		else:
			return
		#wait for HSST_I16 seconds


if T9_level_S112 > HSST_N22 and (S105+S113) < HSST_N21:
	#pause watering funcion
	leachateDump()
	condensateDump()
	nutrientConditioning()
	pHConditioning()