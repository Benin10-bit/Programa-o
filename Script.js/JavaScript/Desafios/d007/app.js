const botoes = document.querySelectorAll('#button')

//Função reutilizável
function alterarAparencia(elemento, escala, cor) {
    elemento.style.transform = `scale(${escala})`
    elemento.style.backgroundColor = cor
}

function mudancaPreco() {
    const tittle = document.querySelector('#resposta')
    const resposta = document.querySelector('#res')

    var num1 = Number(window.prompt('Qual o preço antigo do produto?'))
    var num2 = Number(window.prompt('Qual o valor atual?'))

    var n1 = num1.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
    var n2 = num2.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })

    var aumento = num1 > num2 ? 'barato' : 'caro'

    var diferenca = Math.abs(num1 - num2)
    var subiu = diferenca.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })

    var variacao = ((diferenca / num1) * 100).toFixed(2).replace('.', ',')

    tittle.innerHTML = `<strong>ANALISANDO OS VALORES INFORMADOS</strong>`
    resposta.innerHTML = `
        O produto custava ${n1} e agora custa ${n2}.<br>
        Hoje o produto está mais ${aumento}.<br>
        O preço mudou em ${subiu} em relação ao preço anterior.<br>
        Uma variação de ${variacao}% pra ${aumento === 'barato' ? 'baixo' : 'cima'}.
    `
}

botoes.forEach(ret => {
    ret.addEventListener('mouseenter', () => alterarAparencia(ret, 1.1, '#8A2BE2'))
    ret.addEventListener('mouseout', () => alterarAparencia(ret, 1, '#6A0DAD'))
    ret.addEventListener('click', () => {
        alterarAparencia(ret, 0.8, '#4B0082')
        setTimeout(mudancaPreco, 100)
    })
})
