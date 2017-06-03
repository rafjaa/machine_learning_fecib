// Definindo modulo do angularJS
app = angular.module('BlankApp', ['ngMaterial']);

// Pesquina na tabela 
var filtro = document.getElementById('busca');

var tabela = document.getElementById('lista');
filtro.onkeyup = function() {
    var nomeFiltro = filtro.value;
    console.log('nome do filtro ' + nomeFiltro)
    for (var i = 1; i < tabela.rows.length; i++) {
        
        var nome = tabela.rows[i].cells[1].innerText;
      	var curso = tabela.rows[i].cells[2].innerText;

        var corresponde = nome.toLowerCase().indexOf(nomeFiltro) >= 0 || curso.toLowerCase().indexOf(nomeFiltro) >= 0;
        
        tabela.rows[i].style.display = corresponde ? '' : 'none';
    }
};

//Âncora
document.addEventListener("DOMContentLoaded", function(event) {
	console.log("DOM completamente carregado e analisado" + event);
	
    posicao = document.getElementById('posicao').value;
    document.getElementById(posicao).style.background = '#b3b3ff';

    window.location.href = "#" + posicao ;
});