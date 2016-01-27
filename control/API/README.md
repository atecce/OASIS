# Sensors to be done. Figure out how to get the values returned by these.

UART sensors: 

	S110, S111, S305

I2C or ADC (these overlap, not really clear on which library to use): 

	S105-S109, S112, S208-S211, S304, S306, S403,

I2C only (or not?)

	S101, S104, S102, S205, S206, S303, S402

PWM is for actuators only


Actuators ~RyBo
=========

Looking at the chart, if I'm understanding everything, the
actuators take up a big portion of the lookup table in the API
directory. 

Instead of having a single giant actuator file I think it would be 
best to organize them in seperate files by subsystem. 

Originally I tried to organize them by function type, however I think organizing them by subsystem would be much cleaner.
 
TODO:

    [X] Switch from function type to subsystem
    [ ] Create templates (based off of API/sensors/sensors.py  
    [ ] Add details to each class
