import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GifsService {
  private apiKey: string = 'I3SogrtWfKZK2xQS2GDuKZSBPIrrN2kw'

  private _historial: string[] = [];

  get historial(){
   
    return [...this._historial];
  }

  buscarGifs( query: string = ''){
    query = query.trim().toLowerCase();
    //que solo muestre los no repetidos en el histo
    //sino lo incluye se agrega
    if( !this._historial.includes( query )){ //si y solo si lo voy a insertar sino existe
      this._historial.unshift( query );

      //limitar la cantidad de inserciones al historial
    //cortar el historial
    this._historial =  this._historial.splice(0,10);
    }
    

    console.log(this._historial)
  }

}
