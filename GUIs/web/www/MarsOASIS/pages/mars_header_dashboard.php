
<meta charset="UTF-8">
<link rel="icon" type="image/jpg" href="../images/cu.jpg"></link>
<link href="css/page_styles.css" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="css/menu.css">
<link href="css/styles.css" rel="stylesheet" type="text/css">
<link href='css/fonts.css' rel='stylesheet' type='text/css'>
<script type="text/javascript" src="js/jquery-1.11.3.js"></script>
<script src="js/lucid.js"></script>
<script src="js/jquery.sticky.js"></script>
<script src="js/menu.js"></script>

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
		$(".section").hide();
		$("#recentImageWindow").fadeIn();
		
		$(".links").css("background","initial");
		$("#recentImageWindowLink").css("background","#0d77b6");
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
			$("#messageContainer").fadeOut();
			$("#notificationContainer").css('margin-left','-181px');			
			$("#notificationContainer").fadeToggle(300);		
			$("#accountContainer").fadeOut();
			$("#notification_count").fadeOut("slow");
			return false;
		});
		
		
		$(".elementN").click(function()
		{
			$("#notificationContainer").fadeOut(300);
			return false;
		});

	
		//Popup Click
		$("#notificationContainer").click(function()
		{
			return false;
		});
		
		// Messages
		$("#messageLink").click(function()
		{
			$("#notificationContainer").fadeOut();
			$("#messageContainer").css('margin-left','-180px');
			$("#messageContainer").fadeToggle(300);
			$("#accountContainer").fadeOut();
			$("#message_count").fadeOut("slow");
			return false;
		});
		
		$(".elementM").click(function()
		{
			$("#messageContainer").fadeOut(300);
			return false;
		});

	
		//Popup Click
		$("#messageContainer").click(function()
		{
			return false
		});
		
		// Account
		$("#accountLink").click(function()
		{
			$("#notificationContainer").fadeOut();
			$("#messageContainer").fadeOut();
			$("#accountContainer").css('margin-left','-150px');
			$("#accountContainer").fadeToggle("slow");
			return false;
		});
		
		$(".elementA").click(function()
		{
			$("#accountContainer").fadeOut(300);
			return false;
		});

	
		//Popup Click
		$("#accountContainer").click(function()
		{
			return false;
		});
		
		$( '.messages' ).on( 'mousewheel', function ( e ) {

			$('.messages').impulse();
			e.preventDefault();
		});
		
		$( '.notifications' ).on( 'mousewheel', function ( e ) {
			
			$('.notifications').impulse();
			e.preventDefault();
		});	
		
		var f1 = false;
		$("#innerMenu").click(function()
		{
			f1 = true;
		});
		
		$("#recentImageWindowLink").click(function()
		{
			$(".links").css("background","initial");
			$("#recentImageWindowLink").css("background","#0d77b6");
			$(".section").hide();
			//$(".section").fadeOut("fast");
			$("#recentImageWindow").fadeIn();
			$(".bodyContainer").css("min-height","96%");
		});
		$("#growthMediumDataLink").click(function()
		{	
			$(".links").css("background","initial");
			$("#growthMediumDataLink").css("background","#0d77b6");
			$(".section").hide();
			//$(".section").fadeOut("fast");
			$("#growthMediumData").fadeIn();
			$(".bodyContainer").css("min-height","88%");
		});
		$("#dynamicPlotWindowLink").click(function()
		{
			$(".links").css("background","initial");
			$("#dynamicPlotWindowLink").css("background","#0d77b6");
			$(".section").hide();
			//$(".section").fadeOut("fast");
			$("#dynamicPlotWindow").fadeIn();
			$(".bodyContainer").css("min-height","96%");
		});
		$("#liquidTanksAndPlumbingDataLink").click(function()
		{			
			$(".links").css("background","initial");
			$("#liquidTanksAndPlumbingDataLink").css("background","#0d77b6");
			$(".section").hide();
			//$(".section").fadeOut("fast");
			$("#liquidTanks").fadeIn();
			$(".bodyContainer").css("min-height","145%");
		});
		$("#updateDataLink").click(function()
		{
			$(".links").css("background","initial");
			$("#updateDataLink").css("background","#0d77b6");
			$(".section").hide();
			//$(".section").fadeOut("fast");
			$("#update").fadeIn();
			$(".bodyContainer").css("min-height","65%");
		});

		//Document Click
		$(document).click(function()
		{
			//alert("hi")
			$("#notificationContainer").fadeOut(300);
			$("#messageContainer").fadeOut(300);			
			$("#accountContainer").fadeOut(300);
			if(f1)
			{
				$("#innerMenu").toggleClass("active");
				$("#innerMenuContent").toggleClass('content-open');
				f1 = false;
			}
			else
			{
				$("#innerMenu").removeClass("active");
				$("#innerMenuContent").removeClass('content-open');
			}
		});
	});

</script>