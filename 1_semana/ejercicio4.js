/*Ejercicio pide una frase */


function reversa(texto){
    let cadena_invertida = ""; //guardar el texto invertido
    for(let letra of texto){ //obtine el valor de cada letra
        cadena_invertida = letra  + cadena_invertida;
    }
    return cadena_invertida;
}
console.log("Texto invertido", reversa("viike"));



/**Otra forma */
function r(t){
    let arr = t.split('');
    let nu = [];
    for(let i = arr.length; i>0; i--){
        nu.push(arr[i-1]);
    }
    let final = nu.toString();
    let textoLimpio = final.toLowerCase().replace(/[!¡.,-]/gi,'');
    return textoLimpio;
}
console.log( "Texto invertido 2da Forma: ", r("viike"));
