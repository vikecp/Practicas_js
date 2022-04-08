/*Calculara a cuantos dias, meses y años pertenece */

function calcuarDias(dias){
    let anios = Math.floor(dias/365);
    let dias_restantes = dias % 365;
    let meses = Math.floor(dias_restantes/30);
    dias_restantes = dias_restantes%30;

    return `Equivale a ${anios} años, ${meses} meses, ${dias} dias`;

}

console.log(calcuarDias(9200));