<?php
	$msg = "-----Success----";	
	if(isset($_SESSION['loginMsg']))
	{
		$msg = $_SESSION['loginMsg'];
	}	
?>
<script type = "text/javascript">

	var msg = <?php echo json_encode($msg); ?>;
	if(msg != "-----Success----")
	{
		alert("LOGIN MESSAGE = '"+msg+"'");	
		var msg1 = <?php unset($_SESSION['recoverMsg']);
						 unset($_SESSION['loginMsg']);
						 unset($_SESSION['registerMsg']);
					?>
		msg = "-----Success----";
	}
		
	//alert (msg1);
</script>