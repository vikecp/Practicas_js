/**Dado un  string dependiendo cual tenga mas mayus o minus, ponerlo en todo. */

function mayusMinus(texto){
    let mayus = 0;
    let minus = 0;
    let res = ""
    for(letra of texto){
        if(/[A-Z]/.test(letra)){
            mayus++;
        }else{
            minus++;
        }
    }

    if(mayus > minus){
        res = texto.toUpperCase();
    }else{
        res = texto.toLowerCase();
    }
    return res;
}

console.log(mayusMinus("Hola como estas HOY"))