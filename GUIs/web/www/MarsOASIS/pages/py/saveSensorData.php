<?php
	require_once ('../../utils/connection.php');
	$con = $GLOBALS['con'];

	$sensor=$_POST['sensor'];
	$value=$_POST['value'];

	$sql1 = "INSERT INTO sensors (id,name,value,timestamp)
								  VALUES (null,'".$sensor."','".$value."',CURRENT_TIMESTAMP)";
	mysqli_query($con,$sql1);//mysql_query($sql);
?>