# interface with beaglebone - acutators only use
import Adafruit_BBIO.PWM as PWM

# actuator parent class
from actuator import actuator

# child classes for NTR_WTR subsystems

class sediment_filter(actuator):
  pass

class UV_filter(actuator):
  pass

class mesh_filter(actuator):
  pass

class pre_filter_p1(actuator):
  pass

class pre_filter_p8(actuator):
  pass

class reservoir_heater(actuator):
  pass

class reservoir_chiller(actuator):
  pass

class air_stone_bubbler(actuator):
  pass

class pressure_drippers(actuator):
  pass

class main_pump(actuator):
  pass

class fresh_water(actuator):
  pass

class nutrient_pump1(actuator):
  pass

class nutrient_pump2(actuator):
  pass

class pH_down_pump(actuator):
  pass

class nutrient_tank_1_recirculation(actuator):
  pass

class air_pump(actuator):
  pass

class filter_pump(actuator):
  pass

class nutrient_tank_2_recirculation(actuator):
  pass
