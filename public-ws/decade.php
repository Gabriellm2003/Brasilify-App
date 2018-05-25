<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Brasilify</title>
	
	<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
	<link href="css/indexstyle.css" rel="stylesheet">
	<link href="css/decadestyle.css" rel="stylesheet">
</head>
<body>
	<div>
	
		<header>
			<h1><?php       
          echo $_GET["id"];
          
          require("connection.php");
          $aux = strval($_GET["id"]);
                     
       ?></h1>		
		</header>

		
		<div class="table-like__container">
		  <div class="table-like__cell table-like__cell--green">
		    <div class="description">
		    	<br>
		    	<!-- tirei para deixar no mesmo padrao do genero 
            <h2>Ano</h2> 
          -->
		    	<table class="artist_table">
             <tbody>
               <?php
                $aux /= 10;
                require("connection.php");
	              $query = "SELECT DISTINCT imagem FROM `Albuns` WHERE lancamento LIKE ' \"".$aux."%\"' ORDER BY popularidade DESC";
                //echo $query;    	          
                $auxQuery = $conn->prepare($query);
    	       		$auxQuery->execute();
    	       		$auxQuery->bind_result($imagemalb);
               
                                                           
                $imgs  = array();
      	        while($auxQuery->fetch()){                 
                  if (!( $imagemalb == ' ' )){
                    $imgs[] = $imagemalb;
                    //echo $i." ".' - '.$imagemalb."<br>";
                  }
      	        }  
                 //print_r($imgs);
                 if (count($imgs) > 0 ){
                   $i = 0; 
                   $max = min( count($imgs), 12 );              
                   foreach ($imgs as $i => $value) {
                   
                     if( !($value == ' ')){
                       if($i% 4 == 0){
                        echo "<tr>";
                       }
                       echo "<td><img src=".$value."/></td>";
                       if($i%4 == 3){
                         echo "</tr>";
                       }                  
                    
                       $i += 1;                    
                       if( $i == max(12, $max)){
                          break;
                       }
                     }else{
                       $max += 1;
                     }                  
                   }
                 }else{
                   echo "Nao existem albuns para essa decada<br><br>";
                 }
                 
               ?>
            </tbody>
		    	</table>
		    </div>
		  </div>
		</div>	

		<footer>
		<div class="table-like__container">
			<div id="sobre" class="table-like__cell table-like__cell--footer1">Sobre</div>
			<div id="contato" class="table-like__cell table-like__cell--footer2">Contato	</div>			
		</div>
		</footer>
	
	</div>


  <!-- jQuery (necessario para os plugins Javascript do Bootstrap) -->
  <script src="bootstrap/js/jquery-3.1.1.js"></script>
  <script src="bootstrap/js/bootstrap.min.js"></script>
  <script src="js/index.js"></script>
</body>
</html>
