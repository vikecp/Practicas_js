/*Dado un array de objetos de pelicula(titulo, director, vista)
mostrar todas las peliculas indicando cual has visto y cual no
*/

const coleccion_peliculas = [
    {
        titulo: "La cenicienta",
        director: "Idk",
        vista: false
    },
    {
        titulo: "Los vengadores",
        director: "Joe Russo",
        vista: false
    },
    {
        titulo: "batman vs Superman",
        director: "Zack snyder",
        vista: true
    },
    {
        titulo: "Siempre a tu lado",
        director: "idk",
        vista: true
    }

];


function mispeliculas(peliculas){
    for(pelicula of peliculas){
        let paramostrar = `"${pelicula.titulo} de ${pelicula.director}"`;

        if(pelicula.vista){
            console.log(`Ya has visto: ${paramostrar}`);
        }else{
            console.log(`No has visto: ${paramostrar}`);
        }
    }
    return peliculas;
}

mispeliculas(coleccion_peliculas);