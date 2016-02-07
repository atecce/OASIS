import Adafruit_BBIO.PWM as PWM
import time

PWM.start("P9_16",100,1000,0) #to start PWM of 100% duty cycle, 1000Hz frequency
#PWM.start("P9_16",50,1000,0) #to start PWM of 50% duty cycle, 1000Hz frequency
#time.sleep(5)
#PWM.start("P9_16")
#PWM.cleanup()