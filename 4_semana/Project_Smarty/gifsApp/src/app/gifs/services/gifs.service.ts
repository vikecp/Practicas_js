import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GifsService {
  private apiKey: string = 'I3SogrtWfKZK2xQS2GDuKZSBPIrrN2kw'
  private _historial: string[] = [];

  //mostrar gifs
  public resultados:any[] = []

  get historial(){
    return [...this._historial];
  }

  //api
  constructor( private http: HttpClient){

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

    this.http.get(`https://api.giphy.com/v1/gifs/search?api_key=I3SogrtWfKZK2xQS2GDuKZSBPIrrN2kw&q=${ query }&limit=10`) //mas funcionalidad con http que es igual a fetch
    .subscribe((resp: any) =>{
      console.log(resp);
      this.resultados = resp.data;
    })
    

    console.log(this._historial)
  }

}
