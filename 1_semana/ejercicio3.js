/**Cuantas veces se repite una palabra en una frase */
function search(frase, busqueda){
    let textoLimpio = frase.toLowerCase().replace(/[!¡.,-]/gi,''); // se crea un replace que crea un exp, regular por nada Dos comas.

    let res = 0;
    if(textoLimpio.includes(busqueda)){ //si hay coincidencia
        
        let palabras = textoLimpio.split(" "); //split me lo lleva a un array y en cada espacio lo separa como un valor
        let mapa = { }
        for(let palabra of palabras){ //for of busca conseguir el valor de cada elemento del array mientras que for in muestran el indice y la propiedad
            if(mapa[palabra]){
                mapa[palabra]++;
            }else{
                mapa[palabra] = 1;
            }
        }

        /*for in ---> da el valor del indice 0,1,2,3
          for of ---> da el valor del elemento*/
        res = mapa[busqueda]
        console.log(`La palabra ${busqueda} se repite ${res} veces.`)
    }else{//sino encuentra nada
        res = 0
    }
    return res;
}
search("La niña esta en , feliz! en su casa.  niña en GRANDE", "niña"); 
