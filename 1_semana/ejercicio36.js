/**Dado un texto cuantos consonates y vocales tienes */

function cuentaLetras(texto){
    let consonanes = 0;
    let vocales = 0;
    let textoLimpio = "";

    textoLimpio = texto.split('').filter(letra => /[áéíóú\w]/gi.test(letra) && isNaN(letra)).join('');

    for(let letra of textoLimpio){
        if(/[áéíóúaeiou]/gi.test(letra) ){
            vocales ++;
        }else{
            consonanes++;
        }
    }

    return [consonanes, vocales];


}

let letras = cuentaLetras("Letras como estas hoy !!!")

console.log("Consonates", letras[0]);
console.log("Vocales", letras[1]);