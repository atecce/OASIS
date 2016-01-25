<?php
	include("../utils/connection.php");
	// Inialize session
	session_start();

	// Delete certain session
	unset($_SESSION['userEmail']);
	unset($_SESSION['userLogin']);;
	unset($_SESSION['msg']);
	unset($_SESSION['loginSuccess']);
	// Jump to login page
	header('Location: ../../index.php');
?>
