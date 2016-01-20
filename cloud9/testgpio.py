##sudo ntpdate pool.ntp.org
import Adafruit_BBIO.GPIO as GPIO
import time


pinout = raw_input("GPIO Output Pin to Test (i.e., P8_2): ")
print('PINTOUT IS '+pinout)
pinin = raw_input("GPIO Input Pin to Test (i.e., P8_3): ")
print('PININ IS '+pinin)

GPIO.setup(pinout,GPIO.OUT)
GPIO.setup(pinin, GPIO.IN)
print("Setting "+pinout+" High...")
GPIO.output(pinout,GPIO.HIGH)

if GPIO.input(pinin):
  print(pinin + " is HIGH")
else:
  print(pinin + " is LOW")

time.sleep(3)
print("Setting "+pinout+" Low...")
GPIO.output(pinout,GPIO.LOW)
if GPIO.input(pinin):
  print(pinin + " is HIGH")
else:
  print(pinin + " is LOW")
time.sleep(3)
GPIO.cleanup()
print("Good Bye!")

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
