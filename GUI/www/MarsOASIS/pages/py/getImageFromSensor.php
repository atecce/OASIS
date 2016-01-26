<?php

	header("Content-Type: application/json", true);
	
	//echo "Testing Jaffa";
	
	$python = 'C:\\Python27\\python.exe';
	//echo "<br/>Value: ".$_POST['py'];
	
	$filePath = "/var/www/MarsOASIS/pages/py/python_scripts/Camera/ie_camera.py";

	//echo "<br>".$filePath;
	$today = date("l").", ". date("M d, Y").", ".date("H_i_s"); 
	$timestamp = date("l").", ". date("M d, Y").", ".date("H:i:s");	
	//Tuesday, Jun 3, 2015, 10:10:10
	$string = preg_replace('/\s+/', '', $today);
	$today = preg_replace('/,/', '_', $string);
	//Tuesday, Jun 3, 2015, 10:10:10
	// $today = Tuesday_Jun3_2015_10:10:10

	$cmd = "sudo -u root python $filePath $today"; //$today
	//echo "<br>".$cmd;
	exec("$cmd",$output);
	/*
	$python = `python jaffa.py`;
	echo $python;
	*/
	//echo "<br><br> Output: ";
	//echo '<pre>'; print_r($output); echo '</pre>';
	function startsWith($haystack, $needle) 
	{
		// search backwards starting from haystack length characters from the end
		return $needle === "" || strrpos($haystack, $needle, -strlen($haystack)) !== FALSE;
	}
	// ===> after executing py file
	/*
	 * copy the files to gallery folder
	 * and delete the existing images
     */		

		$images = glob("*.jpg");
		$images1 = glob("*.jpeg");
		//echo $images[0];
		//echo $images1[0];
		// Identify directories
		$source = "";
		$destination = "../gallery/";

		if(!is_dir($destination))
		{
			mkdir($destination);
		}
		$flag = false;
		// Cycle through all source images
		foreach ( $images as $file ) {
			//if (in_array($file, array(".",".."))) continue;
			//echo "file value is:".$file;
			//echo PHP_EOL ;
			//echo "source value is:".$source.$file;
			//echo PHP_EOL ;
			//echo "destination value is:".$destination.$file;
			//echo PHP_EOL ;
			// If we copied this successfully, mark it for deletion
			if (copy($source.$file, $destination.$file)) {
				$flag = true;
				$delete[] = $source.$file;
				//echo "copy successful";
				//echo PHP_EOL ;
			}else{
				//echo "copy unsuccessful";
				//echo PHP_EOL ;
			}
		}
		// Cycle through all source images
		foreach ( $images1 as $file ) {
			//if (in_array($file, array(".",".."))) continue;

			// If we copied this successfully, mark it for deletion
			if (copy($source.$file, $destination.$file)) {
				$flag = true;
				$delete[] = $source.$file;
			}
		}
		
		// Delete all successfully-copied images
		if($flag)
		{
			foreach ( $delete as $file )
			{
				unlink( $file );
			}
		}
	/*
	 * copy the files to gallery folder
	 * and delete the existing images
	 * finished
     */
	$json_array['file'] = "IMG_".$today.".jpg";
	$image_name = "IMG_".$today.".jpg";
	if(file_exists("../gallery/"."IMG_".$today.".jpg"))
	{
		require_once ('../../utils/connection.php');
		$con = $GLOBALS['con'];
		$sql = "INSERT INTO image_cache (id,name,timestamp)
		VALUES (null,'".$image_name."','".$timestamp."')";
		mysqli_query($con,$sql);//mysql_query($sql);
		//echo $sql;
	}
	echo json_encode($json_array);
	exit();
	

?>