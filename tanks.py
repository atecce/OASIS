class tank:

	volume    = float()
	substance = str()

	def __init__(self, volume): 

		# need to specify units
		self.volume = volume

# gallons
T1  = tank(10)
T2  = tank(5)
T3  = tank(2)
T4  = tank(2)
T5  = tank(2)

# liters (why?)
T6  = tank(2.5)

# no units
T7  = tank()
T8  = tank()

# gallons
T9  = tank(5)
