var botao = document.getElementById('botao')
botao.addEventListener('mouseenter', entrar)
botao.addEventListener('mouseout', sair)
botao.addEventListener('click', clicar)
botao.addEventListener('touchstart', tocar)

function entrar(){
    botao.style.transform = 'scale(1.1)'
    botao.style.backgroundColor = '#2E7D32'
    botao.style.color = '#DDEEFF'
}
function sair(){
    botao.style.transform = 'scale(1)'
    botao.style.backgroundColor = ' #4CAF50'
    botao.style.color = ' #F0F8FF'
}
function clicar(){
    botao.style.transform = 'scale(0.9)'
    botao.style.backgroundColor = ' #1B5E20'
    botao.style.color = ' #CCDDFF'
    var nome = window.prompt('Qual nome do item comprado?')
    var val1 = window.prompt('Qual valor do item?')
    var val2 = window.prompt('Qual valor pago?')
    var sub = Number(val2) - Number(val1)
    alert(`Você RECEBERÁ pela compra de/o ${nome} o valor de ${sub.toLocaleString('pt-BR',{style: 'currency', currency: 'USD'})} em troco`)
}
function tocar(){
    botao.style.transform = 'scale(0.9)'
    botao.style.backgroundColor = ' #1B5E20'
    botao.style.color = ' #CCDDFF'
    var nome = window.prompt('Qual nome do item comprado?')
    var val1 = window.prompt('Qual valor do item?')
    var val2 = window.prompt('Qual valor pago?')
    var sub = Number(val2) - Number(val1)
    alert(`Você RECEBERÁ pela compra de/o ${nome} o valor de ${sub.toLocaleString('pt-BR',{style: 'currency', currency: 'EUR'})} em troco`)
}