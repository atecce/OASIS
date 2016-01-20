#P8_13 PWM2B is assigned for the PWM LED control signal
#this function should be called at command line with the following syntax
# python MarsOASIS_LED.py duty frequency polarity
# where duty cycle is from 0-100%, frequency is in Hz, and polarity is either 0 or 1

import sys
import Adafruit_BBIO.PWM as PWM

args = len(sys.argv)
print("Number of Arguments: "+str(args))

if len(sys.argv) !=4:
    sys.exit("Incorrect number of arguments. See commented script for syntax.")


def main(argv):
    dutycycle = int(sys.argv[1])
    frequency = int(sys.argv[2])
    polarity = int(sys.argv[3])
    #syntax is PWM.start(channel, duty=0to100, freq, polarity=0/1)
    PWM.start("P8_13", dutycycle, frequency, polarity)
    raw_input("Press any key to turn off LEDs: ")
    PWM.stop("P8_13")
    PWM.cleanup()

if __name__ == "__main__":
   main(sys.argv[1:])
