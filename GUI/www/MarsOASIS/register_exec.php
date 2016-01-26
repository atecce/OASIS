<?php
	
// Check, if username session is NOT set then this page will jump to login page
	include 'utils/security.php';
	
	if(isset($_POST['register']))
	{
		session_id('mySessionID'); 
		session_start();		
		$userEmail=$_POST['register_email'];
		$userPassword=$_POST['register_password'];
		$userPasswordConfirm=$_POST['register_password_confirm'];
		$userName=$_POST['register_full_name'];
		$userPhone=$_POST['register_phone']+"";
		$userDept=$_POST['register_dept1'];
		
		
		// Include database connection settings
		
		require_once ('utils/connection.php');
		$con = $GLOBALS['con'];
		// Retrieve username and password from database according to user's input
		
		$emailCount = mysqli_query($con,"SELECT count(email) as total_count from userdetails WHERE email = '$userEmail' ") or exit(mysql_error());
		$emailRow = mysqli_fetch_assoc($con,$emailCount);
		$isUserEmail = $emailRow['total_count'];
		
		$phoneCount = mysqli_query($con,"SELECT count(phone) as total_count from userdetails WHERE phone = '$userPhone' ") or exit(mysql_error());
		$phoneRow = mysqli_fetch_assoc($con,$phoneCount);
		$isUserPhone = $phoneRow['total_count'];
		if($isUserEmail == 0 && $isUserPhone == 0)
		{		
			$userPassword = Security::encrypt($userPassword, "mars_oasis");
			$sql = "INSERT INTO userdetails (id,name,email,password,phone,department)
								  VALUES (null,'".$userName."','".$userEmail."','".$userPassword."','".$userPhone."','".$userDept."')";
			$result = mysqli_query($con,$sql);
			$_SESSION['recoverMsg'] = 'Note: Email : '.$userEmail.' Phone : '.$userPhone;
			if($result)
			{
				//your email adress 
				$emailTo = $userEmail; //"yourmail@yoursite.com";

				//from email adress
				$emailFrom = "xhab.marsoasis@gmail.com"; //"contact@yoursite.com";

				//email subject
				$emailSubject = "Registration Successful - Welcome To MARS OASIS, ".$userName."!";

				$message = "<b>We are happy to have you onboard.!</b>";
				$message .= "<p> Your Account Details : </p>";
				$message .= "<p> Name       : ".$userName." </p>";
				$message .= "<p> Email      : ".$userEmail." </p>";
				$message .= "<p> Phone      : ".$userPhone." </p>";
				$message .= "<p> Department : ".$userDept." </p>";
				$message .= "<i><p>Your credentials are safe with us. </p></i>";
				$message .= "<i><h3>Thanks for being a part of MARS OASIS . :) </p></i>";

				$headers = "MIME-Version: 1.0" . "\r\n"; 
				$headers .= "Content-type:text/html; charset=utf-8" . "\r\n"; 
				$headers .= "From: <$emailFrom>" . "\r\n";

				$retval = mail($emailTo, $emailSubject, $message, $headers);

				if( $retval == true )
				{
					$_SESSION['registerMsg'] = 'Note: Welcome Message been sent to your mail. ';					
				}
				else
				{
					$_SESSION['registerMsg'] = 'Note: Sending Welcome Message to your mail failed. \n Apologies for inconvenience! ';
				}
			}
			else
			{
				$_SESSION['registerMsg'] = 'Note: Could not create an account now for you, '.$userName.'! Please try again later! \n Apologies for inconvenience! ';
			}		
		}			
		else
		{			
			if($isUserEmail != 0 && $isUserPhone == 0)
				$_SESSION['registerMsg'] = 'Note: An account has already been registered with this Email - '.$userEmail.'!';
			if($isUserPhone != 0 && $isUserEmail == 0)
				$_SESSION['registerMsg'] = 'Note: An account has already been registered with this Phone - '.$userPhone.'!';
			if($isUserEmail != 0 && $isUserPhone != 0)
				$_SESSION['registerMsg'] = 'Note: An account has already been registered with this Email & Phone - '.$userEmail.' & '.$userPhone.'!';
		}		
		//echo $_SESSION['msg'];
		session_write_close();
		header("Location: register.php");
		exit();
		
	}

?>
