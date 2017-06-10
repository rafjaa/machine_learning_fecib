// Definindo modulo do angularJS
app = angular.module('BlankApp', ['ngMaterial']);

var filtro = document.getElementById('busca');

var tabela = document.getElementById('lista');

// Pesquina na tabela 
if (filtro != null){
    filtro.onkeyup = function() {
        var nomeFiltro = filtro.value;
        for (var i = 1; i < tabela.rows.length; i++) {
            
            var nome = tabela.rows[i].cells[1].innerText;
          	var curso = tabela.rows[i].cells[2].innerText;
            var vinho = tabela.rows[i].cells[4].innerText;

            var corresponde = nome.toLowerCase().indexOf(nomeFiltro) >= 0 || 
                                curso.toLowerCase().indexOf(nomeFiltro) >= 0 ||
                                vinho.toLowerCase().indexOf(nomeFiltro) >= 0;
            
            tabela.rows[i].style.display = corresponde ? '' : 'none';
        }
    };
}

$(document).ready(function(){
    id = $('#id').val()
    //Scroll suave
    if(id != 'None' && id != undefined){
        // css
        $('#'+id).css('background-color', '#b3b3ff');
    
        // Scroll suave
        $('html,body').animate({scrollTop: $('#'+id).offset().top}, 2000);
    }
});
