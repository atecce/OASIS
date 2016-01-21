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
