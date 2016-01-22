# AIR LOOP

# interface with beaglebone
import Adafruit_BBIO.PWM as PWM

# import actuator class
from actuators import Actuator

# main class
class air_loop(actuator):
  pass

class air_stone_bubbler(air_loop):
  pass

class air_pump(air_loop):
  pass

# mimicing sensors, will probably need more variables here
M03 = air_stone_bubber("M03", None, None) 
P07 = air_pump("P07", None, None) 

airloop_suite = (M03, P07)
