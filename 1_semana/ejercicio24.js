/*ver si un array es una permutacion */

function permutacion(secuencia, num){
    for(let i = 0; i<num; i++){
        if(secuencia.indexOf(i + 1) < 0){
            return "no es una permtacion";
        }
    }
    return "Es una permutacion"
}

console.log(permutacion([1,2,4,5], 5))