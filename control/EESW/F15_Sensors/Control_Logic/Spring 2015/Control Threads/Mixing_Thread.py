#Mixing Process
import threading
#implement dual locking mechanism only single event has been coded in
class Mixing_Process(threading.Thread):
    def __init__(watering_event,global_event):
        threading.Thread.__init__(self)
        #P1_port=x # or maybe self. we will see
        self.event=watering_event
        self.global_event=global_event
        
    def run(self):
        pass
        while True:
            self.global_event.wait() # Global stop when flag is cleared
            Sll2_value=getvalue() # T9 S112 level sensor
            S105_value=getvalue()
            S113_value=getvalue()
            HSST_N22=0
            HSST_N21=0
            while ((S112_value>HSST_N22) and (S105+S113<HSST_N21)):
                self.event.clear() # Stop watering function
                "write code to make sure watering function is fully stopped this is very imp"
                leachate_dump()
                condensation_dump()
                NTR_conditioning()
                pH_Conditioning()
                self.event.set() #Resume watering function
                #Recollect all data and start loop again
                Sll2_value=getvalue() # T9 S112 level sensor
                S105_value=getvalue()
                S113_value=getvalue()
                HSST_N22=0
                HSST_N21=0
                time.sleep(unknown) #polling rate
            time.sleep(unknown)
                


"Condensation Dump Function"
#Incorporate control logic V6
def Condensation_Dump():
    P2_port=x
    HSST_M26=0;
    S106_level=getlevelvalue()
    HSST_M26=getvalue()
    if S106_value>HSST_M26:
        while S106_level > HSST_M26:
            mech_ctrl.pump(P2_port,GPIO.HIGH) #Activate Condensation pump P2
            time.sleep(undefined)
            S106_level=getlevelvalue()
        mech_ctrl.pump(P2_port,GPIO.LOW) #Deactivate Condensation pump P2
        return
    else:
        return
    

"Nutrient Conditioning Function"
def NTR_Conditioning():
    EC_S101_value=getecvalue()
    P1_port=1 #NTR1 P1 pump
    P4_port=1 #NTR2 P4 Pump
    HSST_K12=0
    HSST_J12=0
    HSST_I12=0
    while EC_S101_value < HSST_K12:
        mech_ctrl.pump(P1_port,GPIO.HIGH) #Activate NTR1 P1
        mech_ctrl.pump(P4_port,GPIO.HIGH) #Activate NTR2 P4
        time.sleep(HSST_J12)
        mech_ctrl.pump(P1_port,GPIO.LOW) #Deactivate NTR1 P1
        mech_ctrl.pump(P4_port,GPIO.LOW) #Deactivate NTR2 P4
        time.sleep(HSST_I12)
        EC_S101_value=getecvalue()
    return

"pH Conditioning Functions"

def pH_Conditioning():
    PH_S109_value=getphvalue()
    HSST_L16=0
    HSST_J16=0
    HSST_I16=0
    P5_port=0
    while PH_S109_Value > HSST_L16:
        mech_ctrl.pump(P5_port,GPIO.HIGH) # Activate PH Pump P5
        time.sleep(HSST_J16) #Actuation time
        mech_ctrl.pump(P5_port,GPIO.LOW) # Activate PH Pump P5
        time.sleep(HSST_I16) #Settling time
        PH_S109_value=getphvalue()#Read again and loop over
    return
        

"Leachate Dump Function"
def leachate_dump():
    P8_port=0;
    S112_value=getvalue();
    S105_value=getvalue();
    S113_value=getvalue();
    HSST_M22=0
    HSST_N21=0
    mech_ctrl.pump(P8_port,GPIO.HIGH) # Activate Pre-Filter Pump P8
    while not ((S112_value < HSST_M22) or ((S105+S113) > HSST_N21)):        
        S112_value=getvalue();
        S105_value=getvalue();
        S113_value=getvalue();
    mech_ctrl.pump(P8_port,GPIO.LOW) # deactivate Pre-Filter Pump P8
        
        
    
    
    

    
        
    
        
