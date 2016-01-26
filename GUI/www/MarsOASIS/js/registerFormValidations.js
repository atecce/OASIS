$(document).ready(function() 
{
	
	// Text change Listeners Start
	var canRegister = false;
	$('#register_email').bind('change keyup input', function() 
	{
		var pattern = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		var result = pattern.test($('#register_email').val());
		//alert(result);
		if(result)
		{
			//alert("success");
			canRegister = true;
			$("#register_email").removeClass("errorText");
			$("#register_email").addClass("successText");
			$('#register_email').css('border-color', 'green');
		}
		else
		{
			//alert("failure");
			canRegister = false;
			$("#register_email").addClass("errorText");
			$("#register_email").removeClass("successText");
			$('#register_email').css('border-color', 'red');
		}
	});

	$('#register_password').bind("change keyup input", function() 
	{
		var pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;	
		var result = pattern.test($('#register_password').val());
		if(result)
		{
			//alert("success");
			canRegister = true;
			$("#register_password").removeClass("errorText");
			$("#register_password").addClass("successText");
			$('#register_password').css('border-color', 'green');
		}		
		else
		{
			//alert("failure");
			canRegister = false;
			$("#register_password").addClass("errorText");
			$("#register_password").removeClass("successText");
			$('#register_password').css('border-color', 'red');
		}		
	});

	$('#register_password_confirm').bind("change keyup input", function() 
	{
		var pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;	
		var result = pattern.test($('#register_password_confirm').val());
		if(result && $('#register_password_confirm').val() != "" && ($('#register_password').val() == $('#register_password_confirm').val()))
		{
			//alert("success");
			canRegister = true;
			$("#register_password_confirm").removeClass("errorText");
			$("#register_password_confirm").addClass("successText");
			$('#register_password_confirm').css('border-color', 'green');
		}		
		else
		{
			//alert("failure");
			canRegister = false;
			$("#register_password_confirm").addClass("errorText");
			$("#register_password_confirm").removeClass("successText");
			$('#register_password_confirm').css('border-color', 'red');
		}		
	});

	$('#register_full_name').bind("change keyup input", function() 
	{
		var pattern = /^[a-z ,.'-]+$/i;	
		var result = pattern.test($('#register_full_name').val());
		if(result)
		{
			//alert("success");
			canRegister = true;
			$("#register_full_name").removeClass("errorText");
			$("#register_full_name").addClass("successText");
			$('#register_full_name').css('border-color', 'green');
		}		
		else
		{
			//alert("failure");
			canRegister = false;
			$("#register_full_name").addClass("errorText");
			$("#register_full_name").removeClass("successText");
			$('#register_full_name').css('border-color', 'red');
		}		
	});

	$('#register_phone').bind("change keyup input", function() 
	{
		//var pattern = /[789][0-9]{9}/;	
		var pattern = /[1-9][0-9]{9}/;	
		var result = pattern.test($('#register_phone').val());
		if(result)
		{
			//alert("success");
			canRegister = true;
			$("#register_phone").removeClass("errorText");
			$("#register_phone").addClass("successText");
			$('#register_phone').css('border-color', 'green');
		}		
		else
		{
			//alert("failure");
			canRegister = false;
			$("#register_phone").addClass("errorText");
			$("#register_phone").removeClass("successText");
			$('#register_phone').css('border-color', 'red');
		}		
	});
	// Text change Listeners End
	//echo $_SESSION['ERRMSG_ARR'][0];
	
	$("#registration_form").submit(function (e) {
		//e.preventDefault();
		if(!canRegister)
		{
			e.preventDefault();
			//$("#login_form").unbind('submit').submit();
		}
	});
	
	// SignUp Form Validations
	$('#signUp_btn').click(function(e)
	{
		

		//initializing variables with form element values
		$('#signUp_btn').prop('disabled', true);
		var email =  $('#register_email').val();
		var password =  $('#register_password').val();
		var confirm_password =  $('#register_password_confirm').val();
		var fullName =  $('#register_full_name').val();
		var phone =  $('#register_phone').val();
		var dept =  $('#register_dept').find(":selected").text();
		
		//initializing variables with regular expressions	
	 
		var email_regex = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
		var password_regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;	
		var fullName_regex = /^[a-zA-Z\s]+$/;
		var phone_regex = /[1-9][0-9]{9}/;	
		/* (/^
		(?=.*\d)                //should contain at least one digit
		(?=.*[a-z])             //should contain at least one lower case
		(?=.*[A-Z])             //should contain at least one upper case
		[a-zA-Z0-9]{8,}         //should contain at least 8 from the mentioned characters
		$/)*/

		var email_flag = false;
		var password_flag = false;
		var confirm_password_flag = false;
		var fullName_flag = false;
		var phone_flag = false;
		var dept_flag = false;
		
		//alert(email_flag);
		if(email.length == 0)
		{	
			$("#register_email").addClass("errorText");
			
			email_flag = true;
			//alert(email_flag);
			
			$('#register_email_error').text("* Enter the Email ID *");
			//this segment displays the validation rule for email
			$('#register_email_error').fadeIn();
			
			$('#register_email_error').delay(4950).fadeOut('slow');				
						
			var v = setTimeout(
				function() 
				{				
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			$("#register_email").focus();
			$('#register_email').css('border-color', 'red');
		}
		
		//  Validating email.
		else if(!email.match(email_regex))
		{
			$("#register_email").addClass("errorText");
			email_flag = true;
			
		  	$('#register_email_error').text("* Incorrect Email Id *");
			//this segment displays the validation rule for email
			$('#register_email_error').fadeIn();
			
				$('#register_email_error').delay(4950).fadeOut('slow');				
			
			var v = setTimeout(
				function() 
				{					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			$("#register_email").focus();
			$('#register_email').css('border-color', 'red');
		}
		
		//  Validating password.
		if(password.length == 0)
		{
			$("#register_password").addClass("errorText");
			$('#register_password').css('border-color', 'red');
			
			//alert(email_flag);
			if(email_flag == false)
			{
				$("#register_password").focus();
				password_flag = true;
			}	
			$('#register_password_error').text("* Enter the Password *"); 
			
			//this segment displays the validation rule for password
			$('#register_password_error').fadeIn();
							
				$('#register_password_error').delay(4950).fadeOut('slow');
			if(email_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			}
			
		}
		
		//  Validating email field. ( in login : password should be checked with that of db.)
		else if(!password.match(password_regex))
		{
			$("#register_password").addClass("errorText");
			$('#register_password').css('border-color', 'red');
			
			if(email_flag == false)
			{
				$("#register_password").focus();
				password_flag = true;
			}	
			var msg = "Password should contain at least\n one digit\n one lower case\n one upper case\n and minimum of 8 characters from the mentioned ones.";
		  	$('#register_password_error').text("* "+msg+" *");
			//this segment displays the validation rule for password
			$('#register_password_error').fadeIn();
			$('#register_password_error').delay(4950).fadeOut('slow');
			if(email_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			}
			
		}
		
		//  Validating confirm password.
		//alert("Height : before confirm_password.length == 0 ");
		if(confirm_password.length == 0)
		{
			$("#register_password_confirm").addClass("errorText");
			$('#register_password_confirm').css('border-color', 'red');
			$('#register_password_confirm_error').text("* Confirm Password should not be empty *"); 
			//this segment displays the validation rule for password
			$('#register_password_confirm_error').fadeIn();
			//alert("Height : just after confirm_password.length == 0 ");
			//
			if(email_flag == false && password_flag == false)
			{
				
				$("#register_password_confirm").focus();
				confirm_password_flag = true;
			}	
				
			
			$('#register_password_confirm_error').delay(4950).fadeOut('slow');
			if(email_flag == false && password_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);	
			}
			
		}
		
		//  Validating email field. ( in login : password should be checked with that of db.)
		else if(confirm_password != password)
		{
			$("#register_password_confirm").addClass("errorText");
			$('#register_password_confirm').css('border-color', 'red');
			$('#register_password_confirm_error').text("* Confirm password doesn't match *");
			//this segment displays the validation rule for password
			$('#register_password_confirm_error').fadeIn();
			
		  	if(email_flag == false && password_flag == false)
			{
				$("#register_password_confirm").focus();
				confirm_password_flag = true;
			}	
			
			$('#register_password_confirm_error').delay(4950).fadeOut('slow');
			if(email_flag == false && password_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			}
			
		}
		
		if(fullName.length == 0)
		{
			$("#register_full_name").addClass("errorText");
			$('#register_full_name').css('border-color', 'red');
			$('#register_full_name_error').text("* Full Name should not be empty *"); 
			//this segment displays the validation rule for password
			$('#register_full_name_error').fadeIn();
			//alert("Height : just after confirm_password.length == 0 ");
			//
			if(email_flag == false && password_flag == false && confirm_password_flag == false)
			{
				
				$("#register_full_name").focus();
				fullName_flag = true;
			}	
				
			
			$('#register_full_name_error').delay(4950).fadeOut('slow');
			if(email_flag == false && password_flag == false && confirm_password_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);	
			}
			
		}
		
		//  Validating email field. ( in login : password should be checked with that of db.)
		else if(!fullName.match(fullName_regex))
		{
			
			$("#register_full_name").addClass("errorText");
			$('#register_full_name').css('border-color', 'red');
			$('#register_full_name_error').text("* Enter the Valid Full Name *");
			//this segment displays the validation rule for password
			$('#register_full_name_error').fadeIn();
			
		  	if(email_flag == false && password_flag == false && confirm_password_flag == false)
			{
				$("#register_full_name").focus();
				fullName_flag = true;
			}	
				
			
			$('#register_full_name_error').delay(4950).fadeOut('slow');
			if(email_flag == false && password_flag == false && confirm_password_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			}
			
		}
		
		if(phone.length == 0)
		{
			$("#register_phone").addClass("errorText");
			$('#register_phone').css('border-color', 'red');
			$('#register_phone_error').text("* Phone Number not be empty *"); 
			//this segment displays the validation rule for password
			$('#register_phone_error').fadeIn();
			//alert("Height : just after confirm_password.length == 0 ");
			//
			if(email_flag == false && password_flag == false && confirm_password_flag == false && fullName_flag == false)
			{
				
				$("#register_phone").focus();
				phone_flag = true;
			}	
			$('#register_phone_error').delay(4950).fadeOut('slow');
			if(email_flag == false && password_flag == false && confirm_password_flag == false && fullName_flag == false)
			{
				var v = setTimeout(
				function() 
				{				
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);	
			}
			
		}
		
		//  Validating email field. ( in login : password should be checked with that of db.)
		else if(!phone.match(phone_regex))
		{
			$("#register_phone").addClass("errorText");
			$('#register_phone').css('border-color', 'red');
			$('#register_phone_error').text("* Enter the Valid Phone *");
			//this segment displays the validation rule for password
			$('#register_phone_error').fadeIn();
			
		  	if(email_flag == false && password_flag == false && confirm_password_flag == false && fullName_flag == false)
			{
				$("#register_phone").focus();
				phone_flag = true;
				
			}		
			$('#register_phone_error').delay(4950).fadeOut('slow');
			if(email_flag == false && password_flag == false && confirm_password_flag == false && fullName_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			}
			
		}
		
		if(dept == "Select Your Department")
		{
			$("#register_dept").addClass("errorText");
			//alert(email_flag);
			if(email_flag == false && password_flag == false && confirm_password_flag == false && fullName_flag == false && phone_flag == false)
			{
				$("#register_dept").focus();
				dept_flag = true;
				
			}		
			$('#register_dept_error').text("* Select your department *"); 
			
			//this segment displays the validation rule for password
			$('#register_dept_error').fadeIn();
			$('#register_dept_error').delay(4950).fadeOut('slow');
			if(email_flag == false && password_flag == false && confirm_password_flag == false && fullName_flag == false && phone_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			}
			$('#register_dept').css('border-color', 'red');
		}
		else
		{
			$('#register_dept').css('border-color', 'green');
		}
		
		if(!$("#agree_to_terms").is(":checked"))
		{
			$('#agree_to_terms_error').text("* Please agree to our terms & conditions to get registered! *"); 
			
			//this segment displays the validation rule for password
			$('#agree_to_terms_error').fadeIn();
			$('#agree_to_terms_error').delay(4950).fadeOut('slow');
			f(email_flag == false && password_flag == false && confirm_password_flag == false && fullName_flag == false && dept_flag == false && phone_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					
					$('#signUp_btn').removeAttr('disabled');
				}, 6000);
			}
		}
		
		if(email_flag == false && password_flag == false && confirm_password_flag == false && fullName_flag == false && dept_flag == false && phone_flag == false)
		{
			$('#signUp_btn').removeAttr('disabled');		
		}
			
	});
	
	
});

