class pin: pass

class I2C(pin): 
	
	ADC = bool()

class UART(pin): pass

class GPIO(pin):

	# GPIO has separate pin
	def __init__(self, pin = None):

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

P9[9]   = pin()
P9[10]  = pin()

P9[14]  = GPIO()
P9[15]  = GPIO()
P9[23]  = GPIO()
P9[29]  = GPIO()
P9[30]  = GPIO()
P9[31]  = GPIO()

P9[32]  = pin()
P9[33]  = pin()
P9[34]  = pin()
P9[35]  = pin()
P9[36]  = pin()
P9[37]  = pin()
P9[38]  = pin()
P9[39]  = pin()
P9[40]  = pin()

P9[41]  = GPIO()
P9[42]  = GPIO()
