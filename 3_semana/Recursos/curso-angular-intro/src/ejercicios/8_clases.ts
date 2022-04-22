//clases
class PersonaNormal{
    constructor(
        public nombre:string,
        public direccion: string
    ){}
}

class Heroe extends PersonaNormal{
     /*alterEgo: string;
     edad: number;
     NombreReal: string;*/
     //constructor: una funcion que se va a llamar cuando creo una intancia de mi clase

     //Otra forma de usar el constructor
     //estoy asignada a la clase cada una de sus propiedades en base en sus arrguemntos 

     //SUPER: llamar el constructor de la clase a la cual extiende
     constructor (
         public alterEgo:string,
         public edad: number,
         public NombreReal: string){
             super(NombreReal, 'New York'); //extends
         }

     // Las variables se definen afuera del contructor
     //constructor (alterEgo:string, nombre:string){
       //  this.alterEgo = alterEgo;
     //}
}

const iroman = new Heroe('Iron',45, 'tony');// el new herore()los parentesis hacen referencia al constructor
console.log(iroman)

//clases sirven para crear instancias hay funciones de como funciona el codigo

//interfaces no se pueden definir como funciona un metodo o si quiero tener get and set


//niveles de acceso


