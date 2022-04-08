/**Dado un string devolver todos los substring */

function todoSubstring(palabra){
    let substrings = [];
    for(letra in palabra){
        let comienzo = parseInt(letra);

        for(let i = 0; i<= palabra.length - comienzo; i++){
            let final = parseInt(i) + parseInt(comienzo);
            substrings.push(palabra.substring(comienzo, final));
        }
    }
    return substrings.filter(elemento => elemento.length >= 1);
}

console.log(todoSubstring("hola"))