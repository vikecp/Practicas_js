/**Dados dos numeros devolvver cuantos num son impar*/
function impar(num1, num2){
    let contador = 0;
    while(num1 < num2){
        if(num1%2 !== 0){
            contador ++;
        }
        num1++;
    }
    return contador;
}
console.log(impar(1, 100)+ " Son los numeros impares")