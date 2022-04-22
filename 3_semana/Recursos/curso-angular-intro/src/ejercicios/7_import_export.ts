//importaciones y exportaciones

import { calculaISV, Producto } from "./6_Desesctru_funciones";


const carritoCompras: Producto[] = [
    {
        desc: 'Tel 1',
        precio: 150
    },
    {
        desc: 'Tel 2',
        precio: 350
    },
];

const [total, isv] = calculaISV(carritoCompras);
console.log('Total', total);
console.log('ISV', isv);


