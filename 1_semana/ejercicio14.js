/**pide una frase y da un numero y lo repite el num de veces indicado */


// solo funciona en js 
function repite(texto, numero){
    let resultado = "";
    for(let i=0; i<numero; i++){
        resultado += texto;
    }
    return resultado
}
console.log(repite("viike", 8));


///funcion prototipo

String.prototype.repite = function(numero){
    let resultado = "";
    for(let i=0; i<numero; i++){
        resultado += this;
    }
    return resultado
}

console.log("virginia cjhdhv hfvu".repite(4));
