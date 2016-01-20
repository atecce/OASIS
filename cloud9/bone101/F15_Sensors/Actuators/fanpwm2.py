import Adafruit_BBIO.PWM as PWM
import time

PWM.start("P8_46",100,1000,0) #to start PWM of 100% duty cycle, 1000Hz frequency
#PWM.start("P8_46",50,1000,0) #to start PWM of 50% duty cycle, 1000Hz frequency
#time.sleep(5)
#PWM.start("P8_46")
#PWM.cleanup()