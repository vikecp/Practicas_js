/*Funcion para crear tablas de multiplicar */

function tablaMultiplicar(numero){
    let res = `# Tabla del ${numero}\n`;

    for(let i = 1; i<=10; i++){
        let multiplicacion = (i*numero);
        res = res + `${i} x ${numero} = ${multiplicacion}\n`;
    }
    return res;
}
console.log(tablaMultiplicar(5))