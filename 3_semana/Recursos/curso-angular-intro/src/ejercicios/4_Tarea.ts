interface SuperHeroe {
    nombre:string;
    edad: number;
    direccion: Direccion;//objeto anidado
    mostrarDireccion: () => string;
} //cuando el tipo de dato es otro objeto, se crea mejor una nueva interface

interface Direccion{
    calle: string;
    pais: string;
    ciudad: string;
}

const superHeroe: SuperHeroe = {
    nombre: 'Spiderman',
    edad:30,
    direccion:{
        calle:'Maian St',
        pais: 'USA',
        ciudad: 'NY'
    },
    mostrarDireccion(){
        return this.nombre + ', ' + this.direccion.ciudad + ', '+ this.direccion.pais;
    }
}

const direccion = superHeroe.mostrarDireccion();
console.log(direccion);

