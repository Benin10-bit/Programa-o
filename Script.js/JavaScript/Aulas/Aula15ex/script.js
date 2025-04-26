var lnum = []
const section = document.querySelector('#lnum')
function addNum(){
    const input = document.querySelector('#count').value
    
    if (1 > input || input > 100  ){
        alert('Insira números válidos')
        document.querySelector('#count').value = ''
        return;
    }
    
    lnum.push(Number(input))

    let opt = document.createElement('option')
    opt.innerHTML = `O número ${input} foi adicionado!`

    section.appendChild(opt)
    document.querySelector('#count').value = ''

    
}
function verify(){
    const res = document.querySelector('.res')

    let length = lnum.length
    let max = Math.max(...lnum)
    let min = Math.min(...lnum)
    let soma = lnum.reduce((total, num) => total + num, 0)
    let media = soma / length

    res.innerHTML = `Ao todo temos ${length} números cadastrados <br>
    O maior número é ${max} e o menor é ${min}<br>
    Somando todos temos ${soma}<br>
    A média dos números é ${media}`

    lnum = []
    while (section.firstChild) {
        section.removeChild(section.firstChild);
    }
}
function teste(){
    console.log(lnum)
}
