//Atribuindo variáveis às divs
var div1 = document.getElementById('botao1')
var div2 = document.getElementById('botao2')
var div3 = document.getElementById('botao3')
//Adiciona a escuta de objetos DOM
div1.addEventListener('mouseenter', entrar1)
div2.addEventListener('mouseenter', entrar2)
div3.addEventListener('mouseenter', entrar3)
div1.addEventListener('mouseout', sair1)
div2.addEventListener('mouseout', sair2)
div3.addEventListener('mouseout', sair3)
div1.addEventListener('click', clicar1)
div2.addEventListener('click', clicar2)
div3.addEventListener('click', clicar3)
//funções da div 1
function entrar1(){
 div1.style.transform = 'scale(1.1)'
 div1.style.backgroundColor = '#007777'
}
function sair1(){
 div1.style.transform = 'scale(1)'
 div1.style.backgroundColor = 'aqua'
}
function clicar1(){
 alert('Botão 1')
}
//Funções da div 2
function entrar2(){
    div2.style.transform = 'scale(1.1)'
    div2.style.backgroundColor = '#007777'
 }
 function sair2(){
     div2.style.transform = 'scale(1)'
     div2.style.backgroundColor = 'aqua'
 }
 function clicar2(){
  alert('Botão 2')
 }
 //Funções da div 3
 function entrar3(){
     div3.style.transform = 'scale(1.1)'
     div3.style.backgroundColor = '#007777'
 }
 function sair3(){
     div3.style.transform = 'scale(1)'
     div3.style.backgroundColor = 'aqua'
 }
 function clicar3(){
  alert('Botão 3')
 }
 