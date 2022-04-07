function censurado(texto=false, busqueda=false){
    let resultado = "";
    if(!texto && !busqueda){
        resultado ="no se puede leer el texto ni la busqueda";
    }else if (!texto && busqueda){
        resultado="no puedes leer el texto";
    }else if(texto && !busqueda){
        resultado = "no puedes hacer la busqueda";
    }else if(texto && busqueda){
        resultado = texto.replace(new RegExp(busqueda, 'gi'), "[Censurado]")
    }
    return resultado;

}

console.log(censurado("hola como estas hola hola hi", "hola"))