import Adafruit_BBIO.ADC as ADC
ADC.setup()
value = ADC.read("P9_40")
value = ADC.read("P9_40")

PAR_sensor_value = value*1000*5*0.5*1.8

print "PAR value: ", PAR_sensor_value, "micro-mol m^-2 s^-1 per mV"
