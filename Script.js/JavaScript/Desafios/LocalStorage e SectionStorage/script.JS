// 1 - inserir dado
localStorage.setItem('name', 'Matheus')

//2 - resgatar item
const name = localStorage.getItem('name')

console.log(name)

// 4 - resgatando item que não existe
const lastName = localStorage.getItem('lastname')

console.log(lastName)
if (!lastName){
    console.log("Sem sobrenome!")
}

//5 - remover item
localStorage.removeItem("name")

//6 - limpar todos os itens
localStorage.setItem("a", 1)
localStorage.setItem("b", 2)

console.log(typeof Number(localStorage.getItem("a")))

localStorage.clear()