

import smbus #import smbus library
import time
import Adafruit_BBIO.UART as UART
import serial
import time
import struct
import Adafruit_BBIO.ADC as ADC;
import cv2

# ec_read function gives the electical conductivity values of the solution.
def ec_read():
    flag=0
    while True:

        try:
            slave_add=0x64;
            #print" in try block1"
            flag=flag+1;
            #print flag
            bus=smbus.SMBus(1) #assign an object to the SMBus class and mention the interface number
            time.sleep(3)
            bus.write_byte(slave_add,0x52) #R
            time.sleep(3)
            results=bus.read_i2c_block_data(slave_add,0x52) #read cal info
            time.sleep(3)
            #print results
            for index, item in enumerate(results):
                if item == 0:
                       end_val = index
                       break
            results = results[1:end_val]
            results_string = ''.join(chr(i) for i in results)
           # #print" in main try"
           # #print results_string



        except Exception:
            if flag >2:
                #print"false"
                return "False"
            else:
                continue;

        #print results_string
        return float(results_string)

#ec_read(0x64)


#do_read function gives the dissolved oxygen values of the solution.

def do_read():
    slave_add=0x61
    flag=0
    while True:

        try:
            #print" in try block1"
            flag=flag+1;
            #print flag
            bus=smbus.SMBus(1) #assign an object to the SMBus class and mention the interface number
            time.sleep(3)
            bus.write_byte(slave_add,0x52) #R
            time.sleep(3)
            results=bus.read_i2c_block_data(slave_add,0x52) #read cal info
            time.sleep(3)
            #print results
            for index, item in enumerate(results):
                if item == 0:
                       end_val = index
                       break
            results = results[1:end_val]
            results_string = ''.join(chr(i) for i in results)
           # #print" in main try"
           # #print results_string



        except Exception:
            if flag >2:
                #print"false"
                return "False"
            else:
                continue;

        #print results_string
        return float(results_string)

#do_read(0x61)  


#ph_read function gives the ph values of the solution.


def ph_read():
    slave_add=0x63
    flag=0
    while True:

        try:
            #print" in try block1"
            flag=flag+1;
            #print flag
            bus=smbus.SMBus(1) #assign an object to the SMBus class and mention the interface number
            time.sleep(3)
            bus.write_byte(slave_add,0x52) #R
            time.sleep(3)
            results=bus.read_i2c_block_data(slave_add,0x52) #read cal info
            time.sleep(3)
            #print results
            for index, item in enumerate(results):
                if item == 0:
                       end_val = index
                       break
            results = results[1:end_val]
            results_string = ''.join(chr(i) for i in results)
           # #print" in main try"
           # #print results_string



        except Exception:
            if flag >2:
                #print"false"
                return "False"
            else:
                continue;

        #print results_string
        return float(results_string)

#ph_read(0x63)

#moisture_read gives the VWC values for the soil

def moisture_read(ADC_CHANNEL):
   flag=0
   while True:
        try:
                ADC.setup();
                flag=flag+1;
                #ADC_CHANNEL="ADC_channel"; #ADC channel
                voltage=ADC.read(ADC_CHANNEL);
                voltage=ADC.read(ADC_CHANNEL);
                voltage=voltage*1.8*2;
        #       #print voltage
                VWC=0
                if (voltage<1.1):
                        VWC=10*voltage-1
                if (voltage>=1.1 and voltage<1.3):
                        VWC=25*voltage-17.5
                if (voltage>=1.3 and voltage<=1.82):
                        VWC=48.08*voltage-47.5
                if (voltage>=1.8 and voltage<=2.2):
                        VWC=26.32*voltage-7.89
                #print VWC
                return float(VWC)


        except Exception:
                if flag>2:
                        #print "flase"
                        return"False"
                else:
                        continue;




#moisture_read("AIN0")


# O2 sensor gives the O2 percent value 

def O2_sensor(ADC_CHANNEL):

    ADC.setup();
    #ADC_CHANNEL="AIN0"; #ADC channel
    voltage=ADC.read(ADC_CHANNEL);
    voltage=ADC.read(ADC_CHANNEL);
    O2_Percent=(voltage/155)*100;
    #print O2_Percent
    return O2_Percent


#O2_sensor(1)

# Liquid level function gives the liquid levels of the solution

def Liquid_level(ADC_CHANNEL):
	ADC.setup();
	#ADC_CHANNEL="AIN0"; #ADC channel
	reading=0
	reading=ADC.read(ADC_CHANNEL);
	reading=ADC.read(ADC_CHANNEL);

	I= (5- (reading*1.8))/4700;

	resistance= (reading*1.8)/I;
	return resistance

	#print resistance

#PAR sensor measures the luminiscence of the light source

def PAR(ADC_CHANNEL):
	ADC.setup();
	value = ADC.read(ADC_CHANNEL)
	value = ADC.read(ADC_CHANNEL)

	PAR_sensor_value = value*1000*5*0.5*1.8
	return PAR_sensor_value

	#print "PAR value: ", PAR_sensor_value, "micro-mol m^-2 s^-1 per mV"
        

          
#camera sensor

def camera():
	cam=cv2.VideoCapture(0)
	ret, frame=cam.read()
	cv2.imwrite("image.jpeg",frame)
	cam.release()
	cv2.destroyAllWindows()


#CO2

def CO2():
        UART.setup("UART1")
	data=[0xfe,0x44,0x00,0x08,0x02,0x9f,0x25]
	d=struct.pack("7B",*data)
	ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
#serial.begin(9600);
#ser.close()
#ser.open()
	time.sleep(1)
	while(ser.inWaiting()==0):
    		ser.write(d)
    		time.sleep(1)
	A=ser.read(ser.inWaiting())
	for c in A:
   		 print ord(c)
