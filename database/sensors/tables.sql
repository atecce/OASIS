create table if not exists sensors (

	SysID       int(1) 	 not null,
	SenseID     varchar(15)  not null,
	sensor_type varchar(100) not null,
	units 	    varchar(100) not null,
	primary key (SysID)
);

create table if not exists sensor_data (

	sensor_ID int(1)   not null,
	read_at   datetime not null default now(),
	reading   float    not null,
	primary key (read_at),
	foreign key (sensor_ID) references sensors (SysID)
);
