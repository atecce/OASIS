class VPD(threading.Thread):
    def __init__(global_event):
        self.global_event=global_event
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.global_event.wait() # Global stop when flag is cleared
            RH=getRH()
            temp=getTempincentigrade()
            VPD=getvpd()
            HSST_L5=global_var.hsst_hash("L5")
            HSST_K5=global_var.hsst_hash("K5")
            HSST_J5=global_var.hsst_hash("J5")
            HSST_I5=global_var.hsst_hash("I5")
            while VPD > HSST_L5:
                mech_ctrl.pump(port_id,GPIO.HIGH) #Activate Humidifier pump P10
                time.sleep(HSST_J5)
                mech_ctrl.pump(port_id,GPIO.LOW) #Deactivate Humidifier pump P10
                time.sleep(HSST_I5)
                RH=getRH()
                temp=getTempincentigrade()
                VPD=getvpd()
            while VPD < HSST_K5:
                mech_ctrl.pump(port_id,GPIO.HIGH) #Activate Dehumidifier M9
                mech_ctrl.pump(port_id,GPIO.HIGH) #Activate Airpump P12
                time.sleep(HSST_J5)
                mech_ctrl.pump(port_id,GPIO.HIGH) #Deactivate Dehumidifier M9
                mech_ctrl.pump(port_id,GPIO.HIGH) #Deactivate Airpump P12
                RH=getRH()
                temp=getTempincentigrade()
                VPD=getvpd()                
            time.sleep(repeat_frequency)
            
def getvpd():
    write code()
    
