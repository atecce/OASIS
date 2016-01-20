def Init():
    import Adafruit_BBIO.GPIO as GPIO
    global stepEnableChannel
    stepEnableChannel = "P9_17"
    global stepDirectionChannel
    stepDirectionChannel = "P9_13"
    global stepClockChannel
    stepClockChannel = "P9_15"
    global stepLimitSwitch1
    stepLimitSwitch1 = "P9_11"
    global stepLimitSwitch2
    stepLimitSwitch2 = "P9_12"
    #######Setup GPIOs###############
    GPIO.setup(stepEnableChannel,GPIO.OUT)
    GPIO.setup(stepDirectionChannel,GPIO.OUT)
    GPIO.output(stepEnableChannel,GPIO.LOW)
    GPIO.output(stepDirectionChannel,GPIO.LOW)
    GPIO.setup(stepLimitSwitch1,GPIO.IN)
    GPIO.setup(stepLimitSwitch2,GPIO.IN)
    GPIO.setup(stepClockChannel,GPIO.OUT)
    GPIO.output(stepClockChannel,GPIO.LOW)
    GPIO.add_event_detect(stepLimitSwitch1,GPIO.FALLING)
    GPIO.add_event_detect(stepLimitSwitch2,GPIO.FALLING)
    return

def Step(nSteps,Dir):
#Step(nSteps,Dir) takes nSteps while rotation in a Dir direction.
#Input: nSteps is an integer. Note that 2000 steps = 1 revolution                                   #Dir is an integer with value 1 or 0. If you are facing the motor:
    #     1 is clockwise
    #     0 is counter-clockwise
    ######Import Libraries###########
    import Adafruit_BBIO.GPIO as GPIO
    import Adafruit_BBIO.PWM as PWM
    import time
    #######Calculate Duration of PWM
    limitTripped = 0
    for t in range(0,nSteps/2):
        if GPIO.event_detected(stepLimitSwitch1)|GPIO.event_detected(stepLimitSwitch2):
            if GPIO.input(stepDirectionChannel):
                GPIO.output(stepDirectionChannel,GPIO.LOW)
            else:
                GPIO.output(stepDirectionChannel,GPIO.HIGH)
            limitTripped = 1
            break
        GPIO.output(stepClockChannel,GPIO.HIGH)
        time.sleep(.01)
        GPIO.output(stepClockChannel,GPIO.LOW)
	time.sleep(.01)
    return limitTripped

def GoToLimit(Dir):
#GoToLimit(Dir) rotates in a Dir direction until the bracket hits a limit switch
#Dir is an integer with value 1 or 0. If you are facing the motor:
    #1 is clockwise
    #0 is counter-clockwise
######Import Libraries###########
    import Adafruit_BBIO.GPIO as GPIO
    import Adafruit_BBIO.PWM as PWM
    import time
    dirState = 0
    if Dir:
        GPIO.output(stepDirectionChannel,GPIO.HIGH)
        dirState = 1
    else:
        GPIO.output(stepDirectionChannel,GPIO.LOW)
    PWM.start(stepClockChannel,50,250)
    while not(GPIO.event_detected(stepLimitSwitch1)) and not(GPIO.event_detected(stepLimitSwitch2)):
        time.sleep(0)
    if dirState:
        GPIO.output(stepDirectionChannel,GPIO.LOW)
    else:
        GPIO.output(stepDirectionChannel,GPIO.HIGH)
    time.sleep(.005)
    PWM.stop(stepClockChannel)
