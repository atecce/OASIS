<?php

	header("Content-Type: application/json", true);
	require_once ('../utils/connection.php');
	$con = $GLOBALS['con'];
	
	$id = $_POST['id'];
	$user_id  = $_POST['user_id'];
	$json_array['user_id'] = $user_id;
	
	$json_array['id'] = $id;

	
	$v3=$v4=0;
	$p1=$p2=$p3=$p4=$p5=$p6=$p7=$p9=$p10=$p11=$p12=0;
	$m1=$m2=$m6=$m7=$m8=$m18=0;
	$f1=0;
	$la=$st=0;
	
	/*(id.indexOf("save_check") > -1)
	(id.indexOf("save_reset") > -1)
	(id.indexOf("save_start") > -1)
	(id.indexOf("save_stop") > -1)
	(id.indexOf("save_pumps") > -1)
	(id.indexOf("save_valves") > -1)*/
	if(strcmp($id,"save_check") == 0)
	{
		$v1=intval($_POST['v1']);
		$v2=intval($_POST['v2']);
		$v3=intval($_POST['v3']);
		$v4=intval($_POST['v4']);
		$v5=intval($_POST['v5']);
		$v6=intval($_POST['v6']);
		$v7=intval($_POST['v7']);
		$sql10 = "INSERT INTO valves (id,v1,v2,v3,v4,v5,v6,v7,time_stamp,user_id)
								  VALUES (null,".$v1.",".$v2.",".$v3.",".$v4.",".$v5.",".$v6.",".$v7.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql10);
		$p1=intval($_POST['p1']);
		$p2=intval($_POST['p2']);
		$p3=intval($_POST['p3']);
		$p4=intval($_POST['p4']);
		$p5=intval($_POST['p5']);
		$p6=intval($_POST['p6']);
		$p7=intval($_POST['p7']);
		$p8=intval($_POST['p8']);
		$p9=intval($_POST['p9']);
		$p10=intval($_POST['p10']);
		$p11=intval($_POST['p11']);
		$p12=intval($_POST['p12']);	
		$sql20 = "INSERT INTO pumps (id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,time_stamp,user_id)
								  VALUES (null,".$p1.",".$p2.",".$p3.",".$p4.",".$p5.",".$p6.",".$p7.",".$p8.",".$p9.",".$p10.",".$p11.",".$p12.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql20);
		/*$json_array['v1'] = $v1;
		$json_array['v2'] = $v2;
		$json_array['v3'] = $v3;
		$json_array['v4'] = $v4;
		$json_array['v5'] = $v5;
		$json_array['v6'] = $v6;	
		$json_array['v7'] = $v7;
		$json_array['p1'] = $p1;
		$json_array['p2'] = $p2;
		$json_array['p3'] = $p3;
		$json_array['p4'] = $p4;
		$json_array['p5'] = $p5;	
		$json_array['p6'] = $p6;
		$json_array['p7'] = $p7;
		$json_array['p8'] = $p8;
		$json_array['p9'] = $p9;
		$json_array['p10'] = $p10;
		$json_array['p11'] = $p11;
		$json_array['p12'] = $p12;*/
	}
	else if(strcmp($id,"save_reset") == 0)
	{
		$v1=intval($_POST['v1']);
		$v2=intval($_POST['v2']);
		$v3=intval($_POST['v3']);
		$v4=intval($_POST['v4']);
		$v5=intval($_POST['v5']);
		$v6=intval($_POST['v6']);
		$v7=intval($_POST['v7']);
		$sql11 = "INSERT INTO valves (id,v1,v2,v3,v4,v5,v6,v7,time_stamp,user_id)
								  VALUES (null,".$v1.",".$v2.",".$v3.",".$v4.",".$v5.",".$v6.",".$v7.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql11);
		$p1=intval($_POST['p1']);
		$p2=intval($_POST['p2']);
		$p3=intval($_POST['p3']);
		$p4=intval($_POST['p4']);
		$p5=intval($_POST['p5']);
		$p6=intval($_POST['p6']);
		$p7=intval($_POST['p7']);
		$p8=intval($_POST['p8']);
		$p9=intval($_POST['p9']);
		$p10=intval($_POST['p10']);
		$p11=intval($_POST['p11']);
		$p12=intval($_POST['p12']);	
		$sql21 = "INSERT INTO pumps (id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,time_stamp,user_id)
								  VALUES (null,".$p1.",".$p2.",".$p3.",".$p4.",".$p5.",".$p6.",".$p7.",".$p8.",".$p9.",".$p10.",".$p11.",".$p12.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql21);
		/*$json_array['v1'] = $v1;
		$json_array['v2'] = $v2;
		$json_array['v3'] = $v3;
		$json_array['v4'] = $v4;
		$json_array['v5'] = $v5;
		$json_array['v6'] = $v6;	
		$json_array['v7'] = $v7;
		$json_array['p1'] = $p1;
		$json_array['p2'] = $p2;
		$json_array['p3'] = $p3;
		$json_array['p4'] = $p4;
		$json_array['p5'] = $p5;	
		$json_array['p6'] = $p6;
		$json_array['p7'] = $p7;
		$json_array['p8'] = $p8;
		$json_array['p9'] = $p9;
		$json_array['p10'] = $p10;
		$json_array['p11'] = $p11;
		$json_array['p12'] = $p12;*/
	}	
	else if(strcmp($id,"save_start") == 0)
	{
		$start = intval($_POST['start']);
		$stop = intval($_POST['stop']);
		$sql3 = "INSERT INTO mars (id,start,stop,time_stamp,user_id)
								  VALUES (null,".$start.",".$stop.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql3);
		/*$json_array['start'] = $start;
		$json_array['stop'] = $stop;*/
	}
	else if(strcmp($id,"save_stop") == 0)
	{
		$start = intval($_POST['start']);
		$stop = intval($_POST['stop']);
		$sql4 = "INSERT INTO mars (id,start,stop,time_stamp,user_id)
								  VALUES (null,".$start.",".$stop.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql4);
		/*$json_array['start'] = $start;
		$json_array['stop'] = $stop;*/
	}
	else if(strcmp($id,"save_WFC") == 0)
	{
		$p1=intval($_POST['p1']);
		$p2=intval($_POST['p2']);	
		$sql5 = "INSERT INTO water_flow_control (id,p1,p2,time_stamp,user_id)
								  VALUES (null,".$p1.",".$p2.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql5);
		/*$json_array['p1'] = $p1;
		$json_array['p2'] = $p2;*/
	}
	else if(strcmp($id,"save_WC") == 0)
	{
		$m1=intval($_POST['m1']);
		$m2=intval($_POST['m2']);
		$p3=intval($_POST['p3']);
		$p4=intval($_POST['p4']);
		$p5=intval($_POST['p5']);
		$sql5 = "INSERT INTO water_conditioning (id,m1,m2,p3,p4,p5,time_stamp,user_id)
								  VALUES (null,".$m1.",".$m2.",".$p3.",".$p4.",".$p5.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql5);
		/*$json_array['m1'] = $m1;
		$json_array['m2'] = $m2;
		$json_array['p3'] = $p3;
		$json_array['p4'] = $p4;
		$json_array['p5'] = $p5;*/
	}
	else if(strcmp($id,"save_AM") == 0)
	{
		$p10=intval($_POST['p10']);
		$p12=intval($_POST['p12']);
		$v3=intval($_POST['v3']);
		$v4=intval($_POST['v4']);
		$m6=intval($_POST['m6']);
		$m7=intval($_POST['m7']);
		$m8=intval($_POST['m8']);	
		$sql5 = "INSERT INTO atmospheric_management (id,p10,p12,v3,v4,m6,m7,m8,time_stamp,user_id)
								  VALUES (null,".$p10.",".$p12.",".$v3.",".$v4.",".$m6.",".$m7.",".$m8.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql5);
		/*$json_array['p10'] = $p10;
		$json_array['p12'] = $p12;
		$json_array['v3'] = $v3;
		$json_array['v4'] = $v4;	
		$json_array['m6'] = $m6;
		$json_array['m7'] = $m7;
		$json_array['m8'] = $m8;*/
	}
	else if(strcmp($id,"save_LI") == 0)
	{
		$la=intval($_POST['la']);
		$st=intval($_POST['st']);
		$m18=intval($_POST['m18']);	
		$sql5 = "INSERT INTO lighting_and_imagery (id,la,st,m18,time_stamp,user_id)
								  VALUES (null,".$la.",".$st.",".$m18.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql5);
		/*$json_array['la'] = $la;
		$json_array['st'] = $st;
		$json_array['m18'] = $m18;*/
	}
	else if(strcmp($id,"save_SM") == 0)
	{
		$p6=intval($_POST['p6']);
		$p7=intval($_POST['p7']);
		$p9=intval($_POST['p9']);
		$p11=intval($_POST['p11']);
		$f1=intval($_POST['f1']);
		$sql6 = "INSERT INTO system_maintenance (id,p6,p7,p9,p11,f1,time_stamp,user_id)
								  VALUES (null,".$p6.",".$p7.",".$p9.",".$p11.",".$f1.",CURRENT_TIMESTAMP,'".$user_id."')";
		mysqli_query($con,$sql6);//mysql_query($sql);						  
		/*$json_array['p6'] = $p6;
		$json_array['p7'] = $p7;
		$json_array['p9'] = $p9;
		$json_array['p11'] = $p11;
		$json_array['f1'] = $f1;*/
	}
	
	
	echo json_encode($json_array);
	exit();
		

?>