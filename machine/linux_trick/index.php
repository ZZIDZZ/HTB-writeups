<?php
$file = $_GET['page'];

if(!isset($file) || ($file=="index.php")) {
   include("/var/www/market/home.html");
}
else{
	include("/var/www/market/".str_replace("../","",$file));
}
?>