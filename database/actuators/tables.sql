create table if not exists actuators (

	SysID         int(1) 	   not null,
	ActID         varchar(15)  not null,
	actuator_type varchar(100) not null,

	primary key (SysID)
);

create table if not exists sensor_data (

	ID  	   int(1)   not null,
	changed_at datetime not null default now(),
	reading    bool     not null,

	primary key (changed_at),
	foreign key (ID) references actuators (ActID)
);
