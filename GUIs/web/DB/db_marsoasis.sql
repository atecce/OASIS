CREATE TABLE IF NOT EXISTS electrical_conductivity (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS ph_and_circuitry (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS liquid_temp (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS do_probe_and_circuitry (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS liquid_level (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS flow_meter_and_circuitry (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS moisture (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS rh_and_air_temp (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS total_pressure (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS liquid_temp (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS O2 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS CO2 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS light (
	id int(11) NOT NULL AUTO_INCREMENT,
	value float(11) NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	unit varchar(128) NOT NULL,
	sensor_type varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS camera (
	id int(11) NOT NULL AUTO_INCREMENT,
	image LONGBLOB NOT NULL,
	time datetime NOT NULL,
	SysID varchar(128) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS user_details (
	id int(11) NOT NULL AUTO_INCREMENT,
	firstName varchar(256) NOT NULL,
	lastName varchar(256) NOT NULL,
	email varchar(256) NOT NULL,
	department varchar(256) NOT NULL,
	password varchar(256) NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS O2_concentration (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS heater (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS chiller (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS light (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS fan1 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS fan2 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump1 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump2 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump3 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump4 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump5 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump6 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump7 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump8 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump9 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump10 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump11 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);

CREATE TABLE IF NOT EXISTS pump12 (
	id int(11) NOT NULL AUTO_INCREMENT,
	value varchar(128) NOT NULL,
	SysID varchar(128) NOT NULL,
	descritption varchar(256) NOT NULL,
	time datetime NOT NULL,
	PRIMARY KEY (id)
	);




