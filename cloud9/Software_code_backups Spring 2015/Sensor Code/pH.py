import Adafruit.BBIO.ADC as ADC
ADC.setup()

value = ADC.read("P9_40")
value = ADC.read("P9_40")

print value
