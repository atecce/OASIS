



def initTrue():
	P11.activate()
	P7.activate()
	UVF2.activate()
	FanM6.activate()
	FanM7.activate()
	#let loop run for 10 seconds:
		humidP10.activate()
	NPK1P6.activate()
	NPK2P9.activate()
# If level S105 is greater than [HSST_M21]
if S105 > [HSST_M21]: 
	initTrue()
	conMonitoringAndTrouble()
	waterHeating()
	nutrientConditioning()
	pHConditioning()
# Set system mode to germinate

# Activate!
# Run continuous monitoring and troubleshooting
# Run Water heating/cooling function
# Run Nutrient condition function
# Run pH conditioning function

# activate main pump P1
	mainP1.activate()
	while S105 <= [HSST_M21]:
		# deactivate Main pump P1
		mainP1.deactivate()


# set system mode autonomous
# set time of day
# set more shit
# Run time lapse function
# Run day cycle function
# run autooperate
