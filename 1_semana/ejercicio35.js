/* Dado un array crear otro con los elementos del primero y el ultimo*/

function primeroYultimo(elementos){
    let nuevoArray = [];
    nuevoArray.push(elementos[0], elementos[elementos.length -1]);

    return nuevoArray;
}
console.log(primeroYultimo([12, 3,33, 44, 456,12]));