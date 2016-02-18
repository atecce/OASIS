			<div class="content" align="center">
				<nav class="innerMenuContent" id="innerMenuContent">
					<h3>Menu</h3>
					<a id="recentImageWindowLink" class="links" href="#">Recent Image Window</a>
					<a id="growthMediumDataLink" class="links" href="#">Growth Medium Data</a>
					<a id="dynamicPlotWindowLink" class="links" href="#">Dynamic Plot Window</a>
					<a id="liquidTanksAndPlumbingDataLink" class="links" href="#">Liquid Tanks & Plumbing Data</a>
					<a id="updateDataLink" class="links" href="#">Update Data</a>
				</nav>
				<div class="innerMenuBtnContainer">
					<button class="innerMenu" id="innerMenu">Dashboard Menu</button>
				</div>
				<div id="recentImageWindow" align="center" class="section">
					<div class="recentImageWindowHeader"> 
						RECENT IMAGE WINDOW 
					</div> 
					
					<div class = "recentImageWindowBody">
						<div class = "recentImageWindowImage">
							<p id="noImgFound">No Images Found. Use Capture Image feature in <a href="cameraControl.php">Camera Control Page</a>.</p>

						</div>
						<div class="recentImageWindowFooter default1">
							<p id="recentImageTimeStamp">Image Timestamp: 2015-03-24 13:45:15</p>
						</div>
					</div>
				</div>
				
				<div id="growthMediumData" align="center" class="section">
				
					<div class="growthMediumDataHeader"> 
						GROWTH MEDIUM DATA 
					</div> 
					
					<div class = "growthMediumDataBody">
						<div class="elementParent"> 
							<div class="element first"> 
								<p class="elementHeader default1">
									AIR TEMPERATURE (°C)
								</p>	
								<p class="elementBody default1">
									<p class="elementValue default1">
										21.49
									</p>
									<p class="elementRange default1">
										SET RANGE:
									</p>
									<p class="elementRangeValue default1">
										17.00 - 24.00
									</p>
								</p>
								<p class="elementFooter default1">
									Plot
								</p>						
							</div>
							<div class="element">
								<p class="elementHeader default1">
									RELATIVE HUMIDITY (%)
								</p>	
								<p class="elementBody default1">
									<p class="elementValue default1">
										57.93
									</p>
									<p class="elementRange default1">
										SET RANGE:
									</p>
									<p class="elementRangeValue default1">
										50.00 - 70.00
									</p>
								</p>
								<p class="elementFooter default1">
									Plot
								</p>	
							</div>
							<div class="element">
								<p class="elementHeader default1">
									EC: LEACHATE (μS/cm)
								</p>	
								<p class="elementBody default1">
									<p class="elementValue default1">
										1110.45
									</p>
									<p class="elementRange default1">
										SET RANGE:
									</p>
									<p class="elementRangeValue default1">
										1100.00 - 1300.00
									</p>
								</p>
								<p class="elementFooter default1">
									Plot
								</p>	
							</div>
						</div>
						<div class="elementParent"> 
							<div class="element first">
								<p class="elementHeader default1">
									pH: LEACHATE
								</p>	
								<p class="elementBody default1">
									<p class="elementValue default1">
										5.68
									</p>
									<p class="elementRange default1">
										SET RANGE:
									</p>
									<p class="elementRangeValue default1">
										5.00 - 6.00
									</p>
								</p>
								<p class="elementFooter default1">
									Plot
								</p>
							</div>
							<div class="element">
								<p class="elementHeader default1">
									MOISTURE (??)
								</p>	
								<p class="elementBody default1">
									<p class="elementValue default1">
										∞
									</p>
									<p class="elementRange default1">
										SET RANGE:
									</p>
									<p class="elementRangeValue default1">
										0.1 - 0.4
									</p>
								</p>
								<p class="elementFooter default1">
									Plot
								</p>	
							</div>
							
						</div>
					</div>
				</div>
				
				<div id="dynamicPlotWindow" align="center" class="section">
					<div class="dynamicPlotWindowHeader"> 
						DYNAMIC PLOT WINDOW
					</div> 
					
					<div class = "dynamicPlotWindowBody">
						<p class = "dynamicPlotWindowImage">
							<div id="graphDiv"> </div>
									<?php include 'utils/graphContent.php'?>

						</p>
						<p class="dynamicPlotWindowFooter default1">
							Click "PLOT" on a parameter's display icon for Dynamic Plotting.
						</p>
					</div>
				</div>
				<div id="liquidTanks" align="center" class="section">
			
					<div class="liquidTanksHeader"> 
						LIQUID TANKS & PLUMBING DATA 
					</div> 
					
					<div class = "liquidTanksBody">
						<div class="elementParentLIQ"> 
							<div class="elementLIQ first"> 
								<p class="elementHeaderLIQ default2">
									ELECTRICAL CONDUC:<br> MIXING TANK(μS/cm)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										201.6
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										1150 - 1250
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>						
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									pH:<br> MIXING TANK
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										505.6
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										5.5 - 6
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									LIQ. TEMP:<br> MIXING TANK (°C)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										N / A
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										23 - 27
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
						</div>
						<div class="elementParentLIQ"> 
							<div class="elementLIQ first">
								<p class="elementHeaderLIQ default2">
									DISSOLVED O2:<br> MIXING TANK (mg/L)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										N / A
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										N / A
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									LIQ. LEVEL:<br> MIXING TANK (cm)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										11.56
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										0 - 8
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									LIQ. LEVEL:<br> CONDENSATE TANK
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										12.6
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										0 - 10
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									LIQ. LEVEL:<br> NUTRIENT TANK 1 (cm)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										11.6
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										0 - 10
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									LIQ. LEVEL:<br> NUTRIENT TANK 2 (cm)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										11.6
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										0 - 8
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									LIQ. LEVEL:<br> pH TANK(cm)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										11.6
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										0 - 8
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									LIQ. LEVEL:<br> LEACHATE TANK (cm)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										12.6
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										0 - 15
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									IN-FLOW:<br> GROWTH MEDIUM (m/s)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										N / A
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										0.58 - 0.34
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							<div class="elementLIQ">
								<p class="elementHeaderLIQ default2">
									OUT-FLOW:<br> GROWTH MEDIUM (m/s)
								</p>	
								<p class="elementBodyLIQ default2">
									<p class="elementValueLIQ default2">
										16.6
									</p>
									<p class="elementRangeLIQ default2">
										SET RANGE:
									</p>
									<p class="elementRangeValueLIQ default2">
										0.58 - 0.34
									</p>
								</p>
								<p class="elementFooterLIQ default2">
									Plot
								</p>	
							</div>
							
						</div>
					</div>
				</div>
				<div id="update" align="center" class="section">
			
					<div class="updateHeader"> 
						UPDATE
					</div> 
					
					<div class = "updateBody">
					<br><br>
						<select>
							<option value="">Select...</option>
							<option value="">Air Pressure (External Atmosphere)</option>
							<option value="">Air Pressure (Internal Atmosphere)</option>
							<option value="">Air Temperature (External Atmosphere)</option>
							<option value="">Air Temperature (Growth Medium)</option>
							<option value="">Air Temperature (Internal Atmosphere)</option>
							<option value="">Carbon Dioxide Partial Pressure (External Atmosphere)</option>
							<option value="">Carbon Dioxide Partial Pressure (Internal Atmosphere)</option>
							<option value="">Dissolved Oxygen (Mixing Tank)</option>
							<option value="">Electrical Conductivity (Leachate)</option>
							<option value="">Electrical Conductivity (Mixing Tank)</option>
							<option value="">Flow Velocity (Growth Medium In-Flow)</option>
							<option value="">Flow Velocity (Growth Medium Out-Flow)</option>
							<option value="">Lighting: PAR (External)</option>
							<option value="">Lighting: PAR (Internal)</option>
							<option value="">Liquid Level (Condensate Tank)</option>
							<option value="">Liquid Level (Mixing Tank)</option>
							<option value="">Liquid Level (Nutrient Tank 1)</option>
							<option value="">Liquid Level (Nutrient Tank 2)</option>
							<option value="">Liquid Level (pH Tank)</option>
							<option value="">Liquid Temperature (Mixing Tank)</option>
							<option value="">Moisture (Growth Medium)</option>
							<option value="">Oxygen Partial Pressure (External Atmosphere)</option>
							<option value="">Oxygen Partial Pressure (Internal Atmosphere)</option>
							<option value="">pH (Leachate)</option>
							<option value="">pH (Mixing Tank)</option>
							<option value="">Relative Humidity (External Atmosphere)</option>
							<option value="">Relative Humidity (Growth Medium)</option>
							<option value="">Relative Humidity (Internal Atmosphere)</option>
						</select>
						<br><br>
						<input type="text" placeHolder = "Set Point" />
						<input type="text" placeHolder = "Setting Time" />
						<input type="text" placeHolder = "Ideal Min" />
						<br>
						<br>
						<input type="text" placeHolder = "Ideal Max" />
						<input type="text" placeHolder = "Tolerable Min" />
						<input type="text" placeHolder = "Tolerable Max" />
					<br><br>
					</div>
					<div class = "updateFooter">
						<input type="button" value="Update HSST" />
					</div>
				</div>
			</div>