<?php 
	if(isset($_SESSION['department']))
	{
		$dept = $_SESSION['department']."";
		if((strcmp($dept,"MarsOASIS") == 0) || (strcmp($dept,"NASA") == 0))
		{
			include 'mars-nav-menu.php';
		}
		else
		{
			include 'others-nav-menu.php';
		}
	}
	else
	{
		include 'others-nav-menu.php';
	}
?>