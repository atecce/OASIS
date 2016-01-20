import Adafruit_BBIO.ADC as ADC;
ADC.setup();
ADC_CHANNEL="AIN0"; #ADC channel
DO_AIR=0.025; # DO air
DO_WATER=0;
value=ADC.read(ADC_CHANNEL);
value=ADC.read(ADC_CHANNEL);
value=value*1.8;
DO_WATER=(value/DO_AIR)*100;
print DO_WATER


