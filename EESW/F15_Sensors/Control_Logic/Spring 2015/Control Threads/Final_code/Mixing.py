#Mixing Process
import threading
import global_var
import Sensors
#implement dual locking mechanism only single event has been coded in
P3_port="P8_39"    #NPK1 pump
P4_port="P8_41"    #NPK2 pump
P2_port="P8_37"    #Condensate Pump
P8_port="P8_45"   #Pre-Filter Pump
P5_port="P8_43"    #ph Pump
S105_Channel="P9_33"
S112_Channel="P9_35"
S113_Channel="P9_37"
S106_Channel="P9_39"
S109_Channel="P9_40"
class Mixing_Process(threading.Thread):
    def __init__(watering_event,global_event):
        threading.Thread.__init__(self)
        self.watering_event=watering_event
        self.global_event=global_event
        
    def run(self):
        pass
        while True:
            self.global_event.wait() # Global stop when flag is cleared
            S112_value=Sensors.Liquid_level(S112_Channel) # T9 S112 level sensor        
            global_var.sensor_hash_table["LL_2"]=S112_value
            S105_value=Sensors.Liquid_level(S105_Channel)
            global_var.sensor_hash_table["LL_1"]=S105_value
            S113_value=Sensors.Liquid_level(S113_Channel)
            global_var.sensor_hash_table["LL_3"]=S113_value
            HSST_N22=global_var.hsst_hash("N22")
            HSST_N21=global_var.hsst_hash("N21")
            while ((S112_value>HSST_N22) and (S105+S113<HSST_N21)):
                self.watering_event.clear() # Stop watering function
                while not global_var.watering_paused: #Wait till the watering function is stopped
                    time.sleep(2)                
                leachate_dump()
                condensation_dump()
                NTR_conditioning()
                pH_Conditioning()
                gloabl_var.watering_paused=False;
                self.watering_event.set() #Resume watering function
                #Recollect all data and start loop again
                Sll2_value=Sensors.Liquid_level(S112_Channel) # T9 S112 level sensor
                global_var.sensor_hash_table["LL_2"]=S112_value
                S105_value=Sensors.Liquid_level(S105_Channel)
                global_var.sensor_hash_table["LL_1"]=S105_value
                S113_value=Sensors.Liquid_level(S113_Channel)
                global_var.sensor_hash_table["LL_3"]=S113_value
                HSST_N22=global_var.hsst_hash("N22")
                HSST_N21=global_var.hsst_hash("N21")
                time.sleep(30) #polling rate double check
            time.sleep(60)#Double check
                


"Condensation Dump Function"
#Incorporate control logic V6
def Condensation_Dump():
    HSST_M26=global_var.hsst_hash("M26");
    S106_value=Sensors.Liquid_level(S106_Channel)
    global_var.sensor_hash_table["LL_4"]=S106_value
    
    if S106_value>HSST_M26:
        while S106_level > HSST_M26:
            mech_ctrl.pump(P2_port,GPIO.HIGH) #Activate Condensation pump P2
            time.sleep(undefined)
            S106_value=Sensors.Liquid_level(S106_Channel)
            global_var.sensor_hash_table["LL_4"]=S106_value
        mech_ctrl.pump(P2_port,GPIO.LOW) #Deactivate Condensation pump P2
        return
    else:
        return
    

"Nutrient Conditioning Function"
def NTR_Conditioning():
    S101_value=Sensors.ec_read()
    global_var.sensor_hash_table["EC_1"]=S101_value
    HSST_K12=global_var.hsst_hash("K12")
    HSST_J12=global_var.hsst_hash("J12")
    HSST_I12=global_var.hsst_hash("I12")
    while S101_value < HSST_K12:
        mech_ctrl.pump(P3_port,GPIO.HIGH) #Activate NTR1 P3
        mech_ctrl.pump(P4_port,GPIO.HIGH) #Activate NTR2 P4
        time.sleep(HSST_J12)
        mech_ctrl.pump(P3_port,GPIO.LOW) #Deactivate NTR1 P3
        mech_ctrl.pump(P4_port,GPIO.LOW) #Deactivate NTR2 P4
        time.sleep(HSST_I12)
        S101_value=Sensors.ec_read()
        global_var.sensor_hash_table["EC_1"]=S101_value
    return

"pH Conditioning Functions"

def pH_Conditioning():
    S109_value=Sensors.ph_read()
    global_var.sensor_hash_table["LL_7"]=S109_value
    HSST_L16=global_var.hsst_hash("L16")
    HSST_J16=global_var.hsst_hash("J16")
    HSST_I16=global_var.hsst_hash("I16")
    while S109_Value > HSST_L16:
        mech_ctrl.pump(P5_port,GPIO.HIGH) # Activate PH Pump P5
        time.sleep(HSST_J16) #Actuation time
        mech_ctrl.pump(P5_port,GPIO.LOW) # Activate PH Pump P5
        time.sleep(HSST_I16) #Settling time
        S109_value=Sensors.ph_read()#Read again and loop over
        global_var.sensor_hash_table["LL_7"]=S109_value
    return
        

"Leachate Dump Function"
def leachate_dump():    
    S112_value=Sensors.Liquid_level(S112_Channel);
    global_var.sensor_hash_table["LL_2"]=S112_value
    S105_value=Sensors.Liquid_level(S105_Channel);
    global_var.sensor_hash_table["LL_1"]=S105_value
    S113_value=Sensors.Liquid_level(S113_Channel);
    global_var.sensor_hash_table["LL_3"]=S113_value
    HSST_M22=global_var.hsst_hash("M22")
    HSST_N21=global_var.hsst_hash("N21")
    mech_ctrl.pump(P8_port,GPIO.HIGH) # Activate Pre-Filter Pump P8
    while not ((S112_value < HSST_M22) or ((S105+S113) > HSST_N21)):        
        S112_value=Sensors.Liquid_level(S112_Channel);
        global_var.sensor_hash_table["LL_2"]=S112_value
        S105_value=Sensors.Liquid_level(S105_Channel);
        global_var.sensor_hash_table["LL_1"]=S105_value
        S113_value=Sensors.Liquid_level(S113_Channel);
        global_var.sensor_hash_table["LL_3"]=S113_value
    mech_ctrl.pump(P8_port,GPIO.LOW) # deactivate Pre-Filter Pump P8
        
        
    
    
    

    
        
    
        
