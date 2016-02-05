<?php

	header("Content-Type: application/json", true);
		
	$json_array["flag"] = "failure";
	$actuator = $_POST['wc'];
	$value = $_POST['flag'];
	$str = "Hello";

	$output = null; 
	$return = null;
	
	if($actuator == 'p3' || $actuator == 'p4' || $actuator == 'p5'){	
	  if($value == "1"){		
	 	exec('sudo -u root python /var/www/MarsOASIS/pages/py/python_scripts/Operations/Water_Conditioning/'.$actuator.'.py 1', $output, $return);
	  }
	  else if($value == "0"){
	  	exec('sudo -u root python /var/www/MarsOASIS/pages/py/python_scripts/Operations/Water_Conditioning/'.$actuator.'.py 0', $output, $return);
	  }
	}
	else if($actuator == 'm1' || $actuator == 'm2'){
	  if($value == "1"){
		exec('sudo -u root python /var/www/MarsOASIS/pages/py/python_scripts/Operations/Water_Conditioning/'.$actuator.'.py 0', $output, $return);
	  }
	  else if($value == "0"){
		exec('sudo -u root python /var/www/MarsOASIS/pages/py/python_scripts/Operations/Water_Conditioning/'.$actuator.'.py 1', $output, $return);
	  }
	}
	
	//print_r("Output: ".$output); 
	//print_r("Return: ".$return);
	
	require_once ('../../utils/connection.php');
	$con = $GLOBALS['con'];
	
	require_once ('../utils/sessionStart.php');
	$user_id = $_SESSION['userEmail'];
		
	$sql = "SELECT * FROM water_conditioning WHERE actuator = '".$actuator."'";
	if($result = mysqli_query($con,$sql)) //mysql_query($sql);
	{
		$rowcount = mysqli_num_rows($result);
		$str .= " (rowcount) : ".$rowcount;
		if($rowcount == 0)
		{
			$sql1 = "INSERT INTO water_conditioning(id, actuator, current_value, previous_value, current_time_stamp, previous_time_stamp, current_user_id, previous_user_id) VALUES (null,'".$actuator."','".$value."','".$value."',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,'".$user_id."','".$user_id."')";
			$result1 = mysqli_query($con,$sql1);//mysql_query($sql);
			if ($result1) {
				$json_array["flag"] = "success";
			}	
		}
		if($rowcount == 1)
		{
			if($row = mysqli_fetch_assoc($result))
			{
				$previous_time_stamp = $row["current_time_stamp"];
				$previous_user_id = $row["current_user_id"];
				$previous_value = $row["current_value"];
				//$str .= " - ".$previous_time_stamp." - ".$previous_user_id." - ".$previous_value." = ";
				$sql2 = "UPDATE water_conditioning SET current_value='".$value."',previous_value='".$previous_value."',current_time_stamp=CURRENT_TIMESTAMP,previous_time_stamp='".$previous_time_stamp."',current_user_id='".$user_id."',previous_user_id='".$previous_user_id."' WHERE actuator = '".$actuator."'";
				$result2 = mysqli_query($con,$sql2);//mysql_query($sql);
				if ($result2) 
				{
					$json_array["flag"] = "success";
				}
				//$str .= $sql2;
			}
		}
			
	}
	echo json_encode($json_array);
	exit();
		

?>