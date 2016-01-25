<?php
	ob_start();
	session_id('mySessionID'); 
	session_start();
	if(isset($_SESSION['userEmail']) && $_SESSION['userEmail'] != ""  && isset($_SESSION['userLogin']) == "success")
	{		
		
	}
	else
	{
		session_write_close();
		header("Location: ../index.php");
		exit();
	}
?>