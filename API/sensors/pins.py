class pin: pass

class I2C(pin): 
	
	ADC = bool()

class UART(pin):

	comm   = str()
	number = int()

	def __init__(self, number, comm):

		self.number = number
		self.comm   = comm

class GPIO(pin):

	pin = int()

	# GPIO has separate pin
	def __init__(self, pin):

		self.pin = pin

P8 = dict()
P9 = dict()

P9[12] = GPIO(60)
P9[19] = GPIO(13)
P9[20] = GPIO(12)
P9[25] = GPIO(117)
P9[28] = GPIO(113)

P8[37] = UART(5, "transmit")
P8[38] = UART(5, "receive")

P8[39] = GPIO(76)
P8[40] = GPIO(77)
P8[41] = GPIO(74)
P8[42] = GPIO(75)
P8[43] = GPIO(72)
P8[44] = GPIO(73)

P9[9]  = pin()
P9[10] = pin()

P9[11] = UART(4, "receive")
P9[13] = UART(4, "transmit")

P9[14] = GPIO(50)
P9[15] = GPIO(48)
P9[23] = GPIO(49)

P9[24] = UART(1, "transmit")
P9[26] = UART(1, "receive")

P9[29] = GPIO(111)
P9[30] = GPIO(112)
P9[31] = GPIO(110)

P9[32] = pin()
P9[33] = pin()
P9[34] = pin()
P9[35] = pin()
P9[36] = pin()
P9[37] = pin()
P9[38] = pin()
P9[39] = pin()
P9[40] = pin()

P9[41] = GPIO(116)
P9[42] = GPIO(7)
