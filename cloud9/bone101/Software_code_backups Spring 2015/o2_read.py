import Adafruit_BBIO.ADC as ADC;

def O2_sensor(port_ID):
    ADC.setup();
    ADC_CHANNEL="AIN0"; #ADC channel
    voltage=ADC.read(ADC_CHANNEL);
    voltage=ADC.read(ADC_CHANNEL);
    voltage=voltage*1.8
    O2_Percent=(voltage/1860)*100;
    print O2_Percent
    return O2_Percent

O2_sensor("AIN0")
