<?php
$hostname="localhost";
$uname="marsoasis";
$pass="marsoasis";
$dbname="marsoasis";
$con = mysqli_connect($hostname, $uname, $pass,$dbname);
if (mysqli_connect_errno())
  {
  //echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
else{
 //echo "Success: " . mysqli_connect_error();
}
?>