<?php
		require_once ('../utils/connection.php');		
		$con = $GLOBALS['con'];
		
		//p1,p2,p3,p4,p5,m1,m2,p6,p7,p9,p11,m6,m7,m8,m18,la,st,f1

		$sql = "SELECT * FROM mars ORDER BY id DESC LIMIT 1";
		$result = mysqli_query($con,$sql);

		if (mysqli_num_rows($result) > 0) 
		{
			$row = mysqli_fetch_assoc($result); 
			$start=$row["start"];
			$stop=$row["stop"];
			$json_array['start'] = $start;
			$json_array['stop'] = $stop;
		}
		
		//water_flow_control - p1,p2
		$sql2 = "SELECT * FROM water_flow_control ORDER BY id DESC";
		$result2 = mysqli_query($con,$sql2);

		if (mysqli_num_rows($result2) > 0) 
		{
			while ($row2 = mysqli_fetch_assoc($result2))
			{		
				$actuator = $row2["actuator"];
				$json_array[$actuator] = $row2["current_value"];				
			}	
		}
		//water_conditioning - m1,m2,p3,p4,p5
		$sql2 = "SELECT * FROM water_conditioning ORDER BY id DESC";
		$result2 = mysqli_query($con,$sql2);

		if (mysqli_num_rows($result2) > 0) 
		{
			while ($row2 = mysqli_fetch_assoc($result2))
			{		
				$actuator = $row2["actuator"];
				$json_array[$actuator] = $row2["current_value"];				
			}	
		}
		
		//atmospheric_management - p10,p12,m8,v3,v4,m6,m7
		$sql2 = "SELECT * FROM atmospheric_management ORDER BY id DESC";
		$result2 = mysqli_query($con,$sql2);

		if (mysqli_num_rows($result2) > 0) 
		{
			while ($row2 = mysqli_fetch_assoc($result2))
			{		
				$actuator = $row2["actuator"];
				$json_array[$actuator] = $row2["current_value"];				
			}	
		}
		
		//lighting_and_imagery - la,st,m18
		$sql2 = "SELECT * FROM lighting_and_imagery ORDER BY id DESC";
		$result2 = mysqli_query($con,$sql2);

		if (mysqli_num_rows($result2) > 0) 
		{
			while ($row2 = mysqli_fetch_assoc($result2))
			{		
				$actuator = $row2["actuator"];
				$json_array[$actuator] = $row2["current_value"];				
			}	
		}
		
		//system_maintenance - p11,p7,p6,p9,f1
		$sql2 = "SELECT * FROM system_maintenance ORDER BY id DESC";
		$result2 = mysqli_query($con,$sql2);

		if (mysqli_num_rows($result2) > 0) 
		{
			while ($row2 = mysqli_fetch_assoc($result2))
			{		
				$actuator = $row2["actuator"];
				$json_array[$actuator] = $row2["current_value"];				
			}		
		}
		
		echo json_encode($json_array);
		exit();
		
		
		?>