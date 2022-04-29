# Angular 
- framework de js
- crear apps para la web, son responsibe
- SPA

- Es muy amigable
- Modulos ordenados
- Consola todo atraves por comandos
- Seguridad
- Crear componentes
- se base en clases e interfaces
- Se basa en typescript

# intro angular
- Es un framework, es un marco de trabajo estandarizado, se siguen cierta estructura
- tienes todo para comenzar
- Es modular
- 
# Bloques de angular
- Componentes:
    - bloque de html(codigo) y typescript

- servicios: son lugares centralizados de informacion
    - no es necesario usar redux.
- directivas:
    - 3 tipos: Directivas de componentes, estructurales, de atributos.

- rutas: compontes basados en la url
- modulos: agrupar todo lo relacionado a cierta cosa., modulo de cliente, de servicios.

# Pasos para crear proyectos en Angular
**Comandos**
1. ng new nombre
2. ng serve -o: toma el codigo lo transpila a js monta un servidor mediante wepApp y lo abra tan pronto este disponible

## Crear componentes automaticos
- ng g c ruta
- ejemplo: ng g c layout/skeleton ---module ../app
- ng generate component  modules/user/user-list

# Modulos
- ng generate module core
--------Cuando tienes una carpeta -------------------
- ng generate module modules/user

# REactiveX con un modulo de node
npm i --save rxjs

# Para mandar a producion
ng build --prod

# crear servicios
- ng g s gifs/services/gifs --spik-test
