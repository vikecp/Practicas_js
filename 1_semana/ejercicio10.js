/*hacer una escalera */

function escalera(numero){
    let escaleracompleta = "";
    for(let nivel = 1; nivel<=numero; nivel++){
        let escalones = "";

        for(let escalon=1; escalon <= nivel; escalon ++){
            escalones += "[-]";
        }

        escaleracompleta += escalones + '\n';
    }
    return escaleracompleta;
}

console.log(escalera(6))