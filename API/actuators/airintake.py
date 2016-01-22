# AIR INTAKE

# interface with beaglebone
import Adafruit_BBIO.PWM as PWM

# import actuator class
from actuators import Actuator

# main and only class (intake valve)
class air_intake(actuator):
  pass

V05 = air_intake("V05", None, None)

air_intake_suite = list()
air_intake_suite = (V05)
