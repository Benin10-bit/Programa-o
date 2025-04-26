var botao = document.getElementById('button')

botao.addEventListener('mouseenter', entrar)
botao.addEventListener('mouseout', sair)
botao.addEventListener('click', click)

function entrar(){
    botao.style.transform = 'scale(1.1)'
    botao.style.backgroundColor = '#1E73AD'
}
function sair(){
    botao.style.transform = 'scale(1)'
    botao.style.backgroundColor = '#2A95E1'
}
function click(){
    botao.style.transform = 'scale(0.9)'
    botao.style.backgroundColor = '#14527C'
    var prompt = window.prompt('Digite um número:')
    alert(`O número antecessor é ${Number(prompt)-1} e o sucessor é ${Number(prompt)+1}`)
}
