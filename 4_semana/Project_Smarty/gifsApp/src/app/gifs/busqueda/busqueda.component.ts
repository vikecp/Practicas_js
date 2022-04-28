import { Component, ElementRef, ViewChild } from '@angular/core';
import { GifsService } from '../services/gifs.service';

@Component({
  selector: 'app-busqueda',
  templateUrl: './busqueda.component.html',
  styles: [
  ]
})
export class BusquedaComponent  { 
  //Codigo para la caja de texto, cuando el usuario escriba y de enter se limpie la caja de texto
  @ViewChild('txtBuscar') txtBuscar!:ElementRef<HTMLInputElement>; //decorador de ts

  //para usar el servicio, se inyectara
  constructor( private gifsService: GifsService){}

  buscar(){
    const valor =  this.txtBuscar.nativeElement.value;
    //si presionas enter sin nada, no se aagrega al historial
    if( valor.trim().length === 0){
      return;
    }
    this.gifsService.buscarGifs( valor);

    this.txtBuscar.nativeElement.value = ''
  }


}
