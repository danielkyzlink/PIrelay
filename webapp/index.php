<!DOCTYPE html>
<html>
<head>
<title>py rele</title>
<link rel="stylesheet" href="styl.css" type="text/css">
</head>

<body>

<?php
//Load the file
$contents = file_get_contents('rele.json');
 
//Decode the JSON data into a PHP array.
$contentsDecoded = json_decode($contents, true);
 

if (isset($_GET[rele0])){
	if ($_GET[rele0] == "true"){
		$contentsDecoded['rele0'] = true;
	}else{
		$contentsDecoded['rele0'] = false;
	}
}

if (isset($_GET[rele1])){
	if ($_GET[rele1] == "true"){
		$contentsDecoded['rele1'] = true;
	}else{
		$contentsDecoded['rele1'] = false;
	}
}

$rele0 = $contentsDecoded['rele0'];
$rele1 = $contentsDecoded['rele1'];
 
//Encode the array back into a JSON string.
$json = json_encode($contentsDecoded);
 
//Save the file.
file_put_contents('rele.json', $json);

?>


<a href=index.php?rele0=<?php echo(($rele0 ? 'false' : 'true')) ?> class="<?php echo(($rele0 ? 'zapnuto' : 'vypnuto')) ?> relebtn"><div>rele0</div>
<a href=index.php?rele1=<?php echo(($rele1 ? 'false' : 'true')) ?> class="<?php echo(($rele1 ? 'zapnuto' : 'vypnuto')) ?> relebtn"><div>rele1</div>




</body>

</html> 