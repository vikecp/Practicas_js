import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { SearchGifsResponse, Gif } from '../interface/gifs.interface';

@Injectable({
  providedIn: 'root'
})
export class GifsService {
  private apiKey: string = 'I3SogrtWfKZK2xQS2GDuKZSBPIrrN2kw';
  private servicioUrl: string = 'https://api.giphy.com/v1/gifs';
  private _historial: string[] = [];

  //mostrar gifs y que se guarde en el localstorage
  public resultados: Gif[] = []

  get historial(){
    return [...this._historial];
  }

  //api
  constructor( private http: HttpClient){
    //cargar del localstorage siempre se guarda para que si haces refreh siga aparenciendo
    this._historial =  JSON.parse(localStorage.getItem('historial')!) || [];
    this.resultados =  JSON.parse(localStorage.getItem('resultados')!) || [];
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

    //guardar en local storage, te crea un arreglo
    localStorage.setItem('historial', JSON.stringify( this._historial));

    }
    //http params
    const params = new HttpParams()
          .set('api_key', this.apiKey)
          .set('limit', '10')
          .set('q', query);

    this.http.get<SearchGifsResponse>(`${ this.servicioUrl }/search`, { params }) //mas funcionalidad con http que es igual a fetch
    .subscribe((resp) =>{
      this.resultados = resp.data;
      //grabar en el local storage
      localStorage.setItem('resultados', JSON.stringify( this.resultados));
    })
    

    console.log(this._historial)
  }

}
