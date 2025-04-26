function piramide(altura){
    for (c = 1; c <= altura; c++){
        let spaces = ' '.repeat(altura - c)
        let mimdaumreal = '*'.repeat(2*c-1)

        console.log(spaces + mimdaumreal + spaces +spaces+ mimdaumreal)
    }
}
piramide(5)