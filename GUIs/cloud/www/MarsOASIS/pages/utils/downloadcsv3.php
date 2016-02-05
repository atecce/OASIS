<?php
	/*
		used for testing download csv
		http://localhost/MARSOASIS-New/pages/utils/downloadcsv3.php?selectSensor_value=gm_mo&toDate=11/03/2015&fromDate=11/03/2015

		http://localhost/MARSOASIS-New/pages/utils/downloadcsv3.php?selectSensor_value=gm_mo&toDate=11/03/2015&fromDate=11/03/2015
	*/
	$sensor = $_GET['selectSensor_value'];
	header("Pragma: public");
	header("Expires: 0"); 
	header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
	header("Content-Type: text/x-csv");
	header("Content-Disposition: attachment;filename=\"$sensor.csv\""); 
	
	// Open the connection
	include("../../utils/connection.php");
	$con = $GLOBALS['con'];

	
	
	$from = $_GET['fromDate'];
	$f = explode("/",$from);
	$from = $f[2]."-".$f[0]."-".$f[1]." 00:00:00";
	
	$to = $_GET['toDate'];
	$t = explode("/",$to);
	$to = $t[2]."-".$t[0]."-".$t[1]." 23:59:59";
	$file = fopen('php://output', 'w');
	if (strcmp($sensor,"gm_mo") != 0)
	{
		$query = "SELECT * FROM sensors WHERE name = '$sensor' AND timestamp BETWEEN '$from' AND '$to'";
		//query the database
		//$query = 'SELECT * FROM sensors';
		 //echo json_encode(array("id","name","value","timestamp"));
		 fputcsv($file,array("id","name","value","timestamp"));
		 
		if ($rows = mysqli_query($con, $query))
		{
			// loop over the rows, outputting them
			while ($row = mysqli_fetch_assoc($rows))
			{
				//echo nl2br("\n".json_encode($row));
				fputcsv($file,$row);
			}
			// free result set
			//mysqli_free_result($result);
		} 
	}
	else
	{
		$query = "SELECT * FROM sensors WHERE name LIKE 'gm_mo%' AND timestamp BETWEEN '$from' AND '$to'";
		//query the database
		//$query = 'SELECT * FROM sensors';
		fputcsv($file,array("id","name","value","timestamp"));
		 
		 //echo json_encode(array("id","name","value","timestamp"));
		 $stack = array();
		if ($rows = mysqli_query($con, $query))
		{
			// loop over the rows, outputting them
			while ($row = mysqli_fetch_assoc($rows))
			{
				//$row[sensor]
				array_push($stack, $row);
				//echo nl2br("\n".json_encode($row));
			}
			/*
			echo "<pre>";
			print_r($stack);
			echo "</pre>";
			*/
			//echo nl2br("\n\n".$stack."\n");
			$jsonArray = json_encode($stack);
			//2015-11-03 23:50:27
			$date = $stack[0]["timestamp"]."";
			$date = substr($date, 0, 10);
			//echo nl2br("\n\n".$date."\n");
			$datedValues = array();
			$dates = array();
			$i = 0;
			$k = 0;
			foreach ($stack as $value) 
			{
				if(startsWith($value["timestamp"],$date))
				{
					if($i == 0)
					{
						//echo nl2br("\n\n".$date." VALUES : \n");
						$datedValues[$k]["date"] = $date;
						$dates[] = $date;
					}
					$i = 1;
					
					$datedValues[$k][] = array($value["name"], $value["value"]);
					//echo nl2br("\n".$value["name"]." => ".$value["value"]);	
				}
				else
				{
					$i = 0;
					$k = $k+1;
					$date = $value["timestamp"]."";
					$date = substr($date, 0, 10);
				}
			}
			/*
			echo "<pre>";
			print_r($datedValues);
			echo "</pre>";
			*/
			$jsonDatedValues = json_encode($datedValues);
			
			$k = 0;
			foreach($datedValues as $d)
			{
				//echo nl2br("\n\n Date : ".$d["date"]);
				$len = sizeof($d);
				//echo nl2br("\n\n Size : ".$len);
				$mo1 = array();
				$mo2 = array();
				$mo3 = array();
				$mo4 = array();
				for($x = 0; $x < $len-1; $x++)
				{
					//echo nl2br("\n\n Sensor ".($x+1)." : ".$d[$x][0]);
					$currentSensor = $d[$x][0];
					$currentValue = $d[$x][1];
					switch($currentSensor)
					{
						case 'gm_mo1':
										array_push($mo1,$currentValue);
										break;
						case 'gm_mo2':
										array_push($mo2,$currentValue);
										break;
						case 'gm_mo3':
										array_push($mo3,$currentValue);
										break;
						case 'gm_mo4':
										array_push($mo4,$currentValue);
										break;
					}
					//echo nl2br("\n\n Value ".($x+1)." : ".$d[$x][1]);
				}
				//echo nl2br("\n Size : ".sizeof($array));
				$avg_mo1 = $avg_mo2 = $avg_mo3 = $avg_mo4 = 0;
				$l = sizeof($mo1);
				if($l != 0)
				{
					//printArray($mo1);
					$avg_mo1 = array_sum($mo1)/count($mo1);
					//echo nl2br("\n\n Avg(mo1) ".$avg_mo1);
				}
				$l = sizeof($mo2);
				if($l != 0)
				{
					//printArray($mo2);
					$avg_mo2 = array_sum($mo2)/count($mo2);
					//echo nl2br("\n Avg(mo2) ".$avg_mo2);
				}
				$l = sizeof($mo3);
				if($l != 0)
				{
					//printArray($mo3);
					$avg_mo3 = array_sum($mo3)/count($mo3);
					//echo nl2br("\n Avg(mo3) ".$avg_mo3);
				}
				$l = sizeof($mo4);
				if($l != 0)
				{
					//printArray($mo4);
					$avg_mo4 = array_sum($mo4)/count($mo4);
					//echo nl2br("\n Avg(mo4) ".$avg_mo4);
				}
				$avg_mo = ( ($avg_mo1+$avg_mo2+$avg_mo3+$avg_mo4)/4 );
				//echo nl2br("\n\n Avg(mo) ".$avg_mo);
				$row["id"] = $k++;
				$row["name"] = "gm_mo";
				$row["value"] = $avg_mo;
				$row["timestamp"] = $d["date"];
				fputcsv($file,$row);
			}
			
			//echo nl2br("\n\n".$jsonArray);
			//echo nl2br("\n\n".$jsonDatedValues);
			// free result set
			//mysqli_free_result($result);
		} 
	}
	
	function printArray ($array)
	{
		echo "<pre>";
		print_r($array);
		echo "</pre>";
	}
	function startsWith($haystack, $needle) 
	{
		// search backwards starting from haystack length characters from the end
		return $needle === "" || strrpos($haystack, $needle, -strlen($haystack)) !== FALSE;
	}
?>