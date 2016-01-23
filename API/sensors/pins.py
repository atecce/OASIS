class pin: pass

class I2C(PIN): 
	
	ADC = bool()

class UART(PIN): pass

class GPIO(PIN):

	# GPIO has separate pin
	def __init__(self, pin):

		self.pin = pin

P8 = dict()
P9 = dict()

P9[12]  = GPIO()
P9[25]  = GPIO()
P9[28]  = GPIO()
P9[19]  = GPIO()
P9[20]  = GPIO()
P8[39]  = GPIO()
P8[40]  = GPIO()
P8[41]  = GPIO()
P8[42]  = GPIO()
P8[43]  = GPIO()
P8[44]  = GPIO()

P9[9]   = PIN()
P9[10]  = PIN()

P9[14]  = GPIO()
P9[15]  = GPIO()
P9[23]  = GPIO()
P9[29]  = GPIO()
P9[30]  = GPIO()
P9[31]  = GPIO()

P9[32]  = PIN()
P9[33]  = PIN()
P9[34]  = PIN()
P9[35]  = PIN()
P9[36]  = PIN()
P9[37]  = PIN()
P9[38]  = PIN()
P9[39]  = PIN()
P9[40]  = PIN()

P9[41]  = GPIO()
P9[42]  = GPIO()
