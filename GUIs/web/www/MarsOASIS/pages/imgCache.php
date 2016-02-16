<?php include 'utils/sessionStart.php'?>
<html>

	<head>
		<title>Mars OASIS | Image Cache</title>
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
			#imgCachePage{
				background: #8c99a4;
				color: greenyellow;
			}
			.imageLoader {
				position: relative;
				width:280px;
				height:280px;
				background: url(css/loading.gif) 50% 50% no-repeat;
			}
			#noImgFound {
				display: hidden;
			}
			#noImgFound a{
				color: white;
				text-shadow: none;
			}			
		</style>
		<script type="text/javascript">			
			$(document).ready(function()
			{	
				$("#bodyContainer").css("min-height","75%");
				loadGallery();
				function loadPic(imgs)
				{
					//alert(" IMGS:'"+imgs+"'");
					if(imgs != "" && imgs != " ")
					{
						var arr = imgs.split('<=>');
						
						if(arr.length > 0)
						{
							$("#noImgFound").hide();
							var numberOfImgRows = 0;
							for(var i = 0; i < arr.length; i++)
							{
								//<img class="sampleImg" src="../images/lettuce.jpg"></img>
								$(".images").append('<img class="sampleImg" id=imgs' + i + ' ' +
									'src="' + "gallery/" + arr[i] + '" />');
								if(i % 2 == 0)
								{
								   numberOfImgRows++;
								}
							}
							var percent = (numberOfImgRows*30) + 50 + numberOfImgRows;
							$("#bodyContainer").css("min-height",percent+"%");
						}
						else
						{
							$("#noImgFound").show();
						}
						return;	
					}
				}
				function loadGallery() 
				{
					//$('#'+title+'_loader').show();
					$('.imageLoader').fadeIn();
					var dataString = "";
					//$('#imageLoader').css('display', 'block');
					$.ajax({
						type: "POST",
						url: "utils/getImageNames.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							//alert(result.size);
							
							//alert(result.imgs);
							$.when( loadPic(result.imgs) ).done(function() {
								$('.imageLoader').fadeOut();
							});
							//
						},
						error: function (jqXHR, exception) 
						{
							//$('.imageLoader').fadeOut();
							var msg = '';
							//alert(exception);
							//alert(jqXHR.responseText);
							if (jqXHR.status === 0) {
								msg = 'Not connect.\n Verify Network.';
							} else if (jqXHR.status == 404) {
								msg = 'Requested page not found. [404]';
							} else if (jqXHR.status == 500) {
								msg = 'Internal Server Error [500].';
							} else if (exception === 'parsererror') {
								msg = 'Requested JSON parse failed.';
							} else if (exception === 'timeout') {
								msg = 'Time out error.';
							} else if (exception === 'abort') {
								msg = 'Ajax request aborted.';
							} else {
								msg = 'Uncaught Error.\n' + jqXHR.responseText;
							}
							alert(msg);
						}
					});
				}
			});
		</script>
	</head>
	
	<body id="page1" >
		<div class="loader"></div>
		<div align="center" id="bodyContainer">
			
			<div class="nav-menu-holder"><?php include 'utils/nav-menu.php'?></div>
			
			<div id="imgContainer" class="bodyContent" align="center">
			
				<div class="imgContainerHeader"> 
					GALLERY
				</div> 
				
				<div class = "imgContainerBody">
					<div class="imageLoader"></div>
					<div class="images">
						<p id="noImgFound">No Images Found. Use Capture Image feature in <a href="cameraControl.php">Camera Control Page</a>.</p>
					</div>
				</div>
				<div class = "imgContainerFooter">
				</div>
			</div>
			
		</div>
		
	</body>
	<?php include 'utils/footer.php'?>
</html>