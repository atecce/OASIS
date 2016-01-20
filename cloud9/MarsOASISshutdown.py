import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.PWM as PWM
import os
UART.cleanup()
GPIO.cleanup()
PWM.cleanup()

os.system("shutdown -h now")
