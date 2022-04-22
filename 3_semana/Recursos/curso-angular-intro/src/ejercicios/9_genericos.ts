//genericos
function queTiposoy<T>(argu: T){ //generico entra cualquier tipoo de dato
    return argu;
}

let st = queTiposoy('Vike');
let num = queTiposoy(2);
let arr = queTiposoy([1,2,3,3])
