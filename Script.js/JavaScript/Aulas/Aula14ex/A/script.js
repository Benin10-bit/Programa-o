function sequencia(){
    const start = Number(document.querySelector('#start-count').value)
    const end = Number(document.querySelector('#end-count').value)
    const res = document.querySelector('.res')

    // Validação
    if (isNaN(start) || isNaN(end)) {
        res.innerHTML = "Por favor, insira números válidos.";
        return;
    }
    if (start > end) {
        res.innerHTML = "O número inicial deve ser menor ou igual ao final.";
        return;
    }

    let count = []
    
    for(let c = start; c <= end ; c++){
        count.push(c)
    }
    
    res.innerHTML = count.join(" 👉 ")

    document.querySelector('#end-count').value = ''
    document.querySelector('#start-count').value = ''
}
