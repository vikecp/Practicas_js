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
//desestructuracion es 

console.log('El volumen actual es: ' , reproductor.volumen);
