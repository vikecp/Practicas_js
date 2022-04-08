/** Dado un num mostrar un triangulo de filas*/

function triangulo(num){
    let mitad = Math.floor(num -1);
    let res = "";
    //bucle total de filas
    for(let fila = 0; fila<num; fila++){
        let nivel="";
        //bucle para pintar * y espacios

        for(let columna = 0; columna < (2*num - 1); columna++){
            //concatenar por cada iteracion de la columna un asterisco

            if(mitad - fila <= columna && mitad + fila >= columna){
                nivel += "*";
            }else{
                nivel += " ";
            }
            
        }
        res += nivel + "\n";
    }

    return res;
}

console.log(triangulo(10));