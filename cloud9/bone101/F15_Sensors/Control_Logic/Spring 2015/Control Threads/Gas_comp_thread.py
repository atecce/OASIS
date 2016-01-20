class Gas_Composition(threading.Thread):
    def __init__(global_event):
        self.global_event=global_event
        threading.Thread.__init__(self)
     

    def run(self):
        while True:
            "Run CO2 Loop"
            self.global_event.wait() # Global stop when flag is cleared
            CO2_value=getco2value()
            CO2_limit=getco2limit()
            HHST_J2=getvalue()
            HHST_I2=getvalue()
            
            while CO2_Value < CO2_limit:
                    if(mech_ctrl.solenoid(port_id,GPIO.HIGH)):
                        time.sleep(HHST_J2)
                        if(mech_ctrl.solenoid(port_id,GPIO.LOW)):
                            time.sleep(HHST_I2)
                    CO2_value=getco2value()
                            
            "Run O2 Loop"
            O2_value=geto2value()
            O2_limit=HSST_L3
            HHST_J3=getvalue()
            HHST_I3=getvalue()

            while O2_Value > O2_limit:                
                if(mech_ctrl.pump(port_id,GPIO.HIGH)): #Activate O2 Concentrator
                    time.sleep(HSST_J3)
                    if(mech_ctrl.pump(port_id,GPIO.LOW)):
                        time.sleep(HSST_I3)
                O2_value=geto2value()

            "Run Total Pressure Loop"
            TP_value=getTPvalue()
            TP_limit=HSST_K4
            HSST_J4=getvalue()
            HSST_I4=getvalue()
            while TP < TP_limit:
                if(mech_ctrl.solenoid(port_id,GPIO.HIGH)): #Activate N2 Solenoid
                    time.sleep(HSST_J4)
                    if(mech_ctrl.solenoid(port_id,GPIO.LOW)):
                        time.sleep(HSST_I4)
                TP_value=getTPvalue()
            time.sleep(undefined)
            
            
                
                        

