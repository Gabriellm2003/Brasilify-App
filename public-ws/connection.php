<?php
	$servername = 'mysql.dcc.ufmg.br';
	$username = 'liviaab';
	$password = 'sunshine.2441';

	$conn = new mysqli($servername, $username, $password, 'liviaab');
	//Check connection
	if($conn->connect_error){   
		die("Nao foi possivel se conectar ao BD" . $conn->connect_error);
	};

?>