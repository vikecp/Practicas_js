/**pide un num y muestra desde 0 - hasta el numero de 8 en 8 */

function hastaCero(numero){
    let inicio = `---Del numero ${numero} hasta el 0 ---\n`;
    while(numero > 0){
        inicio += `- No ${numero} \n`;
        numero -= 8;
    }
    inicio +="----Fin----";
    return inicio;
}
console.log(hastaCero(100));