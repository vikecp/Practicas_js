/*Invertir un numero  */
function invertir(numero){
    let con_num = parseInt(
        numero
        .toString()
        .split('')
        .reverse()
        .join(''));

    console.log(`El numero ${numero} invertido es ${con_num}`);
}
invertir(256);


