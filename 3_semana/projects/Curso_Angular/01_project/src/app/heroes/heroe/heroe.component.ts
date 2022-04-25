import { Component } from '@angular/core';


@Component({
    selector: 'app-heroe',
    templateUrl: 'heroe.component.html'
})

export class  HeroeComponent {
    nombre: string = "Vike";
    edad: number = 23;

    obtenerNombre(): string {
        return `${this.nombre} - ${this.edad} años`;
       // return this.nombre + ' - ' + this.edad;
    }

    get nombreCapitalizado(){
        return this.nombre.toUpperCase();
    }

    cambiarNombre():void{
        this.nombre = 'Ana';
    }

    cambiarEdad(): void{
        this.edad = 25;
    }

    
}

//Cuando se crea un componente tiene  que estar importado en un modulo