class Gas_Composition(threading.Thread):
    def __init__(LED_Intensity,global_event):
        self.global_event=global_event
        threading.Thread.__init__(self)
        self.LED_Intensity=LED_Intensity       
     

    def run(self):
        #PAR_value=getparvalue()
        HSST_I29=0
        HSST
        time=gettime()
        
        while True:
            self.global_event.wait() # Global stop when flag is cleared
            PAR_value=getparvalue()
            if(time==day):
                while True:
                    if PAR_Value < (TargetPAR-5):
                        self.LED_Intensity=self.LED_Intensity+1
                        LED_Strip(self.LED_Intensity)#Set LED Intensity in percentage
                        break #Confirm this and check if continues loop or timed loop
                    elif PAR_Value > (TargetPAR+5):
                        self.LED_Intensity=self.LED_Intensity-1
                        self.LED_Strip(self.LED_Intensity)#Set LED Intensity in percentage
                        break #Confirm this and check if continues loop or timed loop
                    else:
                        break
            else: #Night Time                
                self.LED_Intensity=0
                self.LED_Strip(LED_Intensity)#Set LED Intensity in percentage
            time.sleep(HSST_I29)
                
            
                    
                        
