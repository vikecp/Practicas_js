//Decoradores: sirven para cambiar las clases cuando son definidas
function reportableClassDecorator<T extends { new (...args: any[]): {} }>(constructor: T) {
    return class extends constructor {
      reportingURL = "http://www...";
    };
  }
@reportableClassDecorator
class MiClase{
    public miPropiedad: string = 'ABD33';
    imprimir(){
        console.log("Hi");
    }
}



