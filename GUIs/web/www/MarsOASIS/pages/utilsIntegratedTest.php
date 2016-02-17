	<div class="content">
		
		<div class="toggles">
			<input type="button" id="ee" class="toggleBtn" value="External Environment"	/>
			<input type="button" id="ee_clear" class="clear" value="Clear All"/>
			<div class="toggle_ee">
				<div class="toggle_body">
					<input type="button" class="sensor eeBtns" name="sensor" onclick="update();" id="ee_rh_t1" value="RH-Temp 1"></input>
					<div id='ee_rh_t1_loader' class="loader1"></div>
					<p class="p_text ee_text"  id ="p_ee_rh_t1"></p>					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor eeBtns" name="sensor" onclick="update();" id="ee_light" value="Light (PAR 2)"></input>
					<div id='ee_light_loader' class="loader1"></div>
					<p class="p_text ee_text"  id ="p_ee_light"></p>					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor eeBtns" name="sensor" onclick="update();" id="ee_tp" value="Total Pressure 2"></input>
					<div id='ee_tp_loader' class="loader1"></div>
					<p class="p_text ee_text"  id ="p_ee_tp"></p>					
				</div>
			</div>
		</div>	
		<div class="toggles">	
			<input type="button" id="gm" class="toggleBtn" value="Growth Medium"	/>
			<input type="button" id="gm_clear" class="clear" value="Clear All"/>			
			<div class="toggle_gm">
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_ec" value="Electrical Conductivity 1"></input>
					<div id='gm_ec_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_ec"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_mo1" value="Moisture 1"></input>
					<div id='gm_mo1_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_mo1"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_mo2" value="Moisture 2"></input>
					<div id='gm_mo2_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_mo2"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_mo3" value="Moisture 3"></input>
					<div id='gm_mo3_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_mo3"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_mo4" value="Moisture 4"></input>
					<div id='gm_mo4_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_mo4"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_pH" value="pH 1"></input>
					<div id='gm_pH_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_pH"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_temp2" value="Temperature 2"></input>
					<div id='gm_temp2_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_temp2"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_temp3" value="Temperature 3"></input>
					<div id='gm_temp3_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_temp3"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor gmBtns" name="sensor" onclick="update();" id="gm_temp4" value="Temperature 4"></input>
					<div id='gm_temp4_loader' class="loader1"></div>
					<p class="p_text gm_text"  id ="p_gm_temp4"></p>
					
				</div>
			</div>
		</div>
		<div class="toggles">
			<input type="button" id="ie" class="toggleBtn" value="Internal Environment"	/>
			<input type="button" id="ie_clear" class="clear" value="Clear All"/>
			<div class="toggle_ie">
				<div class="toggle_body">
					<input type="button" class="sensor ieBtns" name="sensor" onclick="update();" id="ie_co" value="Carbon Dioxide (CO2)"></input>
					<div id='ie_co_loader' class="loader1"></div>
					<p class="p_text ie_text"  id ="p_ie_co"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ieBtns" name="sensor" onclick="update();" id="ie_light" value="Light (PAR 1)"></input>
					<div id='ie_light_loader' class="loader1"></div>
					<p class="p_text ie_text"  id ="p_ie_light"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ieBtns" name="sensor" onclick="update();" id="ie_oxy" value="Oxygen (O2)"></input>
					<div id='ie_oxy_loader' class="loader1"></div>
					<p class="p_text ie_text"  id ="p_ie_oxy"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ieBtns" name="sensor" onclick="update();" id="ie_rh_t2" value="RH-Temp 2"></input>
					<div id='ie_rh_t2_loader' class="loader1"></div>
					<p class="p_text ie_text"  id ="p_ie_rh_t2"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ieBtns" name="sensor" onclick="update();" id="ie_rh_t3" value="RH-Temp 3"></input>
					<div id='ie_rh_t3_loader' class="loader1"></div>
					<p class="p_text ie_text"  id ="p_ie_rh_t3"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ieBtns" name="sensor" onclick="update();" id="ie_tp" value="Total Pressure 1"></input>
					<div id='ie_tp_loader' class="loader1"></div>
					<p class="p_text ie_text"  id ="p_ie_tp"></p>
					
				</div>
			</div>
		</div>	
		<div class="toggles">
			<input type="button" id="ltp" class="toggleBtn" value="Liquid Tanks & Plumbing"	/>
			<input type="button" id="ltp_clear" class="clear" value="Clear All"/>
			<div class="toggle_ltp">
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_dop" value="Dissolved Oxygen"></input>
					<div id='ltp_dop_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_dop"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_ec" value="Electrical Conductivity 2"></input>
					<div id='ltp_ec_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_ec"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_fm1" value="Flow Meter 1"></input>
					<div id='ltp_fm1_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_fm1"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_fm2" value="Flow Meter 2"></input>
					<div id='ltp_fm2_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_fm2"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_ll1" value="Liquid Level 1"></input>
					<div id='ltp_ll1_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_ll1"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_ll2" value="Liquid Level 2"></input>
					<div id='ltp_ll2_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_ll2"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_ll3" value="Liquid Level 3"></input>
					<div id='ltp_ll3_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_ll3"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_ll4" value="Liquid Level 4"></input>
					<div id='ltp_ll4_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_ll4"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_ll5" value="Liquid Level 5"></input>
					<div id='ltp_ll5_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_ll5"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_ll6" value="Liquid Level 6"></input>
					<div id='ltp_ll6_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_ll6"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_pH" value="pH 2"></input>
					<div id='ltp_pH_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_pH"></p>
					
				</div>
				<div class="toggle_body">
					<input type="button" class="sensor ltpBtns" name="sensor" onclick="update();" id="ltp_temp" value="Temperature 1"></input>
					<div id='ltp_temp_loader' class="loader1"></div>
					<p class="p_text ltp_text"  id ="p_ltp_temp"></p>
					
				</div>
			</div>
		</div>	
	</div>