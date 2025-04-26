function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.querySelector('#num')
    var res = document.querySelector('#res')

    if (fano.value <= 0 || Number(fano.value) > ano){
        alert('[ERRO] Insira números válidos')
    }
    else{
        var fsex = document.getElementsByClassName('sexo')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')

        if (fsex[0].checked){
            genero = 'homem'
        }
        else{
            genero = 'Mulher'
        }
    }
}