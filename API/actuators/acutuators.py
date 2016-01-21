# needed for testing
import random

# interface with beaglebone - acutators only use
import Adafruit_BBIO.PWM as PWM

class Actuator():
  """ name, pin, range? """
  name  = str()
  pin   = str()
  actuator_range = dict()
  connection  = str()

  def __init__ (self, name, pin, connection):

    # attributes
    self.name = name
    self.pin = pin
    self.connection = connection
    
    # set up pin


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
