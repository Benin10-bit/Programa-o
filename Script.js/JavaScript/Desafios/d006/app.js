const botoes = document.querySelectorAll('[id^="botao"]')

// Funções reutilizáveis
function alterarAparencia(elemento, escala, cor) {
    elemento.style.transform = `scale(${escala})`
    elemento.style.backgroundColor = cor
}

function verificaAno() {
    // Variáveis
    const ano = window.prompt('Qual ano você deseja verificar?')
    const analise = document.querySelector('#resultado')
    const num = Number(ano)

    // Verifica se o ano é bissexto
    if ((num % 4 === 0 && num % 100 !== 0) || (num % 400 === 0)) {
        analise.innerHTML = "O ano é BISSEXTO &#9989;"
    } else {
        analise.innerHTML = "O ano não é BISSEXTO &#10060;"
    }
}

// Aplica eventos aos botões
botoes.forEach(botao => {
    botao.addEventListener('mouseenter', () => alterarAparencia(botao, 1.1, '#8A2BE2'))
    botao.addEventListener('mouseout', () => alterarAparencia(botao, 1, '#6A0DAD'))
    botao.addEventListener('click', () => {
        alterarAparencia(botao, 1, '#6A0DAD')
        setTimeout(verificaAno, 100) // Garante que a animação apareça antes do prompt
    })
})
