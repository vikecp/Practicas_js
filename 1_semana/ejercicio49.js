/*Dado un objeto  coprobar si exite una propiedad en concreto */
function exitePropiedad(objeto, propiedad){
    if(typeof objeto === 'object' && typeof propiedad == "string" && hasOwnProperty.call(objeto, propiedad)){
        return true;
    }
    return false;
}

let usuario = {
    nombre: "vike",
    apellido: "Cp"
}

console.log(exitePropiedad(usuario, "web"));