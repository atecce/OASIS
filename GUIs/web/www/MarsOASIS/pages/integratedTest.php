<?php 
	include 'utils/sessionStart.php';
	$user_id = $_SESSION['userEmail'];
	if(isset($_SESSION['department']))
	{
		$dept = $_SESSION['department']."";		
		if((strcmp($dept,"MarsOASIS") == 0) || (strcmp($dept,"NASA") == 0))		
		{
			//valid
		}
		else
		{
			header("Location: dashboard.php");
		}
	}
	else
	{
		header("Location: dashboard.php");
	}
?>
<html>

	<head>
		<title>Mars OASIS | Integrated Tests</title>
		
		<?php include 'utils/marsHeader.php'?>	
		<script src="js/jquery.min.js"></script>
		<?php include 'updateIntegratedTestJS.php'; ?>
		<style>
		.content{
			width:85%;
			text-align:center;
		}
		.p_text
		{
			display:none;
		}         
		
		.toggleBtn{
			width:200px;
		}
		.eeBtns{
			width:140px;
		}
		.ltpBtns{
			width:190px;
		}
		.ieBtns{
			width:180px;
		}
		.gmBtns{
			width:180px;
		}
		.loader1
		{
			margin-top:5px;
			text-align: center;
			display:none;
			vertical-align: sub;
			content: url("ajax-loader.gif");				
		}
		
		.sensor
		{
			margin-right:10px;
		}
		.toggle_body
		{
			margin-top: 5px;
			display: flex;
			text-align: left;
			border-bottom: 2px blue solid;
			padding-top: 12px;
			padding-bottom: 12px;
			padding-left: 12px;
		}
		
		.toggle_body:last-child {			
			border-bottom: none;
		}
		.toggles{
			display:block;
			margin-top:10px;
		}
		.toggle_body:last-child{
			margin-bottom:5px;
		}
		.toggle_ee, .toggle_gm, .toggle_ie, .toggle_ltp
		{
			display:none;
			margin-top:15px;			
			margin-bottom:15px;
			border: 3px blue solid;
			width: 100%;
		}
		
		#integratedTestPage{
			background: #8c99a4;
			color: greenyellow;
		}
	</style>
	</head>
	
	<body id="page1">
		<div class="loader"></div>
		<div align="center" id="bodyContainer">
			 
			<div class="nav-menu-holder"><?php include 'utils/nav-menu.php'?></div>
			<div class="integratedTestContent bodyContent">
				<?php include 'utilsIntegratedTest.php'?>
			</div>
			
			
		</div>
		
	</body>
	<?php include 'utils/footer.php'?>
</html>