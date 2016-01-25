<?php
	$msg = "-----Success----";	
	if(isset($_SESSION['recoverMsg']))
	{
		$msg = $_SESSION['recoverMsg'];
	}	
?>
<script type = "text/javascript">

	var msg = <?php echo json_encode($msg); ?>;
	if(msg != "-----Success----")
	{
		alert("RECOVER MESSAGE = '"+msg+"'");	
		var msg1 = <?php unset($_SESSION['recoverMsg']);
						 unset($_SESSION['loginMsg']);
						 unset($_SESSION['registerMsg']);
					?>
		msg = "-----Success----";
	}
	
</script>