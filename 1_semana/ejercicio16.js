function vocales(texto){
    let coincidencias = texto.match(/[aeiou]/gi)

    return coincidencias ? coincidencias.length : 0;

}

console.log("Num de vocales: ", vocales("virginia castañeda"))