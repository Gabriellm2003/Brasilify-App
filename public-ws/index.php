<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Brasilify</title>
	
	<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
	<link href="css/indexstyle.css" rel="stylesheet">
</head>
<body>
	<div>	
		<header>
			<h1>Brasilify</h1>	
		</header>

		<div class="table-like__container">
		  <div class="table-like__cell table-like__cell--green">
		   		<div clas="middle" >
		    		<p>Quer saber mais sobre a cultura brasileira?<br>Pesquisa aí! :D</p>
		   		</div>
		   
		  </div>
		  <div class="table-like__cell table-like__cell--yellow">		    
		    	<div class=" middle ">				
	    			<p>Selecione um gênero </p>
		    		<?php    						
    						require("connection.php");                
                $query = "SELECT DISTINCT generomusical FROM ArtistaGeneroMus";
                $preparedQuery = $conn->prepare($query);
                $preparedQuery->execute();
                $preparedQuery->bind_result($genero);
		echo "<form id='genre_form'>";
		echo "<select id='sel_genero'>";
                echo "<option value='empty'> </option>";
                while ($preparedQuery->fetch()) {
                  echo "<option value=".$genero."> ". str_replace('"','' , $genero)."</option>"; 
		}
		echo "</select>";
		//echo "<br><input type='submit' id='genre_submit' value='Pesquisar'>";
		echo "</form><br>";

		?>
		
		<p>OU</p>
    		<p>uma década</p>  
           <?php
             require("connection.php");
             $query = "SELECT DISTINCT decada FROM Decadas ORDER BY decada";
             $preparedQuery = $conn->prepare($query);
      	     $preparedQuery->execute();
      	     echo "<form id='decade_form'>";
      	     echo "<select id='sel_decadas'>";
             echo "<option value='empty'> </option>";
             $preparedQuery->bind_result($decada);
             while ($preparedQuery->fetch()) {
                  echo "<option value=\"". $decada ."\">".$decada."  </option> "; 
             }

      	     echo "</select>";
      	     //echo "<br><input type='submit' name='decade_submit' value='Pesquisar'>";
      	     echo "</form><br>";
      	     mysqli_close($conn);
          ?>
                   
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
