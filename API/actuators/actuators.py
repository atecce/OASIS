# Main file for the actuators suite

# interface with beaglebone - acutators only use
import Adafruit_BBIO.PWM as PWM

# actuator parent class
class actuator():
  """ name, pin, connection """
  name  = str()
  pin   = str()
  connection  = str()
  """ add attributes as we learn more """  
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

    # start general action 


