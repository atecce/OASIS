#Water heating cooling function
import global_var
import Sensors
# Define ports
P1_port="P8_31" #R1_Ch1
chiller_port="P8_33"   #R1_Ch2
heater_port="P8_35"    #R1_Ch3
#Water heating and cooling funciton
def water_heat_cool():
    S103_value=gettempvalue()
    global_var.sensor_hash_table["TEMP_1"]=S103_value
    S105_value=getlevel()
    global_var.sensor_hash_table["LL_1"]=S105_value
    HSST_H11=global_var.hsst_hash("H11")
    HSST_L11=global_var.hsst_hash("L11")
    HSST_I11=global_var.hsst_hash("I11")
    HSST_K11=global_var.hsst_hash("K11")
    HSST_J11=global_var.hsst_hash("Jll")
    HSST_M21=global_var.hsst_hash("M21")
    if S105_value>HSST_M21:        
        #Chiller Loop
        if S103_value > HSST_L11:
            while S103_value >= HSST_H11:
                mech_ctrl.pump(chiller_port,GPIO.HIGH) #Activate M2 Chiller
                time.sleep(60)#Chiller actuation time 60 seconds-not sure
                time.sleep(HSST_I11)#Settling time
                S103_value=gettempvalue() # Get new sensor reading
                global_var.sensor_hash_table["TEMP_1"]=S103_value
            mech_ctrl.pump(chiller_port,GPIO.LOW) #Deactivate M2 Chiller
            
        #Heater Loop    
        elif S103_value < HSST_K11:
            while S103_value < HSST_K11:
                mech_ctrl.pump(heater_port,GPIO.HIGH) #Activate M1 Heater
                time.sleep(HSST_J11)
                mech_ctrl.pump(heater_port,GPIO.LOW) #Deactivate M1 Heater
                time.sleep(HSST_I11)
                S103_value=gettempvalue() #Get new sensor reading
                global_var.sensor_hash_table["TEMP_1"]=S103_value
    else:
        raise_flag()
        
#def Get_VWC():
    # Do after full communication is defined, This comes for BBB2
#Watering Function Thread
class Watering_Function(threading.Thread):
    def __init__(global_event):
        self.global_event=global_event
        threading.Thread.__init__(self,gloabl_event,watering_event):
            self.global_event=gloabl_event();
            self.watering_event=watering_event();
            self.mixing_event=mixing_event();            

    def run(self):
        while True:
            self.global_event.wait() # Global stop when flag is cleared                   
            HSST_K20=global_var.hsst_hash("K20")
            HSST_L20=global_var.hsst_hash("L20")
            HSST_M21=global_var.hsst_hash("M21")
            VWC=Get_VWC()
            if VWC < HSST_K20:
                water_heat_cool()
                S105_value=getvalue() # Get S105 sensor value
                global_var.sensor_hash_table["LL_1"]=S105_value
                while not((VWC>=HSST_L20) or (S105_value < HSST_M21)):
                    gloabl_var.watering_paused=True; #set pause flag to true
                    self.watering_event.wait() # Watering function paused when flag is cleared
                    mech_ctrl.pump(P1_port,GPIO.HIGH) #Activate Main Pump P1
                    time.sleep(undefined)
                    S105_value=getvalue()
                    global_var.sensor_hash_table["LL_1"]=S105_value
                    VWC=Get_VWC()
                mech_ctrl.pump(P1_port,GPIO.LOW) #Deactivate Main Pump P1
            else:
                pass
            time.sleep(undefined_again)

"------------------------------------------------------------------------------------------"
