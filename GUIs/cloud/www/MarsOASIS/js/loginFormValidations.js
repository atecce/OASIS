$(document).ready(function()
{
	var canLogin = false;
	var emailFlag = false;
	var passwordFlag = false;
	// Text change Listeners STart
	$('#login_email').bind("change keyup input",function() 
	{
		var pattern = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		var result = pattern.test(this.value);
		if(result)
		{
			//alert("success");
			canLogin = true;
			emailFlag = true;
			$("#login_email").removeClass("errorText");
			$("#login_email").addClass("successText");
			$('#login_email').css('border-color', 'green');//enableLogin();
		}		
		else
		{
			//alert("failure");
			canLogin = false;
			emailFlag = false;
			$("#login_email").addClass("errorText");
			$("#login_email").removeClass("successText");
			$('#login_email').css('border-color', 'red');
			//disableLogin();
		}		
	});

	//bind("change keyup input",
	$('#login_password').bind("change keyup input",function() 
	{
		var pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;	
		var result = pattern.test(this.value);
		//alert(result+" - "+this.value)
		if(result)
		{
			//alert("success");
			canLogin = true;
			passwordFlag = true;
			$("#login_password").removeClass("errorText");
			$("#login_password").addClass("successText");
			$('#login_password').css('border-color', 'green');//enableLogin();
		}		
		else
		{
			//alert("failure");
			canLogin = false;
			passwordFlag = false;
			$("#login_password").addClass("errorText");
			$("#login_password").removeClass("successText");
			$('#login_password').css('border-color', 'red');
			//disableLogin();
		}
	});
	// Text change Listeners End
	//echo $_SESSION['ERRMSG_ARR'][0];
	
	
	var f1 = 0, f2 = 0, f3 = 0;
	
	function disableLogin()
	{
		$('#login_btn').prop("disabled", true);
	}
	
	function enableLogin()
	{
		$('#login_btn').prop("disabled", false);
	}
	
	$("#login_form").submit(function (e) {
		//e.preventDefault();
		if(!canLogin || !emailFlag || !passwordFlag)
		{
			e.preventDefault();
			//$("#login_form").unbind('submit').submit();
		}
	});
	
	// Login Form Validations
	$('#login_btn').click(function()
	{		
		//initializing variables with form element values
		//$('#login_btn').prop('disabled', true);
		
		var email =  $('#login_email').val();
		var password =  $('#login_password').val();
		//alert(email+" - "+password);
		
		//initializing variables with regular expressions	
	 
		var email_regex = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
		var password_regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/;	
	 
		/* (/^
		(?=.*\d)                //should contain at least one digit
		(?=.*[a-z])             //should contain at least one lower case
		(?=.*[A-Z])             //should contain at least one upper case
		[a-zA-Z0-9]{8,}         //should contain at least 8 from the mentioned characters
		$/)*/

		var email_flag = false;
		var password_flag = false;

		if(email.length == 0)
		{
			$("#login_email").addClass("errorText");
			var h = 0;
			email_flag = true;
			disableLogin();
			$('#login_email_error').text("* Enter the Email ID *"); 
			//this segment displays the validation rule for email
			$('#login_email_error').fadeIn();
			//if(password_flag == false)
				$('#login_email_error').delay(4950).fadeOut('slow');			
			var v = setTimeout(
				function() 
				{
					//$('#login_email_error').fadeOut();
					
					enableLogin();
				}, 6000);
			$("#login_email").focus();
			$('#login_email').css('border-color', 'red');
		}
		
		//  Validating email.
		else if(!email.match(email_regex))
		{
			$("#login_email").addClass("errorText");
			var h = 0;
			email_flag = true;
			disableLogin();
			$('#login_email_error').text("* Incorrect Email Id *");
			//this segment displays the validation rule for email
			$('#login_email_error').fadeIn();
			//if(password_flag == false)
				$('#login_email_error').delay(4950).fadeOut('slow');
			var v = setTimeout(
				function() 
				{
					//$('#login_email_error').fadeOut();
					
					enableLogin();
				}, 6000);
			$("#login_email").focus();
			$('#login_email').css('border-color', 'red');
		}
		
		//  Validating password.
		if(password.length == 0)
		{
			$("#login_password").addClass("errorText");
			var h = 0;
			password_flag = false;
			disableLogin();
			if(email_flag == false)
			{
				$("#login_password").focus();
				
			}
			$('#login_password_error').text("* Enter the Password *"); 
			//this segment displays the validation rule for password
			$('#login_password_error').fadeIn();
			//if(email_flag == false)
				$('#login_password_error').delay(4950).fadeOut('slow');
			if(email_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					//$('#login_password_error').fadeOut();
					
					enableLogin();
				}, 6000);
			}
			$('#login_password').css('border-color', 'red');
		}
		
		//  Validating email field. ( in login : password should be checked with that of db.)
		else if(!password.match(password_regex))
		{
			$("#login_password").addClass("errorText");
			var h = 0;
			password_flag = false;
			disableLogin();
			if(email_flag == false)
			{
				$("#login_password").focus();
				
			}
		  	$('#login_password_error').text("* Password should contain at least\n one digit\n one lower case\n one upper case\n and minimum of 8 characters from the mentioned ones. *");
			//this segment displays the validation rule for password
			$('#login_password_error').fadeIn();
			//if(email_flag == false)
				$('#login_password_error').delay(4950).fadeOut('slow');
			if(email_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					//$('#login_password_error').fadeOut();
					
					enableLogin();
				}, 6000);
			}
			$('#login_password').css('border-color', 'red');
		}
		if(email_flag == false && password_flag == false)
			enableLogin();	
	});	
});

