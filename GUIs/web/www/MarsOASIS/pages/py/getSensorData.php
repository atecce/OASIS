<?php

	header("Content-Type: application/json", true);
	
	//echo "Testing Jaffa";
	//echo "<br/>Value: ".$_POST['var1'];
	$folderPath = "/var/www/MarsOASIS/pages/py/python_scripts/Integrated_Test";
	$pythonPath = "";
	if(startsWith($_POST['var1'],'ee'))
	{
		$pythonPath = $folderPath."/External_Environment/".$_POST['var1'].".py";
	}
	
	if(startsWith($_POST['var1'],'gm'))
	{
		$pythonPath = $folderPath."/Growth_Medium/".$_POST['var1'].".py";
	}
	
	if(startsWith($_POST['var1'],'ie'))
	{
		$pythonPath = $folderPath."/Internal_Environment/".$_POST['var1'].".py";
	}
	
	if(startsWith($_POST['var1'],'ltp'))
	{
		$pythonPath = $folderPath."/Liquid_Tanks_Plumbing/".$_POST['var1'].".py";
	}
	
	//echo "<br>".$pythonPath;
	$cmd = "sudo -u root python $pythonPath";
	//echo "<br>".$cmd;
	exec("$cmd",$output);
	/*
	$python = 'python jaffa.py';
	echo $python;
	*/
	//echo "<br><br> Output: ";
	//echo '<pre>'; print_r($output); echo '</pre>';
	function startsWith($haystack, $needle) 
	{
		// search backwards starting from haystack length characters from the end
		return $needle === "" || strrpos($haystack, $needle, -strlen($haystack)) !== FALSE;
	}
	
	require_once ('../../utils/connection.php');		
		$con = $GLOBALS['con'];
		
		//global $con;
		$sql = "SELECT * FROM sensors where name='".$_POST['var1']."' ORDER BY id DESC LIMIT 1";		
		$result = mysqli_query($con,$sql);

		if (mysqli_num_rows($result) > 0) 
		{
			 $row = mysqli_fetch_assoc($result); 
				 
				$value=$row["value"];
				$timestamp=$row["timestamp"];
				$json_array['value'] = $value;
				$json_array['file'] = $pythonPath;
				$json_array['timestamp'] = $timestamp;
				
				
		}
		else
		{
				$json_array['value'] = "Not Defined";
				$json_array['file'] = $pythonPath;
				$json_array['timestamp'] = "Unknown";
		}
		mysqli_free_result($result);
		
		echo json_encode($json_array);
		exit();
		

?>