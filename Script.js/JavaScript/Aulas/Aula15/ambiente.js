let num =[5,8,4]
num.sort()

console.log(`Nosso vetor é o ${num}`)
console.log('-=-'.repeat(10))

num.push(6)

console.log(num)
console.log('-=-'.repeat(10))

let lenght = num.length

console.log(lenght)
console.log('-=-'.repeat(10))

/*for(c = 0  ; c < num.length ; c++){
    console.log(num[c])
    }
    console.log('-=-'.repeat(10))*/
    
    for(let pos in num){
        console.log(num[pos])
    }
    console.log('-=-'.repeat(10))

console.log(num.indexOf(8))