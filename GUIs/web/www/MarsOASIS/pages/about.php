<?php include 'utils/sessionStart.php'; ?>
<html>

	<head>
		<title>Mars OASIS | About</title>
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
			#aboutPage{
				background: #8c99a4;
				color: greenyellow;
			}
			#bodyContainer{
				min-height: 76%;
			}
		</style>
	</head>
	
	<body id="page1">
		<div class="loader"></div>
		<center><div class="nav-menu-holder"><?php include 'utils/nav-menu.php'?></div></center>
		<div align="center" class="bodyContent" id="bodyContainer">
			 
			<div id="aboutContent" align="center">
				<div class="aboutContentHeader"> 
					About Mars OASIS
				</div> 
				
				<div class = "aboutContentBody">
				
					
					 <p id="aboutContentPara"> 
							In order to enable long term habitation on planetary surfaces, a means of sustainable food
						production must be developed. Addressing this need for surface habitats on Mars, the
						MarsOASIS team has developed a concept for a Martian surface greenhouse for unmanned
						crop production research as a proof of concept for larger scale food production facilities for
						manned surface missions. Utilizing in-situ resources such as the Martian atmosphere,
						sunlight, and UV-C radiation, the greenhouse aims to provide a sustainable method of longterm
						food production requiring minimal consumable resources. The MarsOASIS system is
						capable of growing a full life cycle of Outredgeous lettuce with its autonomous control
						system designed for a unmanned environment, only requiring teleoperation in extreme
						circumstances. A reduced-scope prototype of MarsOASIS is being developed to test
						technologies such as a natural/artificial hybrid lighting system, a closed water recycling
						system, remote teleoperation, and fully autonomous monitoring and control of the
						greenhouse. The prototype is currently in the final stages of design, with a full
						demonstration of plant life cycle testing set to occur in Fall 2015. Results from this
						prototype demonstration will help quantify the feasibility of the innovative approaches seen
						in the MarsOASIS design.
					</p>		
					<img alt="Captured Image" id="capturedImg" class="capturedImg"src="lettuce.png"/>
				
				</div>
				<div class = "aboutContentFooter">
					
				</div>
			</div>
		</div>
		
		
	</body>
	<?php include 'utils/footer.php'?>
</html>