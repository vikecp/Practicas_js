/**Dado un numero mostrar sus divisores */

function divisor(numero, divisor){
    if(numero % divisor === 0){
        return divisor;
    }else{
        return 0;
    }
}

function mostrar(numero){
    for(let i = 1; i<= numero; i++){
        let esDivisor = divisor(numero, i);
        if(esDivisor ) console.log(esDivisor);
    }
}
mostrar(20);