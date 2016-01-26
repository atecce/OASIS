<?php
	$sensor = $_POST['selectSensor_value'];
	header("Pragma: public");
	header("Expires: 0"); 
	header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
	header("Content-Type: text/x-csv");
	header("Content-Disposition: attachment;filename=\"$sensor.csv\""); 

	// Open the connection
	include("../../utils/connection.php");
	$con = $GLOBALS['con'];

	
	
	$from = $_POST['fromDate'];
	$f = explode("/",$from);
	$from = $f[2]."-".$f[0]."-".$f[1]." 00:00:00";
	
	$to = $_POST['toDate'];
	$t = explode("/",$to);
	$to = $t[2]."-".$t[0]."-".$t[1]." 23:59:59";
	$file = fopen('php://output', 'w');
	//fputcsv($file,array($to,$from));
	
	$query = "SELECT * FROM sensors WHERE name = '$sensor' AND timestamp BETWEEN '$from' AND '$to'";
	//fputcsv($file,array($to,$from,$query));
	//query the database
	//$query = 'SELECT * FROM sensors';
	 fputcsv($file,array("id","name","value","timestamp"));
	if ($rows = mysqli_query($con, $query))
	{
		// loop over the rows, outputting them
		while ($row = mysqli_fetch_assoc($rows))
		{
			fputcsv($file,$row);
		}
		// free result set
		//mysqli_free_result($result);
	} 

?>