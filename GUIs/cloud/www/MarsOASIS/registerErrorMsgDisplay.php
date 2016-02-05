<?php
	$msg = "-----Success----";	
	if(isset($_SESSION['registerMsg']))
	{
		$msg = $_SESSION['registerMsg'];
	}	
?>
<script type = "text/javascript">

	var msg = <?php echo json_encode($msg); ?>;
	if(msg != "-----Success----")
	{
		alert("REGISTER MESSAGE = '"+msg+"'");	
		var msg1 = <?php unset($_SESSION['recoverMsg']);
						 unset($_SESSION['loginMsg']);
						 unset($_SESSION['registerMsg']);
					?>
		msg = "-----Success----";
	}
	
</script>