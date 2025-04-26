const botao = document.querySelectorAll('[class^="button"]')

//Função reutilizável
function alterarEstilo(elemento,escala,cor){
    elemento.style.transform = `scale(${escala})`
    elemento.style.backgroundColor = cor
}

//Função para converter em metros
function converterMetros(){
    const resposta = document.querySelector('#resposta')
    const res = document.querySelector('#res')

   const prompt =  window.prompt('Escolha um número em metros para a conversão')

   resposta.innerHTML = `O valor de <span style = color:"#4B0082">${Number(prompt)}</span> em metros corresponde a:`
   var num = Number(prompt)

   res.innerHTML = `
   ${num/1000} KM <br> 
   ${num/100} HM <br>
   ${num/10} DAM <br>
   ${num*10} DM <br>
   ${num*100} CM <br>
   ${num*1000} MM`
   
}
//Loop

botao.forEach(ret =>{
    ret.addEventListener('mouseenter', ()=> alterarEstilo(ret,1.1,'#9B30C8'))
    ret.addEventListener('mouseout', ()=> alterarEstilo(ret,1,'#6A1B9A'))
    ret.addEventListener('click', ()=>{ 
        alterarEstilo(ret,0.8,'#5A007E')
        setTimeout(converterMetros,100)
    })
})