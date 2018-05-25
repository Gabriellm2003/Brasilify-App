<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Brasilify</title>
	
	<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
	<link href="css/indexstyle.css" rel="stylesheet">
	<link href="css/genrestyle.css" rel="stylesheet">
</head>
<body>
	<div>	
		<header>
       <h1 id="page-title">
       <?php       
          require("connection.php"); 
          $query = "SELECT DISTINCT generomusical FROM `liviaab`.`ArtistaGeneroMus` WHERE `generomusical` = ' \"".   $_GET["id"] .'"\'';
      
          $preparedQuery = $conn->prepare($query);
          $preparedQuery->execute();
          $preparedQuery->bind_result($genero);
          while ($preparedQuery->fetch()){
            if(!$genero){
              echo "Genero nao encontrado";
            }else{
              echo str_replace('"', '',$genero); 
            }
          }           
       ?></h1>	
		</header>
		<div class="table-like__container">
		  <div class="table-like__cell table-like__cell--green">
		    <div class="description">
		    	<table class="artist_table">
            <?php
              if($genero){               
               require("connection.php");
               $qryCount = "SELECT COUNT(artista) FROM `liviaab`.`ArtistaGeneroMus` WHERE `generomusical` ='".$genero."'  ";
               //echo $qryCount.'<br>';
               $prdQry = $conn->prepare($qryCount);
               $prdQry->bind_result($numrows);
               $prdQry->execute();
               while($prdQry->fetch()){
                 $result = $numrows;
               }
               //echo $result."<br>";
               
               require("connection.php");
               $query = "SELECT  artista FROM `liviaab`.`ArtistaGeneroMus` WHERE `generomusical` ='".$genero."' ";
               $preparedQuery = $conn->prepare($query);
               $preparedQuery->execute();
               $preparedQuery->bind_result($artista);

	             //echo $query.'<br> ';              
               $resultado = array();
      	       while ($preparedQuery->fetch()){
                 if(!$artista){
                   echo "Nao foram encontrados artistas para esse genero<br>";
                   break;
                 }
                  $resultado[] = $artista;     
      	       }             
               
               require("connection.php");
      	       $query = "SELECT  imagem FROM `liviaab`.`Artistas` WHERE `spotify_id` = ? ";
      	       $auxQuerry = $conn->prepare($query);
      
      	       //$imagens[] = array();
               $imgs = array();
               
      	       for ($i = 0; $i < min(20, count($resultado)); $i++) {
      	       		$auxQuerry->bind_param("s", $resultado[$i]);
      	       		$auxQuerry->execute();
      	       		$auxQuerry->bind_result($imagem);
      	       		$auxQuerry->fetch();                 
                  if (!( $imagem == ' ' )){
         	       		$imagens[] = $imagem;
                    $imgs[] = $imagem;
                    //echo $i." ".$resultado[$i].' - '.$imagem."<br>";
                  }
      	       }
               //print_r($imgs);
               
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
      	      }           
        ?>
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
