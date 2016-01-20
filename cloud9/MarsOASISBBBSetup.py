 #!/usr/bin/python

from bbio import *  #need to check this library for how it is setting pin mode, with pinMode() function, when GPIO.setup is not releasing pin control
import Adafruit_BBIO.UART as UART

#set pins 8_3 through 8_10, P9_12, P9_19, P9_20, P9_25, P9_28 as GPIO Inputs for sensors TEMP1-TEMP5 and RH/TEMP1 - RH/TEMP3
pinMode(GPIO1_6, INPUT) #TEMP1
pinMode(GPIO1_7, INPUT) #TEMP2
pinMode(GPIO1_2, INPUT) #TEMP3
pinMode(GPIO1_3, INPUT) #TEMP4
pinMode(GPIO2_2, INPUT) #TEMP5
pinMode(GPIO2_3, INPUT) #RH/TEMP1
pinMode(GPIO2_5, INPUT) #RH/TEMP2
pinMode(GPIO2_4, INPUT) #RH/TEMP3

pinMode(GPIO1_28, INPUT)  #3_3VMon
pinMode(GPIO0_13, INPUT)  #LS3_1
pinMode(GPIO0_12, INPUT)  #LS4_1
pinMode(GPIO3_21, INPUT)  #12VMon
pinMode(GPIO3_17, INPUT)  #24VMon

#set GPIO OUTPUT pins, P8_11-P8_12, P8_14-P8_18, P8_20-P8_35, P9_27
pinMode(GPIO1_13, OUTPUT) #HC_En
pinMode(GPIO1_12, OUTPUT) #HC_Sw
pinMode(GPIO0_26, OUTPUT) #OxConEn
pinMode(GPIO1_15, OUTPUT) #LinearActuatorDir
pinMode(GPIO1_14, OUTPUT) #LinearActuatorEn
pinMode(GPIO0_27, OUTPUT) #P01En
pinMode(GPIO2_1, OUTPUT)  #P02En
pinMode(GPIO1_31, OUTPUT) #P03En
pinMode(GPIO1_30, OUTPUT) #P04En
pinMode(GPIO1_5, OUTPUT)  #P05En
pinMode(GPIO1_4, OUTPUT)  #P06En
pinMode(GPIO1_1, OUTPUT)  #P07En
pinMode(GPIO1_0, OUTPUT)  #P08En
pinMode(GPIO1_29, OUTPUT) #P09En
pinMode(GPIO2_22, OUTPUT) #P10En
pinMode(GPIO2_24, OUTPUT) #P11En
pinMode(GPIO2_23, OUTPUT) #P12-DeHumidEn
pinMode(GPIO2_25, OUTPUT) #Sol2En
pinMode(GPIO0_10, OUTPUT) #Sol1En
pinMode(GPIO0_11, OUTPUT) #UVFilterEn
pinMode(GPIO0_9, OUTPUT)  #READY1
pinMode(GPIO2_17, OUTPUT) #SD_DIR_3.3
pinMode(GPIO0_8, OUTPUT)  #SD_ON/OFF_3.3
pinMode(GPIO3_19, OUTPUT)  #READY2

#set UART pins
UART.setup("UART1")
UART.setup("UART4")
UART.setup("UART5")










