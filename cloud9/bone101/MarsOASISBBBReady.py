 #!/usr/bin/python
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

GPIO.setup("P9_27",GPIO.OUT)
GPIO.setup("P8_33",GPIO.OUT)
#Set READY1 HIGH
GPIO.output("P8_33",GPIO.HIGH)
#Set READY2 LOW
GPIO.output("P9_27",GPIO.LOW)  

raw_input("Press any key to disable READY signals")

print('Disaabling READY Signals...')
GPIO.output("P8_33",GPIO.LOW)










