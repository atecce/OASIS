$(document).ready(function()
{
	// Text change Listeners Start
	var forgot_pass_flag = false;
	
	$('#frgt_pass_email').bind("change keyup input", function() 
	{
		var pattern = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		var result = pattern.test($('#frgt_pass_email').val());
		if(result)
		{
			//alert("success");
			forgot_pass_flag = true;
			$("#frgt_pass_email").removeClass("errorText");
			$("#frgt_pass_email").addClass("successText");
			$('#frgt_pass_email').css('border-color', 'green');
		}		
		else
		{
			//alert("failure");
			forgot_pass_flag = false;
			$("#frgt_pass_email").addClass("errorText");
			$("#frgt_pass_email").removeClass("successText");
			$('#frgt_pass_email').css('border-color', 'red');
		}		
	});

	$('#frgt_pass_email_confirm').bind("change keyup input", function() 
	{
		var pattern = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
		var email = $('#frgt_pass_email').val();
		var confirm_email = $('#frgt_pass_email_confirm').val();
		var result = pattern.test(confirm_email);
		frgt_pass_email_confirm
		if(confirm_email != "" && confirm_email == email && result)
		{
			//alert("success");
			forgot_pass_flag = true;
			$("#frgt_pass_email_confirm").removeClass("errorText");
			$("#frgt_pass_email_confirm").addClass("successText");
			$('#frgt_pass_email_confirm').css('border-color', 'green');
		}		
		else
		{
			//alert("failure");
			forgot_pass_flag = false;
			$("#frgt_pass_email_confirm").addClass("errorText");
			$("#frgt_pass_email_confirm").removeClass("successText");
			$('#frgt_pass_email_confirm').css('border-color', 'red');
		}		
	});
	// Text change Listeners End
	//echo $_SESSION['ERRMSG_ARR'][0];
	
	$("#recover_form").submit(function (e) {
		//e.preventDefault();
		if(!forgot_pass_flag)
		{
			e.preventDefault();
			//$("#login_form").unbind('submit').submit();
		}
	});
	
	var f1 = 0, f2 = 0, f3 = 0;
	
	$('#frgt_password_btn').click(function(e)
	{

		//initializing variables with form element values
		$('#frgt_password_btn').prop('disabled', true);
		var email =  $('#frgt_pass_email').val();
		var confirm_email =  $('#frgt_pass_email_confirm').val();
		
		//initializing variables with regular expressions	
	 
		var email_regex = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;			
	 
		var email_flag = false;
		var confirm_email_flag = false;

		if(email.length == 0)
		{
			$("#frgt_pass_email").addClass("errorText");
			var h = 0;
			email_flag = true;
			
			$('#frgt_pass_email_error').text("* Enter the Email ID *"); 
			//this segment displays the validation rule for email
			//alert("Height : "+height);
			$('#frgt_pass_email_error').fadeIn();
			$('#frgt_pass_email_error').delay(4950).fadeOut('slow');
			//alert("Height : "+height);
			var v = setTimeout(
				function() 
				{
					//alert("Height : "+height);
					$('#frgt_password_btn').removeAttr('disabled');
				}, 4950);
			$("#frgt_pass_email").focus();
			$('#frgt_pass_email').css('border-color', 'red');
		}
		
		//  Validating email.
		else if(!email.match(email_regex))
		{
			$("#frgt_pass_email").addClass("errorText");
			var h = 0;
			email_flag = true;
			
		  	$('#frgt_pass_email_error').text("* Incorrect Email Id *");
			//this segment displays the validation rule for email
			$('#frgt_pass_email_error').fadeIn();
			$('#frgt_pass_email_error').delay(4950).fadeOut('slow');
			var v = setTimeout(
				function() 
				{
					$('#frgt_password_btn').removeAttr('disabled');
				}, 4950);
			$("#frgt_pass_email").focus();
			$('#frgt_pass_email').css('border-color', 'red');
		}
		
		//  Validating confirm password.
		if(confirm_email.length == 0)
		{
			$("#frgt_pass_email_confirm").addClass("errorText");
			//var height = 0;
			if(email_flag == false)
			{
				$("#frgt_pass_email_confirm").focus();
				
				confirm_email_flag = true;
				
			}
			$('#frgt_pass_email_confirm_error').text("* Confirm Email should not be empty *"); 
			//this segment displays the validation rule for password
			$('#frgt_pass_email_confirm_error').fadeIn();
			$('#frgt_pass_email_confirm_error').delay(4950).fadeOut('slow');
			if(email_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					$('#frgt_password_btn').removeAttr('disabled');
				}, 4950);
			}				
			$('#frgt_pass_email_confirm').css('border-color', 'red');
		}
		
		//  Validating email field. ( in login : password should be checked with that of db.)
		else if(confirm_email != email)
		{
			$("#frgt_pass_email_confirm").addClass("errorText");
			//var height = 0;
		  	if(email_flag == false)
			{
				$("#frgt_pass_email_confirm").focus();
				confirm_email_flag = true;
				
			}
			$('#frgt_pass_email_confirm_error').text("* Confirm Email doesn't match *");
			//this segment displays the validation rule for password
			$('#frgt_pass_email_confirm_error').fadeIn();
			$('#frgt_pass_email_confirm_error').delay(4950).fadeOut('slow');
			if(email_flag == false)
			{
				var v = setTimeout(
				function() 
				{
					$('#frgt_password_btn').removeAttr('disabled');
				}, 4950);
			}
			$('#frgt_pass_email_confirm').css('border-color', 'red');
		}
		if(email_flag == false && confirm_email_flag == false)
			$('#frgt_password_btn').removeAttr('disabled');		
	});
});

