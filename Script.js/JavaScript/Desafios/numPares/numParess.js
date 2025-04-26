function numPares(start , end){
    let range = []

    for( c = start; c <= end; c++){
        range.push(c)
    }
    let pairs = []

    for (let c of range) {
        if (c % 2 == 0) {
            pairs.push(c);
        }
    }

    return pairs
}

console.log(numPares(1,10))