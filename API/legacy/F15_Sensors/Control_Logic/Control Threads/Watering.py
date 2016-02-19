#dependecies
#Water_heating_cooling_function.py
#Two sleep times undefined and run the loop by the control guy

class Watering_Function(threading.Thread):
    def __init__(global_event):
        self.global_event=global_event
        threading.Thread.__init__(self)
        P1_port=x # or maybe self. we will see
     

    def run(self):
        while True:
            self.global_event.wait() # Global stop when flag is cleared
            HSST_K20=0
            HSST_L20=0
            HSST_M21
            VWC=Get_VWC()
            if VWC < HSST_K20:
                water_heat_cool()
                S105_value=getvalue() # Get S105 sensor value
                while not((VWC>=HSST_L20) or (S105_value < HSST_M21)):
                    mech_ctrl.pump(P1_port,GPIO.HIGH) #Activate Main Pump P1
                    time.sleep(undefined)
                    S105_value=getvalue()
                    VWC=Get_VWC()
                mech_ctrl.pump(P1_port,GPIO.LOW) #Deactivate Main Pump P1
            else:
                pass
            time.sleep(undefined_again)
        
            
            
            
def Get_VWC():
    S208_level=getlevel()
    S209_level=getlevel()
    S2010_level=getlevel()
    S2011_level=getlevel()
    VWC=(S208_level+S209_level+S2010_level+S2011_level)/4
    return vwc
