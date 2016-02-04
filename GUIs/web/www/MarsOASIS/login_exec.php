<?php
	
// Check, if username session is NOT set then this page will jump to login page
	include 'utils/security.php';
	
	//Function to sanitize values received from the form. Prevents SQL injection
	function clean($str) {
		$str = @trim($str);
		if(get_magic_quotes_gpc()) {
			$str = stripslashes($str);
		}
		return mysql_real_escape_string($str);
	}
	
	if(isset($_POST['login']))
	{
		session_id('mySessionID'); 
		session_start();		
		$userEmail=$_POST['login_email'];
		$password=$_POST['login_password'];
		$password = Security::encrypt($password, "mars_oasis");
		// Include database connection settings
		
		require_once ('utils/connection.php');
		$con = $GLOBALS['con'];
		
		// Retrieve username and password from database according to user's input
		
		$login = mysqli_query($con,"SELECT * FROM userdetails WHERE email = '$userEmail' and password = '$password'");
		// Check username and password match
		if (mysqli_num_rows($login) == 1)
		{
			$row = mysqli_fetch_assoc($login);
			$_SESSION['department']=$row['department'];
			// Set username session variable
			$_SESSION['userEmail']=$userEmail;
			$_SESSION['userName']=$row['name'];
			$_SESSION['userLogin']="success";
			$_SESSION['ActuatorFlag'] = "false";
			// Jump to secured page
			header("Location: pages/dashboard.php");
			
		}
		else
		{	
			$_SESSION['userLogin']="failure";	
			$count = mysqli_query($con,"SELECT count(email) as total_count from userdetails WHERE email = '$userEmail' ") or exit(mysql_error());
			$row = mysqli_fetch_array($count,MYSQLI_ASSOC);
			$isUser = $row['total_count'];
			//$_SESSION['loginMsg'] = " '$isUser' ";
			if($isUser == 1)
				$_SESSION['loginMsg'] = "Note: Wrong Email and Password combination for : '$userEmail' ";
			else
				$_SESSION['loginMsg'] = "Note: Email does not exist. Create an account Now for : '$userEmail' ";
			//echo $_SESSION['msg'];
			session_write_close();
			header("Location: index.php");
			exit();			
		}		
	}

?>
