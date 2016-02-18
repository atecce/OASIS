<?php
	
// Check, if user_name session is NOT set then this page will jump to login page
	include 'utils/security.php';
	
	if(isset($_POST['recover']))
	{
		session_id('mySessionID'); 
		session_start();	
		
		$userEmail=$_POST['frgt_pass_email'];
		$userEmailConfirm=$_POST['frgt_pass_email_confirm'];
		
		// Include database connection settings
		
		require_once ('utils/connection.php');
		$con = $GLOBALS['con'];
		
		// Retrieve username and password from database according to user's input
		if($userEmail == $userEmailConfirm)
		{
			
			$count = mysqli_query($con,"SELECT count(email) as total_count from userdetails WHERE email = '".$userEmail."'") or exit(mysql_error());
			
			$row = $count->fetch_assoc();
			
			$isUser = $row['total_count'];
			//echo "$.is.User. = <br>".$isUser;
			if($isUser == 1)
			{
				$result = mysqli_query($con,"SELECT password from userdetails WHERE email = '$userEmail'");
				$row = mysqli_fetch_assoc($result);
				$password = $row["password"];
				$password = Security::decrypt($password, "mars_oasis");
				//your email adress 
				$emailTo = $userEmail; //"yourmail@yoursite.com";

				//from email adress
				$emailFrom = "xhab.marsoasis@gmail.com"; //"contact@yoursite.com";

				//email subject
				$emailSubject = "Mars Oasis - Support : Account Recovery Mail";

				$message = "<b>Please remember your Password </b> <i>or</i> <b> Keep Password you can remember</b>";
				$message .= "<p>Your password : <b>$password</b> </p>";
				$message .= "<i><p>Your credentials are safe with us. </p></i>";
				$message .= "<i><h3>Thanks for being a part of MARS OASIS . :) </p></i>";

				$headers = "MIME-Version: 1.0" . "\r\n"; 
				$headers .= "Content-type:text/html; charset=utf-8" . "\r\n"; 
				$headers .= "From: <$emailFrom>" . "\r\n";

				$retval = mail($emailTo, $emailSubject, $message, $headers);

				if( $retval == true )
				{
					$_SESSION['recoverMsg'] = 'Note: Password has been sent to your mail. ';
				}
				else
				{
					$_SESSION['recoverMsg'] = 'Note: Sending password to your mail failed. Apologies for inconvenience! ';
				}
				
			}			
			else
				$_SESSION['recoverMsg'] = 'Note: Email does not exist. Create an account Now. ';
			//echo $_SESSION['msg'];
			session_write_close();
			header("Location: recover.php");
			exit();
		}
		else
			$_SESSION['recoverMsg'] = 'Note: Confirm Email should match email. ';
	}
			session_write_close();
			header("Location: recover.php");
			exit();

?>
