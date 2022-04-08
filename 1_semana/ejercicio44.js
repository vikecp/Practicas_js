/*Dado un array de strings devolver otros con los valores que esten formados por mas de dos palabras */

function dosPAlabras(elementos){
    let nuevos_elementos = [];

    for(palabra of elementos){
        if(palabra.split(' ').length > 2){
            nuevos_elementos.push(palabra)
        }
    }
    return nuevos_elementos;
}

console.log(dosPAlabras(["hola soy una","soy", "una", "persona es un", "hi"]))