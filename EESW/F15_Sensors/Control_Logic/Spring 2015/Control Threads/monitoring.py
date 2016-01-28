""""monitor flow rate from sensing/mixing tank or main tank to growth medium
potential issues : Bad Main Pump, Flow meter or empty sensing/
mixing tank or main tank"""
#incomplete code
def main_pump_flow_monitor():
    P1_port=0;
    HSST_M19=getvalue();
    S110_value=getvalue(); #get main pump low rate
    Pump_status=getmainpumpstatus(P1_port) #write this function doesnot exist
    if S100_value<HSST_M19:
        pass
        raise_flag(P1_flow_rate_low);
"""monitor DO"""
def DO_monitor():
    HSST_K17=getvalue();
    DO_value=getdovalue();
    if DO_value<HSST_K17:
        pass
        raise_flag(DO_low);

"Monitor if main and leachate tank are empty"
def main_leachate_monitor():
    S112_value=getvalue();
    S105_value=getvalue();
    HSST_M22=getvalue();
    HSST_M21=getvalue();
    if (S112_value<HSST_M22)and(S105_value<HSST_M21):
        raise_flag(Potential Overflow)
        
"Monitor Nutrient tank NPK2 level"
def NPK2_monitor():
    S108_value=getvalue() #NPK2 level sensor
    HSST_M25=getvalue()
    if S108_value<HSST_M25:
        raise_flag("Nutrient Tank 2 is low")
    
        
"Monitor Nutrient tank NPK1 level"
def NPK2_monitor():
    S107_value=getvalue() #NPK1 level sensor
    HSST_M25=getvalue()
    if S107_value<HSST_M25:
        raise_flag("Nutrient Tank 1 is low")

"Monitor pH tank"
def pH_monitor():
    S109_value=getvalue() # Get pH tank level sensor value
    HSST_M25=0
    if S109_value<HSST_M25:
        raise_flag("pH Down Tan is low")

"Monitor Main Tank empty"
def main_empty_monitor():
    S105_value=getvalue() #Main tank level sensor 1
    P11_port=0;
    P7_port=0;
    HSST_M21=getvalue();
    if Sl05<HSST_M21:
        raise_flag("Main tank is low");
        mech_ctrl(P11_port,GPIO.LOW) #Deactivate Main Tank Recircullation pump P11
        GPIO_set(P7_port,GPIO.LOW) #Deactivate P7 Air Bubbler
    else:
        mech_ctrl(P11_port,GPIO.HIGH) #Activate Main Tank Recircullation pump P11
        GPIO_set(P7_port,GPIO.HIGH) #Activate P7 Air Bubbler

"Monitor Main Tank overflow"
def main_overflow_monitor():
    HSST_N21=getvalue();
    S105_value=getvalue(); # Main tank level sensor 1
    S113_value=getvalue(); # Main tank level sensor 2
    if (S113_value+S105_value)>HSST_N21:
        raise_flag("Main tank overflowing")

"Monitor condensation tank level"
def condensation_monitor():
    HSST_N26=getvalue();
    S106_value=getvalue(); #Condesnation tank level sensor
    if S106_value>HSST_N26:
        raise_flag("Condensation tank full")
        
"Monitor Drainage flow rate"
#imcomplete code
def drainage_flow_monitor():
    HSST_M19=getvalue();
    P1_port=getvalue(); #Get main pump port
    S111_value=getvalue() # flow meter from growth medium to leachate tank
    #when p1 is activated code missing
    if S111_value<HSST_M19:
        raise_flag("Drainage flow is low")
        
  



    

        
    
    
