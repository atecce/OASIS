<?php include 'utils/sessionStart.php'?>
<html>

	<head>
		<title>Mars OASIS | Camera Control</title>
		<?php
			if(isset($_SESSION['department']))
			{
				$dept = $_SESSION['department']."";
				if((strcmp($dept,"MarsOASIS") == 0) || (strcmp($dept,"NASA") == 0))	
				{
					include 'utils/marsHeader.php';
				}
				else
				{
					include 'utils/othersHeader.php';
				}
			}
			else
			{
				include 'utils/othersHeader.php';
			}
		?>
		<style>
			#cameraControlPage{
				background: #8c99a4;
				color: greenyellow;
			}
			#ie_camera_loader
			{
				margin-top:5px;
				text-align: center;
				display:none;
				vertical-align: sub;
				content: url("ajax-loader.gif");				
			}
			#capturedImg
			{
				width: 90%;
			}
		</style>
		<script type="text/javascript">
			$(document).ready(function(){
				$("#bodyContainer").css("min-height","75%");
				$("#capturedImg").fadeOut();
				
				function showCapturedImg(fileName)
				{					
					$("#capturedImg").attr('src','');
					$("#capturedImg").fadeOut();
					$("#capturedImg").attr('src','gallery/'+fileName);
					$("#capturedImg").fadeIn("slow");
					$("#bodyContainer").css("min-height","115%");
				}
				
				$("#ie_camera").click(function() 
				{
					//alert("Inside this")
					var title = "ie_camera";
					var dataString = 'py='+title;
					$("#ie_camera_loader").fadeIn();
					
					$.ajax({
						type: "POST",
						url: "py/getImageFromSensor.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							//alert(result.file+"");
							fileName = result.file+"";
							showCapturedImg(fileName);
							$("#ie_camera_loader").fadeOut();
						}
					});
				});		
			});
			
		</script>		
	</head>
	
	<body id="page1">
		<div class="loader"></div>
		<div align="center" id="bodyContainer">
			 
			
			<div class="nav-menu-holder"><?php include 'utils/nav-menu.php'?></div>
			
			<div id="cameraControl" class="bodyContent" align="center">
				<div class="cameraControlHeader"> 
					CAMERA CONTROL
				</div> 
				
				<div class = "cameraControlBody">
				
					
					<p>Set the Camera Position on the Bracket&nbsp;
							<input type="text" value=""/></p>
					
					
					<p>Set the Angle of the Camera Bracket &nbsp;&nbsp;&nbsp;&nbsp;
							<input type="text" value="35"/></p>
							
					<img alt="Captured Image" id="capturedImg" class="capturedImg" src="lettuce.png"/>
				
				</div>
				<div class = "cameraControlFooter">
					<input type="button" id="ie_camera" value="CAPTURE"/>
					<div id='ie_camera_loader' class="loader1"></div>
				</div>
			</div>
			
		</div>
		
	</body>
	<?php include 'utils/footer.php'?>
</html>