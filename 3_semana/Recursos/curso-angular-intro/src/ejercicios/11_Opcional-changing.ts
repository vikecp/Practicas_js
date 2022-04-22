//encadenamiento opcional

interface pasajero{
    nombre: string;
    hijos?: string[] // el ? que ese valor es opcional
}

const pasajero1: pasajero = {
    nombre: 'Fer'
}
const pas2: pasajero = {
    nombre: 'Mel',
    hijos: ['ana', 'Gab']
}

function imprimehijos(pasajero: pasajero) :void{
    const cuantosHijos = pasajero.hijos?.length || 0;
    console.log(cuantosHijos);
}

imprimehijos(pasajero1)
