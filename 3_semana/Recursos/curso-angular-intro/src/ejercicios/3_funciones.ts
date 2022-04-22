//funciones

function sumar (a:number, b:number){
    return a + b;
}

//funcion flecha
const sumarFlecha = (a:number, b:number) : number => {
    return a + b;
}


const res =  sumar(10,20);

// numero requerido, numero opcional, numero por defecto ----EN LOS ARGUMENTOS
function multiplicar(numero:number, otroNumero?:number, base:number = 2):number {
    return numero * base;
    
}


// new void no return nada

interface PersonajeLOR{ //es como una clase tonta
    nombre:string;
    pv: number;
    mostrarHp: (a:number, b:string) => void; //funciones
}
function curar (personaje: PersonajeLOR, curar:number): void{
    personaje.pv += curar;

}

const nuevoPersonaje: PersonajeLOR = {
    nombre: 'Strider',
    pv: 23,
    mostrarHp(){
        console.log('Puntos de vida', this.pv)
    }
}
curar(nuevoPersonaje, 20);
