# needed for testing
import random

# interface with beaglebone - acutators only use
import Adafruit_BBIO.PWM as PWM
from Adafruit_I2C import Adafruit_I2C

class Actuator():
  """ name, pin, range? """
  name  = str()
  pin   = str()
  connection  = str()
  
  input_voltage   = dict()
  flow_rate       = float()
  concentration   = float()
  outlet_pressure = float()
  internal_pressure = float()

  def __init__ (self, name, pin, connection):

    # attributes
    self.name = name
    self.pin = pin
    self.connection = connection
    
    # set up pin - actuators only use GPIO
    if connection == "GPIO": GPIO.setup(pin, GPIO.IN)


  def action(self):

    # perform the particular action for this actuator


# classes for each actuator
class dehumidifier(actuator):
  # dehu class

class aqua_chiller(actuator): 
  # aqua class

class h2O_pump(actuator):
  # h20_pump class

class O2_concentrator(actuator):
  # O2 class

class power_bubbles(actuator):
  # power_bubbles class

class low_volume_pump(actuator):
  # low_volume_pump class

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
