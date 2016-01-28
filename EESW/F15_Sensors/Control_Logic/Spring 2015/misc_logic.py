import mech_ctrl
import time
import water_temp
"""Start Page 7"""
"Condensation Dump Function"

def Condensation_Dump(port_id,Level_Value):    
    if level_value <= 0:    #Deactivate condensation pump P2
        if(mech_ctrl.pump(port_id,GPIO.LOW)):
            return 'True'
        else:
            return 'False'
    else: #Activate condensation pump P2
        if(mech_ctrl.pump(port_id,GPIO.HIGH)):
            return 'True'
        else:
            return 'False'

"Nutrient Conditioning Function"
def NTR_Conditioning(port_id,EC_Value,EC_limit,P1_port,P4_port):
    if EC_Value < EC_limit:
        if(mech_ctrl.pump(P1_port,GPIO.HIGH)): #Activate NTR1 P1
            if(mech_ctrl.pump(P4_port,GPIO.HIGH)): #Activate NTR2 P4
                return 'True'
            else:
                return 'False'
        else:
            return 'False'
    else:
        if(mech_ctrl.pump(P1_port,GPIO.LOW)): #Deactivate NTR1 P1
            if(mech_ctrl.pump(P4_port,GPIO.LOW)): #Deactivate NTR2 P4
                return 'True'
            else:
                return 'False'
        else:
            return 'False'
        
    
"pH Conditioning Functions"
def pH_Conditioning(port_id,pH_Value,pH_limit):    
    if pH_value > pH_limit:    #Activate pH pump P5
        if(mech_ctrl.pump(port_id,GPIO.HIGH)):
            return 'True'
        else:
            return 'False'
    else: #Deactivate pH pump P5
        if(mech_ctrl.pump(port_id,GPIO.LOW)):
            return 'True'
        else:
            return 'False'
"Controll loop with continous monitoring""
"Leachate Dump Function"
def lechate_dump(S112_value,S105_value, S113_value,Main_Tank_limit,P8_port):
    if ((S112_value==0) or (S105_value+S113_value > Main_Tank_limit)):
        if(mech_ctrl.pump(P8_port,GPIO.LOW)): #Deactivate P8
            return 'True'
        else:
            return 'False'
    else:
        "Add more logic in future"
        return 'True'
        
"Not done yet will finish up later"

"Page 7 End"

"Page 4 Start"


"Watering Function"
#VWC=Avarage(S208-211)
def Watering(VWC,port_id)


    
