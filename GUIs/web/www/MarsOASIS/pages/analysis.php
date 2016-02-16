<?php include 'utils/sessionStart.php'?>
<html>

	<head>
		<title>Mars OASIS | Analysis</title>
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
			
		<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
		<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
		<style>
			#analysisPage{
				background: #8c99a4;
				color: greenyellow;
			}
			.loader1
			{
				margin-top:5px;
				display:none;
				content: url("ajax-loader.gif");				
			}
			.ui-datepicker-div,.ui-corner-all,.ui-datepicker-title,.ui-datepicker-calendar{
				text-shadow: none; 
				color: black;
			}
			#ui-datepicker-header{
				text-shadow: none; 
				color: black;
			}
			#writeToCSV{
				margin-right: 28px;
			}
			#note{
				margin-top: 10px;
			}
			#bodyContainer{
				min-height: 86%;
			}
		</style>
		
		<script>
		
			$(document).ready(function()
			{
				$(function() 
				{
					$( "#fromDate" ).datepicker();
					$( "#toDate" ).datepicker();
				});
				$("#writeToCSV").click(function(){       // click the link to download
					lock();
					var fromDate = $("#fromDate").val();
					var toDate = $("#toDate").val();
					var sensorDetails = $("#selectSensor_hidden").val();
					var dataString = "selectSensor_value="+sensorDetails+"&fromDate="+fromDate+"&toDate="+toDate;
					//alert(dataString);
					$.ajax({
						type: "POST",
						url: "utils/checkSensorDataForCSV.php",
						data: dataString,
						cache: false,
						success: function(result)
						{
							if(result.flag == "YES")
							{
								$.when( $("#hiddenform").submit() ).done(function() {
									unlock(); 
								});
							}
							else
							{
								var s = sensorDetails.split("<=>");
								var sensor = s[1]+"";
								alert("No records Found for '"+sensor+"' between "+fromDate+" and "+toDate);
								unlock();
							}
						}
					});
					//alert($( "#fromDate" ).val());
					//checkSensorDataForCSV();
					//alert();
				});				
				function lock(){
				  $(".loader1").fadeIn();
				}
				function unlock(){
				  $(".loader1").fadeOut();
				}
			});
		</script>
	</head>
	
	<body id="page1">
		<div class="loader"></div>
		<div align="center" id="bodyContainer">
			 
			<div class="nav-menu-holder"><?php include 'utils/nav-menu.php'?></div>
			
			<div id="staticPlotting" class="bodyContent" align="center">
			
			<div class="staticPlottingHeader"> 
				STATIC PLOTTING &amp; RAW DATA GENERATOR
			</div> 
			
			<div class = "staticPlottingBody">
				<br><br>
					<form id="hiddenform" method="POST" action="utils/downloadcsv.php">
						&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<select id="selectSensor" name="selectSensor" >
							<option value="">Select...</option>
							<option id="ee_tp" value="ee_tp">Air Pressure (External Atmosphere)</option>
							<option id="ie_tp" value="ie_tp">Air Pressure (Internal Atmosphere)</option>
							<option id="ee_rh_t1" value="ee_rh_t1">Air Temperature (External Atmosphere)</option>
							<option id="ie_rh_t2" value="ie_rh_t2">Air Temperature (Growth Medium)</option>
							<option id="ie_rh_t3" value="ie_rh_t3">Air Temperature (Internal Atmosphere)</option>
							<option id="ie_co" value="ie_co">Carbon Dioxide Partial Pressure (Internal Atmosphere)</option>
							<option id="ltp_dop" value="ltp_dop">Dissolved Oxygen (Mixing Tank)</option>
							<option id="ltp_ec" value="ltp_ec">Electrical Conductivity (Leachate)</option>
							<option id="gm_ec" value="gm_ec">Electrical Conductivity (Mixing Tank)</option>
							<option id="ltp_fm1" value="ltp_fm1">Flow Velocity (Growth Medium In-Flow)</option>
							<option id="ltp_fm2" value="ltp_fm2">Flow Velocity (Growth Medium Out-Flow)</option>
							<option id="ee_light" value="ee_light">Lighting: PAR (External)</option>
							<option id="ie_light" value="ie_light">Lighting: PAR (Internal)</option>
							<option id="ltp_ll1" value="ltp_ll1">Liquid Level (Condensate Tank)</option>
							<option id="ltp_ll2" value="ltp_ll2">Liquid Level (Mixing Tank)</option>
							<option id="ltp_ll3" value="ltp_ll3">Liquid Level (Nutrient Tank 1)</option>
							<option id="ltp_ll4" value="ltp_ll4">Liquid Level (Nutrient Tank 2)</option>
							<option id="ltp_ll5" value="ltp_ll5">Liquid Level (pH Tank)</option>
							<option id="ltp_ll6" value="ltp_ll6">Liquid Temperature (Mixing Tank)</option>
							<option id="gm_mo" value="gm_mo">Moisture (Growth Medium)</option>
							<option id="ie_oxy" value="ie_oxy">Oxygen Partial Pressure (Internal Atmosphere)</option>
							<option id="ltp_pH" value="ltp_pH">pH (Leachate)</option>
							<option id="gm_pH" value="gm_pH">pH (Mixing Tank)</option>
							<option id="ee_rh_t1" value="ee_rh_t1">Relative Humidity (External Atmosphere)</option>
							<option id="ie_rh_t2" value="ie_rh_t2">Relative Humidity (Growth Medium)</option>
							<option id="ie_rh_t3" value="ie_rh_t3">Relative Humidity (Internal Atmosphere)</option>
						</select>
						<input type="hidden" style="display:none;" name="selectSensor_value" id="selectSensor_hidden">
		   
						<script>
							$(document).ready(function() {
								var sensors = [];
								sensors["ee_tp"] = "Air Pressure (External Atmosphere)";
								sensors["ie_tp"] = "Air Pressure (Internal Atmosphere)";
								sensors["ee_rh_t1"] = "Air Temperature (External Atmosphere)"; 
								sensors["ie_rh_t2"] = "Air Temperature (Growth Medium)";
								sensors["ie_rh_t3"] = "Air Temperature (Internal Atmosphere)";
								sensors["ie_co"] = "Carbon Dioxide Partial Pressure (Internal Atmosphere)"; 
								sensors["ltp_dop"] = "Dissolved Oxygen (Mixing Tank)";
								sensors["ltp_ec"] = "Electrical Conductivity (Leachate)";
								sensors["gm_ec"] = "Electrical Conductivity (Mixing Tank)"; 
								sensors["ltp_fm1"] = "Flow Velocity (Growth Medium In-Flow)";
								sensors["ltp_fm2"] = "Flow Velocity (Growth Medium Out-Flow)";
								sensors["ee_light"] = "Lighting: PAR (External)"; 
								sensors["ie_light"] = "Lighting: PAR (Internal)"; 
								sensors["ltp_ll1"] = "Liquid Level (Condensate Tank)";
								sensors["ltp_ll2"] = "Liquid Level (Mixing Tank)";
								sensors["ltp_ll3"] = "Liquid Level (Nutrient Tank 1)"; 
								sensors["ltp_ll4"] = "Liquid Level (Nutrient Tank 2)"; 
								sensors["ltp_ll5"] = "Liquid Level (pH Tank)";
								sensors["ltp_ll6"] = "Liquid Temperature (Mixing Tank)";
								sensors["gm_mo"] = "Moisture (Growth Medium)"; 
								sensors["ie_oxy"] = "Oxygen Partial Pressure (Internal Atmosphere)";
								sensors["ltp_pH"] = "pH (Leachate)"; 
								sensors["gm_pH"] = "pH (Mixing Tank)"; 
								sensors["ee_rh_t1"] = "Relative Humidity (External Atmosphere)";
								sensors["ie_rh_t2"] = "Relative Humidity (Growth Medium)";
								sensors["ie_rh_t3"] = "Relative Humidity (Internal Atmosphere)"; 
								$("#selectSensor").change(function(){
									var fileName = sensors[$("#selectSensor").find(":selected").val()];
									//alert(fileName);
									//alert($("#register_dept").find(":selected").innerHTML());
									var value = $("#selectSensor").find(":selected").val()+"<=>"+fileName;
									//alert(value)
									$("#selectSensor_hidden").val(value);	
									//alert($("#register_dept_hidden").val());
								});
							});
						</script>
						<p>From : &nbsp;&nbsp;<input type="text" class="datepicker" name="fromDate" id="fromDate" readonly="" >
							<img id="calendar1" src="css/calendar.png"/></p>
						
						
						<p>Till : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" class="datepicker" name="toDate" id="toDate" readonly="" >
						
							<img id="calendar2" src="css/calendar.png"/></p>
					
					</form>
				</div>
				<div class = "staticPlottingFooter">

						<input type="button" id="writeToCSV" readonly=""   value="Write to CSV">
						<input type="button" readonly=""   value="Plot Selection">
						
						<p id="note">Note: Please increase column width of each column to view data properly in the downloaded <b>.csv</b> file.</p>
					
				</div>
				
				<div id='analysis_loader' class="loader1"></div>
			</div>
			
		</div>
		
		
		
	</body>
	<?php include 'utils/footer.php'?>
</html>