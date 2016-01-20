" This is the control loop for Heater/Cooling Function"
import mech_control
import time

def control_loop(temp_value,temp_high,temp_low,heater_port,chiller_port):
    if temp_value > temp_high:
        if(mech_ctrl.pump(chiller_port,GPIO.HIGH)): #Activate M2 Chiller
            return 'True'
        else:
            return 'False'
    elif temp_value < temp_low:
        if(mech_ctrl.pump(heater_port,GPIO.HIGH)): #Activate M1 Heater
            return 'True'
        else:
            return 'False'
    else:
        """ This code totally blows! but there is no way to read an
            output port through the Adafruit API so will have to manually
            turn both ports low every time. Total waste of CPU resources"""
        mech_ctrl.pump(chiller_port,GPIO.LOW)#Deactivate M2 Chiller
        mech_ctrl.pump(heater_port,GPIO.LOW)#Deactivate M1 Heater
        
        
    
    
    while temp_value > HSST_H11:
        while temp_value > HSST_H11
        if(mech_ctrl.pump(chiller_port,GPIO.HIGH)): #Activate M2 Chiller
            return 'True'
        else:
            return 'False'
    

        
    
