# Outline of the Control Procedure Code

from read_hsst import HSST

# System power initiated

# SET System mode to INITIATING

# RUN SYSTEM Health Checks
#system_health_checks()

# RUN Monitor and Record
#monitor_record()

# RUN Read HSST
hsst = HSST()
print hsst.read('I', 28)
