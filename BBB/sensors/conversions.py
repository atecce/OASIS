# need this for json file
import json

# returns the SysID when given senseID
senseIDtoSysID = {"EC1":	  101,
	   	  "EC2":	  205,

	   	  "temp1":        103,
	   	  "temp2":	  201,
	   	  "temp3":	  202,
	   	  "temp4":	  203,

	   	  "DO":   	  104,

	   	  "LL1": 	  105,
	   	  "LL2": 	  106,
	   	  "LL3": 	  107,
	   	  "LL4": 	  108,
	   	  "LL5": 	  109,
	   	  "LL6": 	  112,

	   	  "flow_meter1":  110,
	   	  "flow_meter2":  111,

	   	  "pH1":	  102,
	   	  "pH2":	  206,

	   	  "MO1":	  208,
	   	  "MO2":	  209,
	   	  "MO3":	  210,
	   	  "MO4":	  211,

	   	  "RHT1":	  301,
	   	  "RHT2":	  302,
	   	  "RHT3":	  401,

	   	  "TP1":	  303,
	   	  "TP2":	  402,

	   	  "O2":	  	  304,

	   	  "CO2":	  305,

	   	  "PAR1":	  306,
	   	  "PAR2": 	  403}

# returns the sensor type when given SysID
sensor_type = {101: "electrical conductivity",
               102: "pH",
     	       103: "liquid temperature",
     	       104: "dissolved oxygen",
     	       105: "liquid level", 
     	       106: "liquid level",
     	       107: "liquid level",
	       108: "liquid level",
	       109: "liquid level",
	       110: "flow meter",
	       111: "flow meter",
	       112: "liquid level",

	       201: "soil temperature", 
	       202: "soil temperature",
	       203: "soil temperature",
	       205: "electrical conductivity",
	       206: "pH",
	       208: "moisture",
	       209: "moisture",
	       210: "moisture",
	       211: "moisture",

	       301: "relative humidity and air temperature",
	       302: "relative humidity and air temperature",
	       303: "total pressure",
	       304: "oxygen",
	       305: "carbon dioxide",
	       306: "photosynthetically active radiation",

	       401: "relative humidity and air temperature",
	       402: "total pressure",
	       403: "photosynthetically active radiation"}

# dump senseIDtoSysID converter to JSON file
with open('senseIDtoSysID.json', 'w') as jsonfile: json.dump(senseIDtoSysID, jsonfile)

# dump sensor type dictionary to JSON file
with open('sensor_type.json', 'w') as jsonfile: json.dump(sensor_type, jsonfile)
