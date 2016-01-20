import Adafruit_BBIO.GPIO as GPIO
GPIO.setup("P8_33",GPIO.OUT)
GPIO.output("P8_33",GPIO.HIGH)
raw_input("Press any key to exit: ")
