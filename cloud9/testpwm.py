##sudo ntpdate pool.ntp.org
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

pinout = raw_input("PWM Output Pin to Test (i.e., P8_3): ")
print('PWM Pin is '+pinout)

#syntax is PWM.start(channel, duty=0to100, freq, polarity=0/1)
PWM.start(pinout, 50, 1, 1)
time.sleep(10)
PWM.stop(pinout)
PWM.cleanup()
