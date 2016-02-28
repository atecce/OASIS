create table if not exists sensors (
	SysID int(1) not null,
	SenseID varchar(15) not null,
	sensor_type varchar(100) not null,
	units varchar(100) not null,
	primary key (SysID)
);

insert into sensors (SysID, SenseID, sensor_type, units) values
 
 	(101, 'EC1', 	     'electrical conductivity', 	      'micro-Siemens per centimeter'),
 	(102, 'pH1',   	     'pH', 		      		      'pH'),
 	(103, 'temp1', 	     'liquid temperature',      	      'celsius'),
 	(104, 'DO',    	     'dissolved oxygen', 	      	      'milligrams per liter'),
 	(105, 'LL1',   	     'liquid level', 	      		      'centimeters'),
 	(106, 'LL2',   	     'liquid level', 	      		      'centimeters'),
 	(107, 'LL3',   	     'liquid level', 	      		      'centimeters'),
 	(108, 'LL4',   	     'liquid level', 	      		      'centimeters'),
 	(109, 'LL5',   	     'liquid level', 	      		      'centimeters'),
 	(110, 'flow_meter1', 'flow meter', 	      		      'gallons per minute'),
 	(111, 'flow_meter2', 'flow meter', 	      		      'gallons per minute'),
 	(112, 'LL6',	     'liquid level', 	      		      'centimeters'),
 	
 	(201, 'temp2',	     'soil temperature', 	      	      'celsius'),
 	(202, 'temp3',	     'soil temperature', 	      	      'celsius'),
 	(203, 'temp4',	     'soil temperature', 	      	      'celsius'),
 	(205, 'EC2',	     'electrical conductivity', 	      'micro-Siemens per centimeter'),
 	(206, 'pH2',	     'pH', 		      		      'pH'),
 	(208, 'MO1',	     'moisture', 		      	      'volumetric water content'),
 	(209, 'MO2',	     'moisture', 		      	      'volumetric water content'),
 	(210, 'MO3',	     'moisture', 		      	      'volumetric water content'),
 	(211, 'MO4',	     'moisture', 		      	      'volumetric water content'),
 	
 	(301, 'RHT1',	     'relative humidity and air temperature', '%, celsius'),
 	(302, 'RHT2',	     'relative humidity and air temperature', '%, celsius'),
 	(303, 'TP1',	     'total pressure', 			      'pascals'),
 	(304, 'O2',	     'oxygen', 				      '%'),
 	(305, 'CO2',	     'carbon dioxide', 			      'parts per-million'),
 	(306, 'PAR1',	     'photosynthetically active radiation',   'micro-mol photons per meters-squared per second'),
 	
 	(401, 'RHT3',	     'relative humidity and air temperature', '%, celsius'),
 	(402, 'TP2',	     'total pressure', 			      'pascals'),
 	(403, 'PAR2',	     'photosynthetically active radiation',   'micro-mol photons per meters-squared per second');
