def VPD_function():
    RH=getRH()
    temp=getTempincentigrade()
    VPD=getvpd()
    HSST_L5=0
    HSST_K5=0
    HSST_J5=0
    HSST_I5=0
    while True
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
            time.sleep(notdefined)

        
        
        
        
