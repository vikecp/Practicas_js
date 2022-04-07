/**Dados dos arrays filtrar solo los datos que coincidann en cada uno y ponerlos en un nuevo array */

function elementosComunes(arr1, arr2){
    const filtrado = arr1.filter(elemento => {
        return arr2.includes(elemento);
    });
    return filtrado;
}

console.log(elementosComunes([1,2,3,4,8],[2,8,9,0,5]))
// puede serr array de nombres tambien