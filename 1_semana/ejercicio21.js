function recortar(texto, hasta){
    resultado = "";

    if(typeof texto === "string" && typeof hasta === 'number'){
        resultado =  texto.substring(0, hasta);
    }else{
        resultado = "introduce bien los datos"
    }

    return resultado;
}

console.log(recortar("hola como estas soy viike", 10));