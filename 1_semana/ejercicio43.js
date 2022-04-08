/**Dado un array sacar su media */

function media(num){
    let suma = num.reduce((valor_acumulado, num_actual) =>{
        return valor_acumulado + num_actual;
    })

    let media = (suma / num.length);
    return media;
}

console.log(`La media es: `, media([1,2,3,4,5,6]))