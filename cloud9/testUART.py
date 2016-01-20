##sudo ntpdate pool.ntp.org
import Adafruit_BBIO.UART as UART
import serial
import time

#P8_37 is UART5 transmit
#P8_38 is UART5 receive
#P9_11 is UART4 receive
#P9_13 is UART4 transmit
#P9_24 is UART1 transmit
#P9_26 is UART1 receive

#cross connect UART5 and UART4, then UART4 and UART1
#connect P8_37 to P9_11
#connect P8_38 to P9_13

#connect P9_11 to P9_24
#connect P9_13 to P9_26

#open up two terminals with 
# minicom -b 9600 -D /dev/ttyO4
# minicom -b 9600 -D /dev/ttyO5

# minicom -b 9600 -D /dev/ttyO4
# minicom -b 9600 -D /dev/ttyO1

#type in terminals to talk to one another




