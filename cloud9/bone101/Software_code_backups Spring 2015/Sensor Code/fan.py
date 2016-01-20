import Adafruit_BBIO.PWM as PWM
import time
PWM.start("P9_14", 30, 2000, 1)
time.sleep(30)
PWM.stop("P9_14")


