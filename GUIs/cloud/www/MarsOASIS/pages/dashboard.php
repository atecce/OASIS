<?php include 'utils/sessionStart.php'?>
<html>

	<head>
		<title>Mars OASIS | Dashboard</title>
		<?php
			if(isset($_SESSION['department']))
			{
				$dept = $_SESSION['department']."";
				
				if((strcmp($dept,"MarsOASIS") == 0) || (strcmp($dept,"NASA") == 0))	
				{
					include 'mars_header_dashboard.php';
				}
				else
				{
					include 'others_header_dashboard.php';
				}
			}
			else
			{
				include 'others_header_dashboard.php';
			}
		?>
		<link rel="stylesheet" href="css/dashboardMenu.css">
		<style>
			#dashboardPage{
				background: #8c99a4;
				color: greenyellow;
			}
			#recentImage{
				width: 90%;
			}
			#recentImageTimeStamp{
				display: hidden;
			}
			#noImgFound{
				display: hidden;
			}
			#noImgFound a{
				color: white;
				text-shadow: none;
			}
			#bodyContainer
			{
				min-height:auto;
			}
			.bodyContainer
			{
				min-height:96%;
			}
		</style>		
		<script type="text/javascript">			
			$(document).ready(function()
			{	
				loadRecentImage();
			});
			function loadRecentImage() 
			{
				var dataString = "";
				$.ajax({
					type: "POST",
					url: "py/getRecentImage.php",
					data: dataString,
					cache: false,
					success: function(result)
					{
						if(result.imgName == "nothing")
						{
							$('#recentImageTimeStamp').hide();
							$('#noImgFound').show();
						}
						else
						{
							$('#recentImageTimeStamp').show();
							$('#noImgFound').hide();
							$('.recentImageWindowImage').prepend('<img class="recentImage" id="recentImage" '+'src="'+"gallery/"+result.imgName+'" title="'+result.imgName+'" />');
							$('#recentImageTimeStamp').html("Image Timestamp: "+result.timeStamp);
						}
					}
				});
			}
		</script>
		<script src="js/d3.min.js"></script>
	</head>
	
	<body id="page1">
		<div class="loader"></div>
		<div class="bodyContainer">
			<center><div class="nav-menu-holder"><?php include 'utils/nav-menu.php'?></div></center>
			
			<div align="center" class="bodyContent" id="bodyContainer">

				<?php include 'utilsDashboard.php'?>
				
			</div>
		</div>
	</body>
	<?php include 'utils/footer.php'?>
</html>