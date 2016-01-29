import mech_ctrl
import time

"CO2 Control loop"
def CO2_control(port_id,CO2_Value,CO2_limit):    
    if CO2_Value < CO2_limit:
        if(mech_ctrl.solenoid(port_id,GPIO.HIGH)):
            time.sleep(0.5)
            if(mech_ctrl.solenoid(port_id,GPIO.LOW)):
                return 'True'
            else:
                return 'False'
        else:
            return 'False'

"O2 Control Loop"

def O2_control(port_id,O2_Value,O2_limit):    
    if O2_Value > O2_limit:
        if(mech_ctrl.pump(port_id,GPIO.HIGH)): #Activate O2 Concentrator
            time.sleep(0.5)
            if(mech_ctrl.pump(port_id,GPIO.LOW)):
                return 'True'
            else:
                return 'False'
        else:
            return 'False'

"Total Pressure Control Loop"

def TP_control(port_id,TP_Value,TP_limit):    
    if TP_Value < TP_limit:
        if(mech_ctrl.solenoid(port_id,GPIO.HIGH)): #Activate N2 Solenoid
            time.sleep(0.5)
            if(mech_ctrl.solenoid(port_id,GPIO.LOW)):
                return 'True'
            else:
                return 'False'
        else:
            return 'False'

                
        
            
        
        
        
        
        
    

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
