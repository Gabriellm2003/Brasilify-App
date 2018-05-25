$(document).ready(function() {
    var genero = 0;
    var decada = 0;
		$('#sel_genero').change(function() {
			genero = $(this).val();
      window.location.href = 'genre.php?id='+genero;
		});
	
		$('#sel_decadas').change(function() {
			decada = $(this).val();
      window.location.href = "decade.php?id=" + decada;
		});	
   
    $('#sobre').click(function(){
      window.location.href = 'sobre.php';
    }).mouseenter(function(){
      $(this).css("background-color", '#C3F0B7');
    }).mouseleave(function(){
      $(this).css("background-color", 'white');
    });
    $('#contato').click(function(){
      window.location.href = 'contato.php';
    }).mouseenter(function(){
      $(this).css("background-color", '#FFFDA7');
    }).mouseleave(function(){
      $(this).css("background-color", 'white');
    });;
     
	});

  
	window.onload=function() {
		document.getElementById('genre_form').onsubmit=function() {
			window.location.href = 'genre.php?id='+genero;
      //window.location.replace("genre.php?id=" + genero);
			return false;
		};
		
		document.getElementById('decade_form').onsubmit=function() {
      window.location.href = "decade.php?id=" + decada;
			//window.location.replace("decade.php?id=" + decada);
			return false;
		};
  
	};