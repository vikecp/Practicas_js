/*Dado un array de numeros devolver pares e impares en array dferente */

function pares(numeros){
    return{
        pares: numeros.filter(num => num  % 2 == 0),
        impares: numeros.filter(num => num % 2 !== 0)
    }
}

console.log(pares([1,2,4,50,22,333,345,12,888,7]));