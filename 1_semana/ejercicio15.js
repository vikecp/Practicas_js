/**dado una cadena de texto devolver la letra que mas se repite */

function masUsado(frase){
    let mapeo_letras = {};
    let max_rep = 0;
    let letra_mas_repe = 0;

    for(let letra of frase){
        if(!mapeo_letras[letra]){
            mapeo_letras[letra] = 1;
        }else{
            mapeo_letras[letra]++;
        }
    }

    for(let letra in mapeo_letras){
        if(mapeo_letras[letra].toString().trim().length === 1 && mapeo_letras[letra] > max_rep){
            max_rep = mapeo_letras[letra];
            letra_mas_repe =  letra;
        }
    }
   
    return letra_mas_repe;
}


console.log("la letra mas repetida es ", masUsado( "aaaaaaaaaa"));

