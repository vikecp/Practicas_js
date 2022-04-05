function palindromo(text){
    let invertido = text.split('').reverse().join('');

    if(text === invertido){
        console.log(`La palabra ${text} es un Palindromo`);
    }
    else{
        console.log("No es un palindromo!")
    }
}
palindromo("ana")