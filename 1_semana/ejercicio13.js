/*Dado un array dividirlos en tantos subarrays dados */
function divicion(array_principal, numero){
    let arreglos = [];
    for(let elemento of array_principal){
        
        let ultimo = arreglos[arreglos.length -1];

        if(!ultimo || ultimo.length === numero){
            arreglos.push([elemento])
        }else{
            ultimo.push(elemento);
        }
    }
    return arreglos;
}
console.log(divicion([1,2,3,4,5,5],4));
