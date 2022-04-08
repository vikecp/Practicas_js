/*Dados dos numeros devolver sum, res, mult, div */


function calculadora(num1, num2){
    let res = `
    La suma es: ${num1 + num2}
    La resta es: ${num1 - num2}
    La multiplicacion es: ${num1 * num2}
    La division es: ${num1 / num2}
    `;
    return res;
}

console.log(calculadora(10,5));