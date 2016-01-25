# interface with beaglebone - acutators only use
import Adafruit_BBIO.PWM as PWM

# actuator parent class
from actuator import actuator

# child classes for atmo subsystems
class vent_fan1(actuator):
  pass

class vent_fan2(actuator):
  pass

class O2_concentrator(actuator):
  pass

class dehumidifier(actuator):
  pass


class mister(actuator):
  pass

class blue_apple_1(actuator):
  pass

class blue_apple_2(actuator):
  pass

class humidfier_pump(actuator):
  pass

class air_pump(actuator):
  pass

class regulator_CO2(actuator):
  pass

class regulator_N(actuator):
  pass




