import Adafruit_BBIO.ADC as ADC;
ADC.setup();
ADC_CHANNEL="AIN0"; #ADC channel
voltage=ADC.read(ADC_CHANNEL);
voltage=ADC.read(ADC_CHANNEL);
voltage=voltage*2;
#print voltage
VWC=0
if (voltage<1.1):
	VWC=10*voltage-1
if (voltage>=1.1 and voltage<1.3):
	VWC=25*voltage-17.5
if (voltage>=1.3 and voltage<=1.82):
	VWC=48.08*voltage-47.5
if (voltage>=1.8 and voltage<=2.2):
	VWC=26.32*voltage-7.89

print VWC 

	

	




