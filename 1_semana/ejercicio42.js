/*Dados dos num, sacar un num aleaotorrio entre ellos */

function aleaotorio(min, max){
    let res = "";
    return Math.round(Math.random() * (max - min) + min);
}
console.log(aleaotorio(1,10));