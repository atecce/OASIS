#include <stdio.h>

struct HSST_table {

	// micro-Siemens per centimeter
	EC_min = 1150
	EC_max = 1250

	// pH
	pH_min = 5.5
	pH_max = 6

	// celsius
	day_temp_min = 23
	day_temp_max = 27

	night_temp_min = 18
	night_temp_max = 22

	soil_temp_min = 15
	soil_temp_max = 20

	water_temp_min = 22
	water_temp_max = 24
		
	// %
	humidity_min = 50
	humidity_max = 70

	// kPA
	pressure_min = 80
	pressure_max = 84

	// ppm
	const float C02_min = 1000
	const float C02_max = 2000

	// micro-mol per meters-squared seconds
	const float PAR_min = 200
	const float PAR_max = 250
};

class sensor {

	public:

		sensor(const char *name, const char *pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}

		// This method depends on quite a bit. Depending on the data communication
		// type and the sensor, it will use different libraries and return different 
		// values.
		float read();
};

class EC : public sensor {

	const char *units	        = "micro-S-cm-l";
	const char *data_comm	        = "I2C";
	const float sensor_range[2]     = {3, 3000};
	const float required_resolution = 1;

	public:

		EC(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class pH : public sensor {

	const char *units	        = "pH";
	const char *data_comm	        = "I2C";
	const float sensor_range[2]     = {2, 12};
	const float required_resolution = .2;

	public:

		pH(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class temperature : public sensor {

	const char *units	        = "C";
	const char *data_comm	        = "one-wire";
	const float sensor_range[2]     = {0, 100};
	const float required_resolution = 1;

	public:

		temperature(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class moisture : public sensor {

	const char *units	        = "%";
	const char *data_comm	        = "ADC-I2C";
	const float sensor_range[2]     = {0, 50};
	const float required_resolution = 1;

	public:

		moisture(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class DO_probe : public sensor {

	const char *units	        = "mg/L";
	const char *data_comm	        = "I2C";
	const float sensor_range[2]     = {0, 15};
	const float required_resolution = .1;

	public:

		DO_probe(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class liquid_level : public sensor {

	const char *units	        = "cm";
	const char *data_comm	        = "ADC-I2C";
	const float sensor_range[2]     = {0, 40.5};
	const float required_resolution = 1.25;

	public:

		liquid_level(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class flow_meter : public sensor {

	const char *units	        = "gpm";
	const char *data_comm	        = "UART";
	const float sensor_range[2]     = {.2, 2};
	const float required_resolution = .05;

	public:

		flow_meter(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class RH_temp : public sensor {

	const char *units	        = "(C, %)";
	const char *data_comm	        = "one-wire";
	const float sensor_range[2]     = {5, 99};
	const float required_resolution = 1;

	public:

		RH_temp(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class total_pressure : public sensor {

	const char *units	        = "kPA";
	const char *data_comm	        = "I2C";
	const float sensor_range[2]     = {30, 110};
	const float required_resolution = 1;

	public:

		total_pressure(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class oxygen : public sensor {

	const char *units	        = "%";
	const char *data_comm	        = "ADC-I2C";
	const float sensor_range[2]     = {0, 100};
	const float required_resolution = 1;

	public:

		oxygen(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class CO2 : public sensor {

	const char *units	        = "ppm";
	const char *data_comm	        = "UART";
	const float sensor_range[2]     = {0, 2000};
	const float required_resolution = 100;

	public:

		CO2(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class light_PAR : public sensor {

	const char *units	        = "micro-mol per meters-squared seconds";
	const char *data_comm	        = "ADC-I2C";
	const float sensor_range[2]     = {0, 2000};
	const float required_resolution = 2;

	public:

		light_PAR(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};

class camera : public sensor {

	const char *units	    = "RGB";
	const char *data_comm	    = "USB";
	const float sensor_range[2] = {1, 255};
	//float required_resolution = "1k0x1k";
	
	public:

		camera(const char *name, const char *pin) 
		: sensor(name, pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}
};
