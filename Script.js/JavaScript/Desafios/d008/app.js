const botao = document.querySelector('#button')

function alterarAparecia(elemento, escala, cor) {
    elemento.style.transform = `scale(${escala})`
    elemento.style.backgroundColor = cor
}

function Media() {
    const res = document.querySelector('#analise')

    // Pede as notas e substitui ',' por '.'
    var nota1 = window.prompt('Primeira nota').replace(',', '.')
    var nota2 = window.prompt('Segunda nota').replace(',', '.')

    // Converte para número após o replace
    var n1 = Number(nota1)
    var n2 = Number(nota2)

    // Verifica se a conversão deu certo
    if (isNaN(n1) || isNaN(n2)) {
        res.innerHTML = 'Insira notas válidas!'
        return
    }

    // Calcula a média
    var media = (n1 + n2) / 2

    // Determina a situação
    var situacao = media > 6 ? 'aprovado' : media > 3 ? 'recuperação' : 'reprovado'

    res.innerHTML = `O aluno está ${situacao}`
}

// Eventos do botão
botao.addEventListener('mouseenter', () => alterarAparecia(botao, 1.1, '#c0c0c0'))
botao.addEventListener('mouseout', () => alterarAparecia(botao, 1, '#dcdcdc'))
botao.addEventListener('click', () => {
    alterarAparecia(botao, 0.8, '#a9a9a9')
    setTimeout(Media, 100)
})
