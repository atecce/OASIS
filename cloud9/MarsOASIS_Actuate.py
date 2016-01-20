#This script allows toggles the state of individual components and is called from command line as follows:
#$ python MarsOASIS_Actuate.py component On/Off Seconds
#where component is the BBB pin number enabling the component to be actuated.
# eventually we can write a dictionary to type in the component name without referencing the pin
# we can also have arguments that toggle on/off several components

import Adafruit_BBIO.GPIO as GPIO
import sys
import time

def main(argv):
    
    args = len(sys.argv)
    print("Number of Arguments: "+str(args))
    if len(sys.argv)<=1 or len(sys.argv)>4:
         sys.exit("Incorrect number of arguments")
    
    port_id = sys.argv[1] #default status is 'ON', until user interrupts
    print('Component: '+port_id)
    status = 'On'
    duration  = None
    GPIO.setup(port_id,GPIO.OUT)
    
    if len(sys.argv)>2:   #turns component on or off
        status = sys.argv[2]
    
    print('Status: '+status)
        
    if len(sys.argv)>3: #turns component on/off, for set duration in seconds
        duration = float(sys.argv[3])
        print('Duration (seconds): '+str(duration))
        
    if duration is not None:
        if status == 'Off':
            GPIO.output(port_id,GPIO.LOW)
            time.sleep(duration)
        else:
            if status == 'On':
                GPIO.output(port_id,GPIO.HIGH)
                time.sleep(duration)
            else:
                sys.exit("Status Error")
    else:
        if status == 'Off':
            GPIO.output(port_id,GPIO.LOW)
            raw_input("Press any key to continue: ")
        else:
            if status == 'On':
                GPIO.output(port_id,GPIO.HIGH)
                raw_input("Press any key to continue: ")
    

if __name__ == "__main__":
   main(sys.argv[0:])