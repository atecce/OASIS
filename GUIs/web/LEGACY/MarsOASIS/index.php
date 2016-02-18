<?php
	ob_start();
	session_id('mySessionID'); 
	session_start();
	
	if(isset($_SESSION['userEmail']) && $_SESSION['userEmail'] != ""  && isset($_SESSION['userLogin']) == "success")
	{		
		session_write_close();
		header("Location: pages/dashboard.php");
		exit();
	}
	
	unset($_SESSION['userEmail']);
	unset($_SESSION['userLogin']);	
?>

<html>
	<head>
		<title>Mars OASIS | Login</title>
		<script src="js/jquery.min.js"></script>
		<script src="js/jquery.tools.min.js"></script>
		<link rel="icon" type="image/jpg" href="images/cu.jpg" />
		<link href="css/styles.css" rel="stylesheet" type="text/css" />
		<meta charset="UTF-8">		
		<script src="js/loginFormValidations.js"></script>
		<script type="text/javascript">
			$(window).load(function() {
				$(".loader").fadeOut("slow");
				$(".input_field :input").tooltip({
			 
				  // place tooltip on the right edge
				  position: "center right",
			 
				  // a little tweaking of the position
				  offset: [-2, 10],
			 
				  // use the built-in fadeIn/fadeOut effect
				  effect: "fade",
			 
				  // custom opacity setting
				  opacity: 0.7
			 
				  });
			})
		</script>
			
	</head>
	<body>
		<div class="loader"></div>
		<br/><br/>
		
		<div align="center">
			<img id="logo" src="images/marsoasistransparent.jpg"></img> 
			<br/>
			<h2>Login to your account</h2>
			<form method="post" id="login_form" action="login_exec.php">
				<div class="form-child input_field">
					<input type="text" class="inputText" placeholder="Email" title="Enter your Registered Email." name="login_email" id="login_email"></input><br/>
					<p class="error" id = "login_email_error"> </p>
				</div>
				<div class="form-child input_field">
					<input type="password" class="inputText" placeholder="Password" name="login_password" title="Enter your Password." id="login_password"></input><br/><br/>
					<p class="error" id = "login_password_error"> </p>
				</div>
				<div class="form-child">
					<input type="submit" value="Login" name="login" id="login_btn"/>
					<p class="error" id = "login_btn_error_msg"></p>
				</div>
				<?php include 'loginErrorMsgDisplay.php' ?>
			</form>
		</div>
		
		<table align="center" cellpadding="10">
			<tr>
				<th align="center">Forgot your Password ?</th>
				<th align="center">Don't have an account yet ?</th>
			</tr>
			<tr>
				<td align="center">No worries, click <a href="recover.php" style="color:blue; font-size: 20px">here</a> to reset your password.</td>
				<td align="center"><a href="register.php" style="color:blue; font-size: 20px; text-shadow:none;">Create an account ?</a></td>
			</tr>
		</table>
		
		<footer class="footer">
			<marquee><span>MarsOASIS Fall 2015 Team Welcomes You</span></marquee>
			<div id="footer" align="center">
			MarsOASIS © 2015
			</div>
		</footer>
		
		
	</body>
</html>