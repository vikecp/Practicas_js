/**Dado un num devolverr su factorial */

function factorial(num){
    let res = 1;
    for( let i= 1; i<= num; i++){
        res *= i;
    }
    return res;

}

console.log("El fatorial de 3 es", factorial(3))