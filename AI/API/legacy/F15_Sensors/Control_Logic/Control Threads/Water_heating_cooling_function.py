def water_heat_cool():
    temp_value=gettempvalue()
    HSST_H11=0
    HSST_L11=0
    HSST_Ill=0
    HSST_K11=0
    HSST_J11=0
    while True:
        if temp_value > HSST_L11:
            while temp_value >= HSST_H11:
                mech_ctrl.pump(chiller_port,GPIO.HIGH) #Activate M2 Chiller
                time.sleep(HSST_I11)
                temp_value=gettempvalue() # Get new sensor reading
            mech_ctrl.pump(chiller_port,GPIO.LOW) #Deactivate M2 Chiller
        elif temp < HSST_K11:
            while temp < HSST_K11:
                mech_ctrl.pump(heater_port,GPIO.HIGH) #Activate M1 Heater
                time.sleep(HSST_J11)
                mech_ctrl.pump(heater_port,GPIO.LOW) #Deactivate M1 Heater
                time.sleep(HSST_I11)
                temp_value=gettempvalue() #Get new sensor reading
        else :
            pass
        
        
        
            
            
                

                    
            
            
            
