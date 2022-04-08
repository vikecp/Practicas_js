/**Dados dos numeros cual es mayor y cual es menor */

function mayorMenor(num1, num2){
    let res = ""
    if(num1 === num2){
        res = "Los numeros son iguales";
    }else if(num1 > num2){
        console.log(`El numero mayor es ${num1}`);
        console.log(`El numero menor es ${num2}`);
    }else{
        console.log(`El numero mayor es ${num2}`);
        console.log(`El numero menor es ${num1}`);
    }
    return res;
}
console.log(mayorMenor(3,2))