/*Dada dos cadenas ver si son anagramas entre si */

function limpiarTexto(frase1){
    let frase_clean =  frase1.replace(/[^\w]/gi,'').toLowerCase().split('').sort().join(''); //elimina todo lo que no sea una letra
}


function anagramas(texto1, texto2){
    
    return limpiarTexto(texto1) === limpiarTexto(texto2);
}

console.log(anagramas("SerGIO . { !", "Riesgo%7."));