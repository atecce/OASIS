<?php
header("Content-Type: application/json", true);
	// ===> after executing py file
	/*
	 * copy the files to gallery folder
	 * and delete the existing images
     */		

	$imgs = array();
	$dates = array();
	require_once ('../../utils/connection.php');
	$con = $GLOBALS['con'];
	
	$sql = "SELECT * FROM image_cache";
	$result = mysqli_query($con, $sql);

	if (mysqli_num_rows($result) > 0) 
	{
		// output data of each row
		while($row = mysqli_fetch_assoc($result)) 
		{
			$imgs[] = $row["name"];
			$dates[] = $row["timestamp"];
		}
	}
	//echo $images[0];
	//echo $images1[0];
	// Identify directories
	$i = 0;
	$imgs3 = "";
	$dates3 = "";
	for($k = 0; $k < sizeof($imgs); $k++)
	{
		//substr($str, 4);
		//$imgs1[$i++] = substr($image, 3); 
		$i++;
		if($k != sizeof($imgs)-1)
		{			
			$imgs3 .= $imgs[$k]."<=>";
			$dates3 .= $dates[$k]."<=>";
		}
		else
		{	
			$imgs3 .= $imgs[$k];
			$dates3 .= $dates[$k];
		}
	}
	$imgs1["size"] = $i;
	$imgs1["imgs"] = $imgs3;
	
	//printArray($imgs1);
	function printArray ($array)
	{
		echo "<pre>";
		print_r($array);
		echo "</pre>";
	}
	
	
	echo json_encode($imgs1);
	exit();
	

?>