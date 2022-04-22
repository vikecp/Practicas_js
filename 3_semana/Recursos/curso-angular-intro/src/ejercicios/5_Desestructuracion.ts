//Destructuracion de objetos
interface Reproductor {
    volumen:number;
    segundo: number;
    cancion: string;
    detalles: Detalles
}

interface Detalles{
    autor: string;
    anio: number;
}

const reproductor: Reproductor = {
    volumen: 90,
    segundo: 36,
    cancion: 'mess',
    detalles: {
        autor: 'Ed sheeran',
        anio: 2015
    }
}
//desestructuracion de objetos es estraer ciertas propiedades de un objeto y crear variables
const {volumen, segundo, cancion, detalles} = reproductor;
const {autor} = detalles;
/* 
console.log('El volumen actual es: ' ,volumen);
console.log('El Segundo actual es: ' ,segundo);
console.log('La cancion actual es: ' ,cancion);
console.log('El autor actual es: ' ,autor);
**/

// desec de arreglos
const brawl: string [] = ['nita', 'shelly', 'piper', 'leon','belle'];

//desestructuracion
const [ , , p3] = brawl;
console.log('Brawl 1:', p3);