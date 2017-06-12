// Definindo modulo do angularJS
app = angular.module('BlankApp', ['ngMaterial']);

var filtro = document.getElementById('busca');

var tabela = document.getElementById('lista');

// Pesquina na tabela 
if (filtro != null){
    filtro.onkeyup = function() {
        var nomeFiltro = filtro.value.toLowerCase();
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
        console.log($('#'+id).offset().top)
        // Scroll suave
        $('html, body').animate({scrollTop: $('#'+id).offset().top}, 2000);
    }

    // Remove envio formulário com ENTER
    $('input').keypress(function (e) {
        var code = null;
        code = (e.keyCode ? e.keyCode : e.which);                
        return (code == 13) ? false : true;
    });

    // Exibe e esconde botão voltar ao topo
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('a[href="#top"]').fadeIn();
        } else {
            $('a[href="#top"]').fadeOut();
        }
    });

    // Scroll suave ao voltar ao topo
    $('a[href="#top"]').click(function(){
        $('html, body').animate({scrollTop : 0},800);
        return false;
    });
});


