CREATE TABLE IF NOT EXISTS 'electrical_conductivity' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'ph_and_circuitry' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'liquid_temp' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'do_probe_and_circuitry' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'liquid_level' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'flow_meter_and_circuitry' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'moisture' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'rh_and_air_temp' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'total_pressure' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'liquid_temp' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'O2' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);
CREATE TABLE IF NOT EXISTS 'CO2' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'light' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'value' float(11) NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	'unit' varchar(128) NOT NULL,
	'sensor_type' varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS 'camera' (
	'id' int(11) NOT NULL AUTO_INCREMENT,
	'image' LONGBLOB NOT NULL,
	'time' datetime NOT NULL,
	'SysID' varchar(128) NOT NULL,
	);










