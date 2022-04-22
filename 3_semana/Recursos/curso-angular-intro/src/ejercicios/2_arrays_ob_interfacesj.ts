//objeto
interface Personaje {
    nombre: string;
    hp: number;
    habilidades: string[];
    puebloNatal?: string;
}

const personaje: Personaje = {
    nombre: 'vike',
    hp: 100,
    habilidades: ['bash','counter','healing']
}


//si quiero agregar al objeto otro atributo
personaje.puebloNatal = 'Pueblo paleta';


