/*Dado un array de numeros devolver el valor mas bajo y el mas alto */

function altoBjo(arry_numero){
    let ordenar = arry_numero.sort((a,b) => a -b);

    return {
        "Alto":ordenar[ordenar.length -1],
        "Bajo": ordenar[0]
    }
}

console.log(altoBjo([1,3, 44, 2,5,0, 33,44,3333,88888,1]));