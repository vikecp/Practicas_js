/* */

function eliminarduplicados(elementos){
    elementos = elementos.filter(elemento =>{
        return typeof elemento === 'number';
    });
    let set_sinDuplicados = new Set(elementos);

    return Array.from(set_sinDuplicados);
}

console.log(eliminarduplicados(["uno", "dos",1,1,2,2,3,4,"hola"]))