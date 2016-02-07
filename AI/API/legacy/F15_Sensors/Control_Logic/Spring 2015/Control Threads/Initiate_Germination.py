def Initiate_Germination():
    #Define ports
    P11_port=0; #Main Tank Recirc pump
    P7_port=0; #Air bubbler
    F2_Port=0; #UV Filter
    M6_port=0; #Fan M6
    M6_PWM_port=0;
    M7_port=0; #Fan M7
    M7_PWM_port=0;
    fan_duty_cycle=0;
    P10_port=0; #Humidifier Pump
    P1_port=0; Main Pump P1
    
    #Start the sequence
    mech_ctrl(P11_port,GPIO.HIGH) #Activate Main Tank Recircullation pump P11
    GPIO_set(P7_port,GPIO.HIGH) #Activate P7 Air Bubbler
    GPIO_set(F2_port,GPIO.HIGH) #Activate UV Filter F2
    FAN(M6_port,GPIO.HIGH,M6_PWM_port,fan_duty_cycle) #Activate Fan M6
    AN(M6_port,GPIO.HIGH,M7_PWM_port,fan_duty_cycle) #Activate Fan M7
    mech_ctrl(P10_port,GPIO.HIGH) #Activate Humidifier pump P10
    time.sleep(10)
    mech_ctrl(P10_port,GPIO.LOW) #Deactivate Humidifier pump P10
    #launch threads for both circulation  pumps
    #Launch threads for all the continous monitoring functions
    #Entering Main pump Nutrient and water delivery loop
    mech_ctrl(P1_port,GPIO.HIGH) #Turn on main pump
    HSST_M21=getvalue()
    S105_level=getvalue() #Get Level sensor 1 value
    while not S105<=HSST_M21:
        time.sleep(1SPS) #1SPS
        S105_value=getvalue()
        HSST_M21=getvalue()
        #When controll loop is done get out
    mech_ctrl(P1_port,GPIO.OFF) #Turn OFF main pump

    #Control logic undermined from here
    







# Two functions to be launched as indpendent threads
#NPK1 circulation pump thread
class NPK1_circ(threading.Thread):
    def __init__(global_event):
        threading.Thread.__init__(self)
        self.event=watering_event
        self.event=global_event
        P6_port=0; #NPK1 Circulation pump P6
        
    def run(self):        
        while True:
            self.global_event.wait() # Global stop when flag is cleared
            HSST_J27=getvalue();
            HSST_I27=getvalue();
            mech_ctrl(P6_port,GPIO.HIGH) #Activate NPK1 Circulation Pump P6
            time.sleep(HSST_I27)
            mech_ctrl(P6_port,GPIO.LOW) #Activate NPK1 Circulation Pump P6
            time.sleep(HSST_I27);
            
#NPK2 circulation pump thread
class NPK1_circ(threading.Thread):
    def __init__(global_event):
        threading.Thread.__init__(self)
        self.event=watering_event
        self.event=global_event
        P9_port=0; #NPK1 Circulation pump P9
        
    def run(self):        
        while True:
            self.global_event.wait() # Global stop when flag is cleared
            HSST_J28=getvalue();
            HSST_I28=getvalue();
            mech_ctrl(P9_port,GPIO.HIGH) #Activate NPK1 Circulation Pump P9
            time.sleep(HSST_I28)
            mech_ctrl(P9_port,GPIO.LOW) #Activate NPK1 Circulation Pump P9
            time.sleep(HSST_I28);
            




    






    
    
