
/**Dado un numero devolver cuantos bucles tiene */
function bucles(numero){
    let array_num = numero.toString().split('');
    let bucles = 0;
    for(numero of array_num){
        numero = parseInt(numero);

        if(numero === 0 || numero === 6 || numero === 9){
            bucles++;
        }else if(numero === 8){
            bucles += 2;
        }
    }
    return bucles;
}

console.log(bucles(400));