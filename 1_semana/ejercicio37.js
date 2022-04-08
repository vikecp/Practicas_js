/*De acuaerdo con un texto o un array indicar cual es la palabra o cosa que mas aparece */
function elmasAparece(datos){
    let mapeo = {};
    let masFrecuente = "", valor_mas_frecuente = 0;
    if(typeof datos === 'string'){
        datos = datos.split(' ');
    }
    for(elemento of datos){ // si existe el elemento
        if(mapeo[elemento]){
            mapeo[elemento]++;
        }else{
            mapeo[elemento] = 1; // sino existe
        }
    }

    for(let elemento in mapeo){
        if(mapeo[elemento] > valor_mas_frecuente){
            valor_mas_frecuente = mapeo[elemento];
            masFrecuente = elemento;
        }
    }

    return {
        "Mas_frecuente": masFrecuente,
        "Mayor_Valor": valor_mas_frecuente
    };
}
console.log(elmasAparece("Viike como estas viike creo que prog vike"));
console.log(elmasAparece([1,2,3,4,4,4,4,3,1]));
