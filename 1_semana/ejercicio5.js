/* Ejercicio que pide ¿Cuanto es el x por ciento de x numero? */

function calcular(porcentaje, numero) {
    let res = (porcentaje * numero) / 100;
    console.log(`El ${porcentaje}% de ${numero} es: ${res}`);
    return res;
}
calcular(43, 897);

