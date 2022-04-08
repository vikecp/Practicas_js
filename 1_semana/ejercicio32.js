/* Dado un array de num devolver  el array con sus num al cuadrado*/

function alCuadrado(numeros){
    let numerosCuadrados = numeros
                            .filter(numero =>  typeof numero === 'number')
                            .map(numero => Math.pow(numero,2));
return numerosCuadrados;
}

console.log(alCuadrado([1,3,"cjhv", true, "hi"]));