class PIN:

	def __init__(self, number, proc, name, modes):

		self.number = number
		self.proc   = proc
		self.name   = name
		self.modes  = modes
		
P8_01 = PIN("P8_01", None,  "GND",       ( None,            None,         None,               None,               None,                   None,                None,               None))
P8_02 = PIN("P8_02", None,  "GND",       ( None,            None,         None,               None,               None,                   None,                None,               None))
P8_03 = PIN("P8_03", "R9",  "GPIO1_6",   ("gpmc_ad6",      "mmc1_dat6",   None,               None,               None,                   None,                None,              "gpio1[6]"))
P8_04 = PIN("P8_04", "T9",  "GPIO1_7",   ("gpmc_ad7",      "mmc1_dat7",   None,               None,               None,                   None,                None,              "gpio1[7]"))
P8_05 = PIN("P8_05", "R8",  "GPIO1_2",   ("gpmc_ad2",      "mmc1_dat2",   None,               None,               None,                   None,                None,              "gpio1[2]"))
P8_06 = PIN("P8_06", "T8",  "GPIO1_3",   ("gpmc_ad3",      "mmc1_dat3",   None,               None,               None,                   None,                None,              "gpio1[3]"))
P8_07 = PIN("P8_07", "R7",  "TIMER4",    ("gpmc_advn_a",    None,        "timer4",            None,               None,                   None,                None,              "gpio2[2]"))
P8_08 = PIN("P8_08", "T7",  "TIMER7",    ("gpmc_oen_re",    None,        "timer7",            None,               None,                   None,                None,              "gpio2[3]"))
P8_09 = PIN("P8_09", "T6",  "TIMER5",    ("gpmc_be0n_c",    None,        "timer5",            None,               None,                   None,                None,              "gpio2[5]"))
P8_10 = PIN("P8_10", "U6",  "TIMER6",    ("gpmc_wen",      "timer6",      None,               None,               None,                   None,                None,              "gpio2[4]"))
P8_11 = PIN("P8_11", "R12", "GPIO1_13",  ("gpmc_ad13",     "lcd_data18", "mmc1_dat5",        "mmc2_dat1",        "eQEP2B_in",             None,               "pr1_pru0_pru_r30", "gpio2[13]"))
P8_12 = PIN("P8_12", "T12", "GPIO1_12",  ("gpmc_ad12",     "Lcd_data19", "mmc1dat4",         "Mmc2_dat0",        "Eqep2a_in",             None,               "pr1_pru0_pru_r30", "gpio2[12]"))
P8_13 = PIN("P8_13", "T10", "EHRPWM2B",  ("gpmc_ad9",      "lcd_data22", "mmc1dat1",         "mmc2_dat5",        "ehrpwm2b",              None,                None,              "gpio0[23]"))
P8_14 = PIN("P8_14", "T11", "GPIO0_26",  ("gpmc_ad10",     "lcd_data21", "mmc1dat2",         "mmc2_dat6",        "ehrpwm2b_tripzone_in",  None,                None,              "gpio0[26]"))
P8_15 = PIN("P8_15", "U13", "GPIO1_15",  ("gpmc_ad15",     "lcd_data16", "mmc1dat7",         "mmc2_dat3",        "eQEP2_strobe",          None,               "pr1_pru0_pru_r31", "gpio1[15]"))
P8_16 = PIN("P8_16", "V13", "GPIO1_14",  ("gpmc_ad14",     "lcd_data17", "mmc1_dat6",        "mmc2_dat2",        "eQEP2_index",           None,               "pr1_pru0_pru_r31", "gpio1[14]"))
P8_17 = PIN("P8_17", "U12", "GPIO0_27",  ("gpmc_ad11",     "lcd_data20", "mmc1_dat3",        "mmc2_dat7",        "ehrpwm0_synco",         None,                None,              "gpio0[27]"))
P8_18 = PIN("P8_18", "V12", "GPIO2_1",   ("gpmc_clk_mu",   "lcd_memory", "gpmc_wait1",       "mmc2_clk",          None,                   None,               "mcasp0_fsr",       "gpio2[1]"))
P8_19 = PIN("P8_19", "U10", "EHRPWM2A",  ("gpmc_ad8",      "lcd_data23", "mmc1_dat0",        "mmc2_dat4",        "ehrpwm2A",              None,                None,              "gpio0[22]"))
P8_20 = PIN("P8_20", "V9",  "GPIO1_31",  ("gpmc_csn2",     "gpcm_be1n",  "mmc1_cmd",          None,               None,                  "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio1[31]"))
P8_21 = PIN("P8_21", "U9",  "GPIO1_30",  ("gpmc_csn1",     "gpmc_clk",   "mmc1_clk",          None,               None,                  "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio1[30]"))
P8_22 = PIN("P8_22", "V8",  "GPIO1_5",   ("gpmc_ad5",      "mmc1_dat5",   None,               None,               None,                   None,                None,              "gpio1[5]"))
P8_23 = PIN("P8_23", "U8",  "GPIO1_4",   ("gpmc_ad4",      "mmc1_dat4",   None,               None,               None,                   None,                None,              "gpio1[4]"))
P8_24 = PIN("P8_24", "V7",  "GPIO1_1",   ("gpmc_ad1",      "mmc1_dat1",   None,               None,               None,                   None,                None,              "gpio1[1]"))
P8_25 = PIN("P8_25", "U7",  "GPIO1_0",   ("gpmc_ad0",      "mmc1_dat0",   None,               None,               None,                   None,                None,              "gpio1[0]"))
P8_26 = PIN("P8_26", "V6",  "GPIO1_29",  ("gpmc_csn0",      None      ,   None,               None,               None,                   None,                None,              "gpio1[29]"))
P8_27 = PIN("P8_27", "U5",  "GPIO1_22",  ("lcd_vsync",     "gpmc_a8"  ,   None,               None,               None,                  "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[22]"))
P8_28 = PIN("P8_28", "V5",  "GPIO2_24",  ("lcd_pclk",      "gpmc_a10" ,   None,               None,               None,                  "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[24]"))
P8_29 = PIN("P8_29", "R5",  "GPIO2_23",  ("lcd_hsync",     "gpmc_a9" ,    None,               None,               None,                  "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[23]"))
P8_30 = PIN("P8_30", "R6",  "GPIO2_25",  ("lcd_ac_bias_e", "gpmc_a11" ,   None,               None,               None,                   None,                None,              "gpio2[25]"))
P8_31 = PIN("P8_31", "V4",  "UART5_CTS", ("lcd_data14",    "gpmc_a18" ,  "qEP1_index",       "mcasp0_axr1",      "uart5_rxd",             None,               "uart5_ctsn",       "gpio0[10]"))
P8_32 = PIN("P8_32", "T5",  "UART5_RTS", ("lcd_data15",    "gpmc_a19" ,  "qEP1_strobe",      "mcasp0_ahclkx",    "mascp0_axr3",           None,               "uart5_rtsn",       "gpio0[11]"))
P8_33 = PIN("P8_33", "V3",  "UART4_RTS", ("lcd_data13",    "gpmc_a17" ,  "qEP1B_in",         "mcasp0_fsr",       "mascp0_axr3",           None,               "uart4_rtsn",       "gpio0[9]"))
P8_34 = PIN("P8_34", "U4",  "UART3_RTS", ("lcd_data11",    "gpmc_a15" ,  "ehrpwm1B",         "mcasp0_ahclkr",    "mascp0_axr2",           None,               "uart3_rtsn",       "gpio2[17]"))
P8_35 = PIN("P8_35", "V2",  "UART4_CTS", ("lcd_data12",    "gpmc_a16" ,  "eQEP1A_in",        "mcasp0_aclkr",     "mascp0_axr2",           None,               "uart4_ctsn",       "gpio0[8]"))
P8_36 = PIN("P8_36", "U3",  "UART3_CTS", ("lcd_data10",    "gpmc_a14" ,  "ehrpwm1A",         "mcasp0_axr0",       None,                   None,               "uart3_ctsn",       "gpio2[16]"))
P8_37 = PIN("P8_37", "U1",  "UART5_TXD", ("lcd_data8",     "gpmc_a12" ,  "ehrpwm1_tripzone", "mcasp0_aclkx",     "uart5_txd",             None,               "uart2_ctsn",       "gpio2[14]"))
P8_38 = PIN("P8_38", "U2",  "UART5_RX",  ("lcd_data9",     "gpmc_a13" ,  "ehrpwm0_synco",    "mcasp0_fsx",       "uart5_rxd",             None,               "uart2_rtsn",       "gpio2[15]"))
P8_39 = PIN("P8_39", "T3",  "GPIO2_12",  ("lcd_data6",     "gpmc_a6" ,   None,               "eQEP2_index",       None,                   "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[12]"))
P8_40 = PIN("P8_40", "T4",  "GPIO2_13",  ("lcd_data7",     "gpmc_a7" ,   None,               "eQEP2_strobe",     "pr1_edio_data_out",     "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[13]"))
P8_41 = PIN("P8_41", "T1",  "GPIO2_10",  ("lcd_data4",     "gpmc_a4" ,   None,               "eQEP2A_in",         None,                   "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[10]"))
P8_42 = PIN("P8_42", "T2",  "GPIO2_11",  ("lcd_data5",     "gpmc_a5" ,   None,               "eQEP2B_in",         None,                   "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[11]"))
P8_43 = PIN("P8_43", "R3",  "GPIO2_8",   ("lcd_data2",     "gpmc_a2" ,   None,               "ehrpwm2_tripzone",  None,                   "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[8]"))
P8_44 = PIN("P8_44", "R4",  "GPIO2_9",   ("lcd_data3",     "gpmc_a3" ,   None,               "ehrpwm0_synco",     None,                   "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[9]"))
P8_45 = PIN("P8_45", "R1",  "GPIO2_6",   ("lcd_data0",     "gpmc_a0" ,   None,               "ehrpwm2A",          None,                   "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[6]"))
P8_46 = PIN("P8_46", "R2",  "GPIO2_7",   ("lcd_data1",     "gpmc_a1" ,   None,               "ehrpwm2B",          None,                   "pr1_pru1_pru_r30",  "pr1_pru1_pru_r31", "gpio2[7]"))

pins = (P8_01, P8_02, P8_03, P8_04, P8_05, P8_06, P8_07, P8_08, P8_09, P8_10, 
        P8_11, P8_12, P8_13, P8_14, P8_15, P8_16, P8_17, P8_18, P8_19, P8_20, 
        P8_21, P8_22, P8_23, P8_24, P8_25, P8_26, P8_27, P8_28, P8_29, P8_30, 
        P8_31, P8_32, P8_33, P8_34, P8_35, P8_36, P8_37, P8_38, P8_39, P8_40, 
        P8_41, P8_42, P8_43, P8_44, P8_45, P8_46)

for pin in pins:

	print pin.number, str(pin.proc), pin.name,

	for mode in pin.modes: print mode,

	print
