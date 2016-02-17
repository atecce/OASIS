<div class="content">

	<div class="toggles" style="display:inline-flex;">
	
			<p style="margin:20px;height:20px">Mode: 	</p>
			<div class="onoffswitch" style="width:48px;">
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="modifyonoffswitch" >
				<label class="onoffswitch-label" for="modifyonoffswitch"></label>
			</div>		
	</div>
	
	
	<div class="toggles">
	<input type="button" id="displayStart" value="Start Mars Oasis!" class="toggleBtn"/>
	<div class="modeOnWarningContainer">
		<img src="css/alert.png" id="START_Warning" class="modeOnWaring" title="You Can Modify The Values Now ! Beware!" />
	</div>
	<div id='toggleStart_loader' class="loader1"></div>
	<div class="toggleStart">
	<div class="toggle">	
			<p>Start: 	</p>
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="startonoffswitch" >
				<label class="onoffswitch-label" for="startonoffswitch"></label>
			</div>
		</div>
	</div>
	</div>
	
	<div class="toggles">
	<input type="button" id="displayStop" value="Stop Mars Oasis!" class="toggleBtn"/>
	<div class="modeOnWarningContainer">
		<img src="css/alert.png" id="STOP_Warning" class="modeOnWaring" title="You Can Modify The Values Now ! Beware!"  />
	</div>
	<div id='toggleStop_loader' class="loader1"></div>
	<div class="toggleStop">
	<div class="toggle">	
			<p>Stop: 	</p>
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="stoponoffswitch" >
				<label class="onoffswitch-label" for="stoponoffswitch"></label>
			</div>
		</div>
	</div>
	</div>
	
	<div class="toggles">
	<input type="button" id="displayWFC" value="Water Flow Control" class="toggleBtn"/>
	<div class="modeOnWarningContainer">
		<img src="css/alert.png" id="WFC_Warning" class="modeOnWaring" title="You Can Modify The Values Now ! Beware!"  />
	</div>
	<div id='toggleWFCBody_loader' class="loader1"></div>
	<div class="toggleWFCBody">
		<table class="toggleTable">
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Main Tank Pump (P1):	</p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox WFC_values values" id="p1onoffswitch" >
				<label class="onoffswitch-label" for="p1onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Condensate Tank Pump (P2): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox WFC_values values" id="p2onoffswitch" >
				<label class="onoffswitch-label" for="p2onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Leachate Tank Pump (P8): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox WFC_values values" id="p8onoffswitch" >
				<label class="onoffswitch-label" for="p8onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		</table>
	</div>	
	</div>
	
	<div class="toggles">
	<input type="button" id="displayWC" value="Water Conditioning" class="toggleBtn"/>
	<div class="modeOnWarningContainer">
		<img src="css/alert.png" id="WC_Warning" class="modeOnWaring" title="You Can Modify The Values Now ! Beware!"  />
	</div>
	<div id='toggleWCBody_loader' class="loader1"></div>
	<div class="toggleWCBody">
		<table class="toggleTable">
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Water Heater (M1): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox WC_values values" id="m1onoffswitch" >
				<label class="onoffswitch-label" for="m1onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Water Chiller (M2): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox WC_values values" id="m2onoffswitch" >
				<label class="onoffswitch-label" for="m2onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Nutrient 1 Dosing (P3):	</p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox WC_values values" id="p3onoffswitch" >
				<label class="onoffswitch-label" for="p3onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Nutrient 2 Dosing (P4): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox WC_values values" id="p4onoffswitch" >
				<label class="onoffswitch-label" for="p4onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>pH Dosing (P5): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox WC_values values" id="p5onoffswitch" >
				<label class="onoffswitch-label" for="p5onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		</table>
	</div>	
	</div>
	
	<div class="toggles">
	<input type="button" id="displayAM" value="Atmospheric Management" class="toggleBtn"/>
	<div class="modeOnWarningContainer">
		<img src="css/alert.png" id="AM_Warning" class="modeOnWaring" title="You Can Modify The Values Now ! Beware!"  />
	</div>
	<div id='toggleAMBody_loader' class="loader1"></div>
	<div class="toggleAMBody">
		<table class="toggleTable">
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Humidifier/Mister Pump (P10): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox AM_values values" id="p10onoffswitch" >
				<label class="onoffswitch-label" for="p10onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Dehumidifier & Air Pump (M9/P12): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox AM_values values" id="p12onoffswitch" >
				<label class="onoffswitch-label" for="p12onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>O2 Concentrator (M8):	</p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox AM_values AM_Type_1 values" id="m8onoffswitch" >
				<label class="onoffswitch-label" for="m8onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>CO2 Gas Solenoid (V3): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox AM_values AM_Type_1 values" id="v3onoffswitch" >
				<label class="onoffswitch-label" for="v3onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>N2 Gas Solenoid (V4): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox AM_values AM_Type_1 values" id="v4onoffswitch" >
				<label class="onoffswitch-label" for="v4onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Fan 1 (M6): </p></td>
			<td class="toggleColumn">
			<div id="rangeContainer">
			<input type="range" min="0" max="100" id="m6-value-range" class="AM_values AM_Type_2" onchange="handlePercent(this);">           
			<p id="m6-value" class="AM_values_Text rangeValue"></p>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Fan 2 (M7): </p></td>
			<td class="toggleColumn">
			<div id="rangeContainer">
			<input type="range" min="0" max="100" id="m7-value-range" class="AM_values AM_Type_2" onchange="handlePercent(this);">           
			<p id="m7-value" class="AM_values_Text rangeValue"></p>
			</div>
			</td>
		</div>
		</tr>
		</table>
	</div>	
	</div>
	
	
	<div class="toggles">
	<input type="button" id="displayLI" value="Lighting and Imagery" class="toggleBtn"/>
	<div class="modeOnWarningContainer">
		<img src="css/alert.png" id="LI_Warning" class="modeOnWaring" title="You Can Modify The Values Now ! Beware!"  />
	</div>
	<div id='toggleLIBody_loader' class="loader1"></div>
	<div class="toggleLIBody">
		<table class="toggleTable">
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Camera Location (LA):	</p></td>
			<td class="toggleColumn">
			<div id="rangeContainer">
			<input type="range" min="0" max="100" id="la-value-range" class="LI_values" onchange="handlePercent(this);">           
			<p id="la-value" class="LI_values_Text rangeValue"></p>	
			</div>	
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Bracket Rotation (ST): </p></td>
			<td class="toggleColumn">
			<div id="rangeContainer">
			<input type="range" min="0" max="100" id="st-value-range" class="LI_values" onchange="handlePercent(this);">           
			<p id="st-value" class="LI_values_Text rangeValue"></p>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
			<td class="toggleColumn"><p>LED % Brightness (M18): </p></td>
			<td class="toggleColumn">
			<div id="rangeContainer">
			<input type="range" min="0" max="100" id="m18-value-range" class="LI_values" onchange="handlePercent(this);">           
			<p id="m18-value" class="LI_values_Text rangeValue"></p>
			</div>
			</td>
		</tr>
		</table>
	</div>	
	</div>
	
	<div class="toggles">
	<input type="button" id="displaySM" value="System Maintenance" class="toggleBtn"/>
	<div class="modeOnWarningContainer">
		<img src="css/alert.png" id="SM_Warning" class="modeOnWaring" title="You Can Modify The Values Now ! Beware!"  />
	</div>
	<div id='toggleSMBody_loader' class="loader1"></div>
	<div class="toggleSMBody">
		<table class="toggleTable">
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Main Tank Circulation (P11): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox SM_values values" id="p11onoffswitch" >
				<label class="onoffswitch-label" for="p11onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Main Tank Air Bubbler (P7): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox SM_values values" id="p7onoffswitch" >
				<label class="onoffswitch-label" for="p7onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Nutrient Tank 1 Circulation (P6):	</p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox SM_values values" id="p6onoffswitch" >
				<label class="onoffswitch-label" for="p6onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>Nutrient Tank 2 Circulation (P9): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox SM_values values" id="p9onoffswitch" >
				<label class="onoffswitch-label" for="p9onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		<tr class="toggleRow">
		<div class="toggle">	
			<td class="toggleColumn"><p>UV Filter (F1): </p></td>
			<td class="toggleColumn">
			<div class="onoffswitch">
				
				<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox SM_values values" id="f1onoffswitch" >
				<label class="onoffswitch-label" for="f1onoffswitch"></label>
			</div>
			</td>
		</div>
		</tr>
		</table>
	</div>	
	</div>
	
</div>