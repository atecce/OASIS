<?php
	header("Content-Type: application/json", true);
	require_once ('../../utils/connection.php');
	$con = $GLOBALS['con'];
	
	$sql1 = "SELECT * FROM image_cache ORDER BY id DESC LIMIT 1";
	$result1 = mysqli_query($con,$sql1);

	if (mysqli_num_rows($result1) > 0) 
	{
		$row1 = mysqli_fetch_assoc($result1); 
		$json_array['imgName'] = $row1["name"];
		$json_array['timeStamp'] = $row1["timestamp"];
	}
	else
	{
		$json_array['imgName'] = "nothing";
		$json_array['timeStamp'] = "not found";
	}
	
	mysqli_free_result($result1);
		
	echo json_encode($json_array);
	exit();
?>