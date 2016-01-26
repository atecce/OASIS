<?php
	ob_start();
	session_id('mySessionID'); 
	session_start();
	unset($_SESSION['userEmail']);
	unset($_SESSION['userLogin']);	
?>
<html>
	<head>
		<title>Mars OASIS | Sign Up</title>
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
		<script src="js/registerFormValidations.js"></script>
		<link rel="icon" type="image/jpg" href="images/cu.jpg" />
		<link href="css/styles.css" rel="stylesheet" type="text/css" />
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
		<meta charset="UTF-8">
		<script type="text/javascript">
			$(window).load(function() {
				$(".loader").fadeOut("slow");
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
		<img id="logo" src="images/marsoasistransparent.jpg" />
		<br/><br/>
		<h2>Create New Account</h2>
		<br/>
		<form method="post" action="register_exec.php">
		   <div class="form-child">
			   <input type="email" placeholder="Email" id="register_email" name="register_email"/>
			   <p class="error" id = "register_email_error"> </p>
		   </div>
		   <div class="form-child">
			   <input type="password" placeholder="Password" id="register_password" name="register_password"/>
			   <p class="error" id = "register_password_error"> </p>
		   </div>
		   
		   <div class="form-child">
			   <input type="password" placeholder="Confirm Password" id="register_password_confirm" name="register_password_confirm"/>
			   <p class="error" id = "register_password_confirm_error"> </p>
		   </div>
		   
		   <div class="form-child">
			   <input id="register_full_name" type="text" placeholder="Full Name" name="register_full_name" />
			   <p class="error" id = "register_full_name_error"> </p>
		   </div>
		   
		   <div class="form-child">
			   <input id="register_phone" name="register_phone" type="text" placeholder="Phone Number" />
			   <p class="error" id = "register_phone_error"> </p>
		   </div>
		   
		   <div class="form-child">
			   <select id="register_dept">
				  <option selected>Select Your Department</option>
				  <option>CU</option>
				  <option>MarsOASIS</option>
				  <option>NASA</option>
				  <option>Autoponics</option>
				  <option>Other</option>
			   </select>
			   <p class="error" id = "register_dept_error"> </p>
			   <!-- get the value of selected dept -->
		   <input type="hidden" name="register_dept1" id="register_dept_hidden">
		   
			<script>
			  $(document).ready(function() {
			  $("#register_dept").change(function(){
			  //alert($("#register_dept").find(":selected").text());
			  $("#register_dept_hidden").val($("#register_dept").find(":selected").text());	
			  alert($("#register_dept_hidden").val());
			  });
			  });
			</script>
		   </div>
		   
		   
				
			
			<div class="form-child">
				<input type="checkbox"/> I agree to the <a href="" style="color:blue;">Terms of Service</a> and <a href="" style="color:blue;">Private Policy</a>
			</div>
			<br><br>
			
			<div class="form-child">
				<input type="button" onclick="location.href='index.php';" value="Go To Login" />
				<input type="submit" id="signUp_btn" value="Sign Up" name="register" />
				<p class="error" id = "signUp_btn_error_msg"></p>
		    </div>
			<?php include 'registerErrorMsgDisplay.php' ?>  		   		  
		</form>
		
    
</div>
		<div><marquee><span>MarsOASIS Fall 2015 Team Welcomes You</span></marquee>
		<div id="footer" align="center">
		MarsOASIS © 2015
		</div></div>
	</body>
</html>