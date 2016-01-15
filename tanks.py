class tank:

	volume    = float()
	substance = str()

	def __init__(self, volume, substance): 

		# need to specify units
		self.volume = volume

# gallons
T1  = tank(10, None)
T2  = tank(5, None)
T3  = tank(2, "H20/Condensate")
T4  = tank(2, None)
T5  = tank(2, None)

# liters (why?)
T6  = tank(2.5, "pH")

# no units
T7  = tank(None, "CO2")
T8  = tank(None, "N2")

# gallons
T9  = tank(5, "Leachate")
