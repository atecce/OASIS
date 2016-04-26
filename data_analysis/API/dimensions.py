import math

class CO2_cannister:

	height = 11.5
	radius = 2.5

	volume = height * math.pi*radius**2 + \
		 .5 * (4.0/3.0) * math.pi*radius**3

class enclosure:

	radius = 21.5

	volume = .5 * 4.0/3.0*math.pi*radius**3

print CO2_cannister.volume, enclosure.volume, enclosure.volume / CO2_cannister.volume
