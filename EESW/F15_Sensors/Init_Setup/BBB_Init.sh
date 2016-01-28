#echo BB-TEMP1:00A0 > /sys/devices/bone_capemgr.9/slots
#echo BB-TEMP2:00A0 > /sys/devices/bone_capemgr.9/slots
echo BB-TEMP3:00A0 > /sys/devices/bone_capemgr.9/slots
#echo BB-TEMP4:00A0 > /sys/devices/bone_capemgr.9/slots
#echo BB-TEMP5:00A0 > /sys/devices/bone_capemgr.9/slots

(sleep 5; python /var/lib/cloud9/F15_Sensors/Init_Setup/OUTPUTSetup.py) &
(sleep 5; python /var/lib/cloud9/F15_Sensors/Init_Setup/inputsetup.py) &