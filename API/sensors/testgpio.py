##sudo ntpdate pool.ntp.org

# need this to interact with Beaglebone
import Adafruit_BBIO.GPIO

# need this to wait
import time

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

for number in P9: 
	
	if isinstance(P9[number], GPIO):

		pinin = "P9"+"_"+str(number)
		#pinout = "P9_"+str(i)

		#pinout = raw_input("GPIO Output Pin to Test (i.e., P8_2): ")
		#print('PINTOUT IS '+pinout)
		#pinin = raw_input("GPIO Input Pin to Test (i.e., P8_3): ")
		print 'PININ IS '+pinin 

		#GPIO.setup(pinout,GPIO.OUT)
		Adafruit_BBIO.GPIO.setup(pinin, Adafruit_BBIO.GPIO.IN)
		#print("Setting "+pinout+" High...")
		#GPIO.output(pinout,GPIO.HIGH)

		if Adafruit_BBIO.GPIO.input(pinin):
		  print pinin + " is HIGH" 
		else:
		  print pinin + " is LOW" 

		time.sleep(3)
		#print("Setting "+pinout+" Low...")
		#GPIO.output(pinout,GPIO.LOW)
		if Adafruit_BBIO.GPIO.input(pinin):
		  print pinin + " is HIGH" 
		else:
		  print pinin + " is LOW" 
		time.sleep(3)
		Adafruit_BBIO.GPIO.cleanup()
		print "Good Bye!" 

		##sudo ntpdate pool.ntp.org
		#import Adafruit_BBIO.GPIO as GPIO
		#import Adafruit_BBIO.PWM as PWM
		#import time
		#GPIO.setup("P8_9",GPIO.OUT)
		#print("Setting P8_9 High...")
		#GPIO.output("P8_9",GPIO.HIGH)
		#time.sleep(3)
		#print("Setting P8_9 Low...")
		#GPIO.output("P8_9",GPIO.LOW)
		#time.sleep(3)
		#GPIO.cleanup()
		#print("Good Bye!")


