# returns the SysID when given senseID
senseIDtoSysID = {'EC1':	  101,
	   	  'EC2':	  205,

	   	  'temp1':        103,
	   	  'temp2':	  201,
	   	  'temp3':	  202,
	   	  'temp4':	  203,

	   	  'DO':   	  104,

	   	  'LL1': 	  105,
	   	  'LL2': 	  106,
	   	  'LL3': 	  107,
	   	  'LL4': 	  108,
	   	  'LL5': 	  109,
	   	  'LL6': 	  112,

	   	  'flow_meter1':  110,
	   	  'flow_meter2':  111,

	   	  'pH1':	  102,
	   	  'pH2':	  206,

	   	  'MO1':	  208,
	   	  'MO2':	  209,
	   	  'MO3':	  210,
	   	  'MO4':	  211,

	   	  'RHT1':	  301,
	   	  'RHT2':	  302,
	   	  'RHT3':	  401,

	   	  'TP1':	  303,
	   	  'TP2':	  402,

	   	  'O2':	  	  304,

	   	  'CO2':	  305,

	   	  'PAR1':	  306,
	   	  'PAR2': 	  403}

# returns the senseID when given SysID
SysIDtosenseID = {101: 'EC1',
		  102: 'pH1',
	   	  103: 'temp1',
	   	  104: 'DO',
		  105: 'LL1',
		  106: 'LL2',
		  107: 'LL3',
		  108: 'LL4',
		  109: 'LL5',
		  110: 'flow_meter1',
		  111: 'flow_meter2',
		  112: 'LL6',

		  201: 'temp2',
		  202: 'temp3',
		  203: 'temp4',
		  205: 'EC2',
		  206: 'pH2',
		  208: 'MO1',
		  209: 'MO2',
		  210: 'MO3',
		  211: 'MO4',

		  301: 'RHT1',
		  302: 'RHT2',
		  303: 'TP1',
		  304: 'O2',
		  305: 'CO2',
		  306: 'PAR1',

		  401: 'RHT3',
		  402: 'TP2',
		  403: 'PAR2'}

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

# returns the data communication type when given the SysID
data_comm_lookup = {101: "I2C",
		    102: "I2C",
		    103: "one_wire",
		    104: "I2C",
		    105: "ADC",
		    106: "ADC",
		    107: "ADC",
		    108: "ADC",
		    109: "ADC",
		    110: "UART",
		    111: "UART",
		    112: "ADC",

		    201: "one_wire",
		    202: "one_wire",
		    203: "one_wire",
		    205: "I2C",
		    206: "I2C",
		    208: "ADC",
		    209: "ADC",
		    210: "ADC",
		    211: "ADC",

		    301: "one_wire",
		    302: "one_wire",
		    303: "I2C",
		    304: "ADC",
		    305: "UART",
		    306: "ADC",

		    401: "one_wire",
		    402: "I2C",
		    403: "ADC"}
