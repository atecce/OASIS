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
		<script src="js/jquery.min.js"></script>
		<script src="js/jquery.tools.min.js"></script>
		<script src="js/registerFormValidations.js"></script>
		<link rel="icon" type="image/jpg" href="images/cu.jpg" />
		<link href="css/styles.css" rel="stylesheet" type="text/css" />
		<meta charset="UTF-8">
		<script type="text/javascript">
			$(window).load(function() {
				$(".loader").fadeOut("slow");
				// select all desired input fields and attach tooltips to them
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
				  
			});
			
			function goBack(){
				window.location.href="index.php";
			}
		</script>
	</head>
	<body>
		<div class="loader"></div>
		<br/><br/>
		<div align="center" style="position:relative;">
		<img id="logo" src="images/marsoasistransparent.jpg" />
		<br/><br/>
		<h2>Create New Account</h2>
		<br/>
		<form method="post" id="registration_form" action="register_exec.php">
		   <div class="form-child input_field">
			   <input type="email" class="inputText" placeholder="Email" title="Enter your Email." id="register_email" name="register_email"/>
			   <p class="error" id = "register_email_error"> </p>
		   </div>
		   <div class="form-child input_field">
			   <input type="password" class="inputText" placeholder="Password" title="Must be at least 8 characters. Password should contain <br/> atleast - <br/> 1 UpperCase, <br/> 1 LowerCase & <br/> 1 Number. <br/> Password should be minimum of <br/> 8 characters!" id="register_password" name="register_password"/>
			   <p class="error" id = "register_password_error"> </p>
		   </div>
		   
		   <div class="form-child input_field">
			   <input type="password" class="inputText" placeholder="Confirm Password" title="Confirm Password should match the Password." id="register_password_confirm" name="register_password_confirm"/>
			   <p class="error" id = "register_password_confirm_error"> </p>
		   </div>
		   
		   <div class="form-child input_field">
			   <input id="register_full_name" class="inputText" type="text" placeholder="Full Name" title="Enter your Name." name="register_full_name" />
			   <p class="error" id = "register_full_name_error"> </p>
		   </div>
		   
		   <div class="form-child input_field">
			   <input id="register_phone" class="inputText" name="register_phone" type="text" placeholder="Phone Number" title="Enter your Phone Number." />
			   <p class="error" id = "register_phone_error"> </p>
		   </div>
		   
		   <div class="form-child input_field">
			   <select id="register_dept" class="inputText" title="Select your Department!">
				  <option selected>Select Your Department</option>
				  <option>CU</option>
				  <option>MarsOASIS</option>
				  <option>NASA</option>
				  <option>Autoponics</option>
				  <option>Other</option>
			   </select>
			   <p class="error" id = "register_dept_error"> </p>
			   <!-- get the value of selected dept -->
		   <input type="hidden" style="display:none;" name="register_dept1" id="register_dept_hidden">
		   
			<script>
			  $(document).ready(function() {
			  $("#register_dept").change(function(){
			  //alert($("#register_dept").find(":selected").text());
			  $("#register_dept_hidden").val($("#register_dept").find(":selected").text());	
			  //alert($("#register_dept_hidden").val());
			  });
			  });
			</script>
		   </div>
		   
			<div class="form-child input_field">
				<input type="checkbox" class="inputText" title="You must Agree to the Terms to get Registered!" id="agree_to_terms"></input> I agree to the <a href="#" style="color:blue;">Terms of Service</a> and <a href="#" style="color:blue;">Private Policy</a>
				<p class="error" id = "agree_to_terms_error"> </p>
			</div>
			
			<div class="form-child">
				<input type="button" onclick="location.href='index.php';" value="Go To Login" />
				<input type="submit" id="signUp_btn" value="Sign Up" name="register" />
				<p class="error" id = "signUp_btn_error_msg"></p>
		    </div>
			<?php include 'registerErrorMsgDisplay.php' ?>  		   		  
		</form>
		
		<footer class="footer">
			<marquee><span>MarsOASIS Fall 2015 Team Welcomes You</span></marquee>
			<div id="footer" align="center">
			MarsOASIS © 2015
			</div>
		</footer>
	</div>
		
	</body>
</html>