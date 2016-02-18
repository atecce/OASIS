<?php
	header("Content-Type: application/json", true);
	$sensorDesc = explode("<=>",$_POST['selectSensor_value']);
	$sensor = $sensorDesc[0];
	$fileName = $sensorDesc[1];
	
	// Open the connection
	include("../../utils/connection.php");
	$con = $GLOBALS['con'];

	$from = $_POST['fromDate'];
	$f = explode("/",$from);
	$from = $f[2]."-".$f[0]."-".$f[1]." 00:00:00";
	
	$to = $_POST['toDate'];
	$t = explode("/",$to);
	$to = $t[2]."-".$t[0]."-".$t[1]." 23:59:59";
	
	if (strcmp($sensor,"gm_mo") != 0)
	{
		$query = "SELECT * FROM sensors WHERE name = '$sensor' AND timestamp BETWEEN '$from' AND '$to'";
		//query the database
		//$query = 'SELECT * FROM sensors';
		//echo json_encode(array("id","name","value","timestamp"));
		if ($rows = mysqli_query($con, $query))
		{
			$rowcount = mysqli_num_rows($rows);
			
			if($rowcount > 0)
			{
				$jsonArray['flag'] = "YES";
			}
			else
			{
				$jsonArray['flag'] = "NO";
			}
			mysqli_free_result($rows);
			
			echo json_encode($jsonArray);
			exit();
		} 
	}
	else
	{
		$query = "SELECT * FROM sensors WHERE name LIKE 'gm_mo%' AND timestamp BETWEEN '$from' AND '$to'";
		//query the database
		//$query = 'SELECT * FROM sensors';
		 
		 //echo json_encode(array("id","name","value","timestamp"));
		 $stack = array();
		if ($rows = mysqli_query($con, $query))
		{
			$rowcount = mysqli_num_rows($rows);
			
			if($rowcount > 0)
			{
				$jsonArray['flag'] = "YES";
			}
			else
			{
				$jsonArray['flag'] = "NO";
			}
			mysqli_free_result($rows);
			
			echo json_encode($jsonArray);
			exit();	
		}
	}
?>