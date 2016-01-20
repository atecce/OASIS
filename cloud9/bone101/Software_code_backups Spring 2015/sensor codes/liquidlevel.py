import Adafruit_BBIO.ADC as ADC;
ADC.setup();
ADC_CHANNEL="AIN4"; #ADC channel
RES=3300;
supply_voltage=3.3;
value=ADC.read(ADC_CHANNEL);
value=ADC.read(ADC_CHANNEL);
print "voltage is "
value=value*2
print value
I=(supply_voltage-value)/RES;
resistance=value/I;
resistance=1500-resistance;
print "resistance is "
print resistance
#water_level=-(resistance-1500)/140;
water_level=resistance/140;
#water_level=8-water_level;
print water_level


