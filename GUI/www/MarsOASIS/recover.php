<?php
	ob_start();
	session_id('mySessionID'); 
	session_start();
	unset($_SESSION['userEmail']);
	unset($_SESSION['userLogin']);	
?>
<html>
	<head>
		<title>Mars OASIS | Reset Password</title>
		<script src="js/jquery.min.js"></script>
		<script src="js/jquery.tools.min.js"></script>
		<script src="js/recoverFormValidations.js"></script>
		<link rel="icon" type="image/jpg" href="images/cu.jpg"></link>
		<link href="css/styles.css" rel="stylesheet" type="text/css">
		<meta charset="UTF-8">
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
			function goBack(){
				window.location.href="index.php";
			}
		</script>
	</head>
	<body>
		<div class="loader"></div>
		<br/><br/>
		<div align="center">
		<img id="logo" src="images/marsoasistransparent.jpg"></img>
		<br/><br/>
		<h2>Forget Password ?</h2>
		<br/>
		<form method="post" id="recover_form" action="recover_exec.php">
			<div class="form-child input_field">
				Enter your email address:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
				<input type="email" class="inputText" placeholder="Email"  title="Enter your Registered Email." id="frgt_pass_email" name="frgt_pass_email"/>
				<p class="error" id = "frgt_pass_email_error"> </p>
			</div>
			<div class="form-child input_field">
				Confirm your email address:
				<input type="email" class="inputText" placeholder="Confirm Email"  title="Confirm your Registered Email." id="frgt_pass_email_confirm" name="frgt_pass_email_confirm" />
				<p class="error" id = "frgt_pass_email_confirm_error"> </p>
			</div>
			<br/><br/>
			<div class="form-child">
			<input type="button" value="Back" onclick="goBack();" />&nbsp;
			
			<input type="submit" value="Get Password" id="frgt_password_btn" name="recover" />
			<p class="error" id = "frgt_password_btn_error_msg"></p>
			</div>
			<?php include 'recoverErrorMsgDisplay.php' ?>
		</form>	
		<footer class="footer">
			<marquee><span>MarsOASIS Fall 2015 Team Welcomes You</span></marquee>
			<div id="footer" align="center">
			MarsOASIS © 2015
			</div>
		</footer>
	</body>
</html>