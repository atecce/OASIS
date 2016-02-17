
<meta charset="UTF-8">
<link rel="icon" type="image/jpg" href="../images/cu.jpg"></link>
<link href="css/page_styles.css" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="css/menu.css">
<link href="css/styles.css" rel="stylesheet" type="text/css">
<link href='css/fonts.css' rel='stylesheet' type='text/css'>
<script type="text/javascript" src="js/jquery.min.js"></script>
<script src="js/lucid.js"></script>
<script src="js/jquery.sticky.js"></script>
<script src="js/menu1.js"></script>

<script type="text/javascript" >
	$(window).on('load', function() 
	{
		$(".parentNav").sticky({topSpacing:10});
		
		var width = window.innerWidth;
		var elem = document.getElementById("logoLeft");
		if( width <= 450 )
		{
			//alert(width)
			$(elem).detach().appendTo('#marsLogoContainer1');
			$(".main-menu").css("margin-left", 0);
			$(".main-menu").css("width", "100%");
			$(".sub-nav-container").css("margin-left", 0);
		}
		else
		{
			//alert(width)
			$(elem).detach().prependTo('#parentNav');
			$(".main-menu").css("margin-left", 120);
			$(".main-menu").css("width", "calc(100% - 120px)");
			$(".main-menu").css("width", "-webkit-calc(100% - 120px)");
			$(".main-menu").css("width", "-o-calc(100% - 120px)");
			$(".main-menu").css("width", "-moz-calc(100% - 120px)");
			$(".sub-nav-container").css("margin-left", 120);
		}
		
		$(".loader").fadeOut("slow");
		
		$(this).impulse();
		
		$('.notifications').impulse({target: $('.notifications')});
		$('.messages').impulse({target: $('.messages')});
	});
	
	$(document).ready(function()
	{
		window.onresize = function()
		{
			$(".parentNav").sticky({topSpacing:10});
			
			//alert("hiii")
			var width = window.innerWidth;
			var elem = document.getElementById("logoLeft");
			if( width <= 450 )
			{
				//alert(width)
				$(elem).detach().appendTo('#marsLogoContainer1');
				$(".main-menu").css("margin-left", 0);
				$(".main-menu").css("width", "100%");
				$(".sub-nav-container").css("margin-left", 0);
			}
			else
			{
				//alert(width)
				$(elem).detach().prependTo('#parentNav');
				$(".main-menu").css("margin-left", 120);
				$(".main-menu").css("width", "calc(100% - 120px)");
				$(".main-menu").css("width", "-webkit-calc(100% - 120px)");
				$(".main-menu").css("width", "-o-calc(100% - 120px)");
				$(".main-menu").css("width", "-moz-calc(100% - 120px)");
				$(".sub-nav-container").css("margin-left", 120);
			}	
			
		};

		// Notifications
		$("#notificationLink").click(function()
		{
			$("#messageContainer").fadeOut(300);
			$("#notificationContainer").css('margin-left','-181px');			
			$("#notificationContainer").fadeToggle(300);		
			$("#accountContainer").fadeOut(300);
			$("#notification_count").fadeOut("slow");
			return false;
		});
		
		
		$(".elementN").click(function()
		{
			$("#notificationContainer").fadeOut(300);
			return false;
		});

	
		//Document Click
		$(document).click(function()
		{
			$("#notificationContainer").fadeOut(300);
		});
		//Popup Click
		$("#notificationContainer").click(function()
		{
			return false
		});
		
		// Messages
		$("#messageLink").click(function()
		{
			$("#notificationContainer").fadeOut(300);
			$("#messageContainer").css('margin-left','-180px');
			$("#messageContainer").fadeToggle(300);
			$("#accountContainer").fadeOut(300);
			$("#message_count").fadeOut("slow");
			return false;
		});
		
		$(".elementM").click(function()
		{
			$("#messageContainer").fadeOut(300);
			return false;
		});

	
		//Document Click
		$(document).click(function()
		{
			$("#messageContainer").fadeOut(300);
		});
		//Popup Click
		$("#messageContainer").click(function()
		{
			return false
		});
		
		// Account
		$("#accountLink").click(function()
		{
			$("#notificationContainer").fadeOut(300);
			$("#messageContainer").fadeOut(300);
			$("#accountContainer").css('margin-left','-150px');
			$("#accountContainer").fadeToggle("slow");
			return false;
		});
		
		$(".elementA").click(function()
		{
			$("#accountContainer").fadeOut(300);
			return false;
		});

	
		//Document Click
		$(document).click(function()
		{
			$("#accountContainer").fadeOut(300);
		});
		//Popup Click
		$("#accountContainer").click(function()
		{
			return false
		});
		
		$( '.messages' ).on( 'mousewheel', function ( e ) {

			$('.messages').impulse();
			e.preventDefault();
		});
		
		$( '.notifications' ).on( 'mousewheel', function ( e ) {
			
			$('.notifications').impulse();
			e.preventDefault();
		});	
		
	});
	
	
</script>