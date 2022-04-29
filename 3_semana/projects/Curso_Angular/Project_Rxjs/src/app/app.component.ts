import { Component } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app'
  //Intro Rxjs
  obs: any;

  ngOnInit() {
    this.obs = new Observable(subscriber => {
      subscriber.next(1);
      subscriber.next(2);
      subscriber.next(3);
      setTimeout(() => {
        subscriber.next(4);
        subscriber.complete();
      }, 1000);
    });
  }
  rxjsFun(){
    console.log('just before subscribe');
    this.obs.subscribe({
    next: (x: string) => console.log('got value ' + x) ,
    error: (err: string) => console.error('something wrong occurred: ' + err),
    complete() { console.log('done'); }
    });
    console.log('just after subscribe');
  }
  
}

