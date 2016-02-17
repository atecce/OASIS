import Adafruit_BBIO.PWM as PWM
import time

class PWM:

	def __init__(self, pin):

		self.pin = pin

	def set(self, duty_cycle):

		PWM.start(self.pin, duty_cycle, frequency

PWM.start("P9_16",100,1000,0) #to start PWM of 100% duty cycle, 1000Hz frequency
#PWM.start("P9_16",50,1000,0) #to start PWM of 50% duty cycle, 1000Hz frequency
#time.sleep(5)
#PWM.start("P9_16")
#PWM.cleanup()

PWM.start("P8_45",100,1000,0) #to start PWM of 100% duty cycle, 1000Hz frequency
#PWM.start("P8_45",50,1000,0) #to start PWM of 50% duty cycle, 1000Hz frequency
#time.sleep(5)
#PWM.start("P8_45")
#PWM.cleanup()

PWM.start("P8_46",100,1000,0) #to start PWM of 100% duty cycle, 1000Hz frequency
#PWM.start("P8_46",50,1000,0) #to start PWM of 50% duty cycle, 1000Hz frequency
#time.sleep(5)
#PWM.start("P8_46")
#PWM.cleanup()

LED =  PWM("P9_16")
fan1 = PWM("P9_45")
fan2 = PWM("P9_46")
