/* Dado un num si es un num capicua o no */

function capi(num){
    let res = ""
    let procesado = parseInt(num
                    .toString()
                    .split('')
                    .reverse()
                    .join(''));

    if(num === procesado){
        res = "Es un numero capicua"
    }else{
        res = "No Es un numero capicua"
    }
    return res;

}

console.log(capi(3001));
