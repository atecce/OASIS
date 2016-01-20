import Adafruit_BBIO.GPIO as GPIO

def setup_GPIO_BB1():
    #Init Beaglebone Black relay port
    try:
        True
        #Relay 1
        GPIO.setup("P8_31", GPIO.OUT)
        GPIO.setup("P8_33", GPIO.OUT)
        GPIO.setup("P8_35", GPIO.OUT)
        GPIO.setup("P8_37", GPIO.OUT)
        GPIO.setup("P8_39", GPIO.OUT)
        GPIO.setup("P8_41", GPIO.OUT)
        GPIO.setup("P8_43", GPIO.OUT)
        GPIO.setup("P8_45", GPIO.OUT)
    except Exception:
        return 'False'
    
def setup_GPIO_BB2():
    #Init Beaglebone Black relay port
    try:
        True
        #Relay 2
        GPIO.setup("P8_31", GPIO.OUT)
        GPIO.setup("P8_33", GPIO.OUT)
        GPIO.setup("P8_35", GPIO.OUT)
        GPIO.setup("P8_37", GPIO.OUT)
        GPIO.setup("P8_39", GPIO.OUT)
        GPIO.setup("P8_41", GPIO.OUT)
        GPIO.setup("P8_43", GPIO.OUT)
        GPIO.setup("P8_45", GPIO.OUT)
        #Relay 3
        GPIO.setup("P8_32", GPIO.OUT)
        GPIO.setup("P8_34", GPIO.OUT)
        GPIO.setup("P8_36", GPIO.OUT)
        GPIO.setup("P8_38", GPIO.OUT)
        GPIO.setup("P8_40", GPIO.OUT)
        GPIO.setup("P8_42", GPIO.OUT)
        GPIO.setup("P8_44", GPIO.OUT)
        GPIO.setup("P8_46", GPIO.OUT)
    except Exception:
        return 'False'

" Not sure if this function is usefull but definetly"
"nice to have"
def cleanup_GPIO():
    try:
        GPIO.cleanup()
        return 'True'
    except Exception:
        return 'False'
    
"This function turns a solenoid ON or OFF"
"This assumes all the GPIO are set up as a part of the init routine"    
def solenoid(port_id,status):
    try:    
        if status=='ON':
            GPIO.output(port_id,GPIO.HIGH)
            return 'True'
        if status=='OFF':
            GPIO.output(port_id,GPIO.LOW)
            return 'True'
        return 'False' #If the status is neither ON/OFF operation Falseed
    except Exception:
        return 'False'
    
"This function turns a Pump ON or OFF"
"This assumes all the GPIO are set up as a part of the init routine"    
def pump(port_id,status):
    try:    
        if status=='ON':
            GPIO.output(port_id,GPIO.HIGH)
            return 'True'
        if status=='OFF':
            GPIO.output(port_id,GPIO.LOW)
            return 'True'
        return 'False' #If the status is neither ON/OFF operation Falseed
    except Exception:
        return 'False'

def GPIO_set(port_id,status):
    try:    
        if status=='ON':
            GPIO.output(port_id,GPIO.HIGH)
            return 'True'
        if status=='OFF':
            GPIO.output(port_id,GPIO.LOW)
            return 'True'
        return 'False' #If the status is neither ON/OFF operation Falseed
    except Exception:
        return 'False'


      
    

