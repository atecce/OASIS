# needed for testing
import random

# interface with beaglebone - acutators only use
import Adafruit_BBIO.PWM as PWM
from Adafruit_I2C import Adafruit_I2C

class Actuator():
  """ name, pin, connection """
  name  = str()
  pin   = str()
  connection  = str()
  
  input_voltage   = dict()
  flow_rate       = float()
  concentration   = float()
  outlet_pressure = float()
  internal_pressure = float()

  def __init__ (self, name, pin, connection="GPIO"):

    # attributes
    self.name = name
    self.pin = pin
    self.connection = connection
    
    # set up pin - actuators only use GPIO
    if connection == "GPIO": GPIO.setup(pin, GPIO.IN)


  def action(self):

    # perform the particular action for this actuator


class sediment_filter(acuator):

class UV_filter(acuator):

class mesh_filter(acuator):

class pre_filter_p1(acuator):

class pre_filter_p2(acuator):

class reservor_heater(acuator):

class reservoir_chiller(acuator):

class air_stone_bubbler(acuator):

class pressure_compensating_drippers(acuator):

class ventilation_fan_1(acuator):

class ventialation_fan_2(acuator):

class O2_concentrator(acuator):

class dehumidifier(acuator):

class mister(acuator):

class blue_apple_1(acuator):

class blue_apple_2(acuator):

class stepper_motor(acuator):

class bracket(acuator):

class sensor_pole(acuator):

class LED(acuator):

class twenty_movement(acuator):

class main_pump(acuator):

class fresh_H2O_pump(acuator):

class nutrient_dosing_pump(acuator):

class pH_down_dosing_pump(acuator):

class nutrient_tank_1_recirculation_pump(acuator):

class air_pump(acuator):

class filter_pump(acuator):

class nutrient_tank_2_recirculation_pump(acuator):

class humidifier_pump(acuator):

class submers_mix_tank(acuator):

class air_pump_2(acuator):

class regulator_1(acuator):

class regulator_2(acuator):

class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):
class (acuator):


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)


F1 = sediment_filter(self)
F2 = UV_filter(self)
F3 = mesh_filter(self)
F4 = 
F5 = 

M01 = reservoir_heater(self)
M02 = reservoir_chiller(self) 
M03 = air_stone_bubbler(self) 
M05 = pressure_drippers(self) 
M06 = vent_fan1(self) 
M07 = vent_fan2(self)
M08 = O2_concentrator(self) 
M09 = dehumidifier(self) 
M10 = blue_apple_1(self) 
M11 = blue_apple_2(self) 
M12 = 
M15 = 
M16 = 
M17 = 
M18 = 
M19 = 

P01 = 
P02 = 
P03 = 
P04 = 
P05 = 
P06 = 
P07 = 
P08 = 
P09 = 
P10 = 
P11 =
P12 =

R01 = 
R02 = 

T01 =
T02 = 
T03 = 
T04 = 
T05 = 
T06 = 
T07 = 
T08 = 
T09 = 
 
actuator_suite = ()
