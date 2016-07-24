<?php
$data = json_decode(file_get_contents("php://input"));
$username='root';
$server='localhost';
$password='';
$database='trade';
$con = new mysqli($server,$username,$password,$database);
$m = $data->subEmail;
$Q="INSERT INTO subscribe (Email)
VALUES ('$m')";
if($con->query($Q)===TRUE)
{
	
}
else {
    $d = array('msg'=>'false');
}
  	$d = array('msg'=>'true');
	$jsn = json_encode($d);
        print_r($jsn);
$con->close();
?>