class actuator {

	public:

		actuator(const char *name, const char *pin) {

			// these are determined at construction
			name = name;
			pin  = pin;
		}

		// This method depends on quite a bit. Depending on the data communication
		// type and the sensor, it will use different libraries and return different 
		// values.
		bool toggle();
};

class EC : public actuator {

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

class pH : public actuator {

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

class temperature : public actuator {

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

class moisture : public actuator {

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

class DO_probe : public actuator {

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

class liquid_level : public actuator {

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

class flow_meter : public actuator {

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

class RH_temp : public actuator {

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

class total_pressure : public actuator {

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

class oxygen : public actuator {

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

class CO2 : public actuator {

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

class light_PAR : public actuator {

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

class camera : public actuator {

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
