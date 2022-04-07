/*Ejercicio dibujar un cuadrado hueco con asteriscos */
function lado(numero){
    let lado = "";
    for(let i = 0; i<numero; i++){
        lado += "*";
    }
    return lado;
    
}
function cuadrado(numero){
    let dibujo = lado(numero) + "\n";
    let contenido = "*";
    for(let i = 2; i<numero; i++){
        contenido = "*";
        for(let x = 2; x<numero; x++){
            contenido+= " ";
        }
        contenido += "*"
        dibujo += contenido +"\n";
    }

    dibujo += lado(numero);
    return dibujo;
    
}
console.log(cuadrado(4))

/*Funcio que hace un cuadrado
function lado(numero){
    let lado = "";
    for(let i = 0; i<numero; i++){
        lado += "*";
    }
    return lado;
    
}
function cuadrado(numero){
    let dibujo = lado(numero) + "\n";
    let contenido = "";
    for(let i = 2; i<numero; i++){
        contenido = "";
        for(let x=0; x<numero; x++){
            contenido+= "*";
        }
        dibujo += contenido +"\n";
    }

    dibujo += lado(numero);
    return dibujo;
    
}
console.log(cuadrado(4))


*/



