/* Dado un array de objetos devolver cuales son las aficicones 
mas comunes de los usuarios */

const usuarios = [
    {nombre: "victor", aficiones : ["informatica", "juegos", "cine"]},
    {nombre: "vike", aficiones : ["informatica", "juegos", "cine"]},
    {nombre: "Paco", aficiones : ["tenis", "juegos", "cine"]},
    {nombre: "pepe", aficiones : ["futbol", "teatro", "cine"]}
    ]
function aficiones(arrOj){
    let mapeo = {};

    for(objeto of arrOj){

        for(aficion of objeto.aficiones){
            if(!mapeo[aficion]){
                mapeo[aficion] = 1;
            }else{
                mapeo[aficion]++;
            }
        }
    }
    return mapeo;

}

console.log(aficiones(usuarios));