/* hacer un reloj que en tiempo real vaya mostrando el dibujo */
function relojRapido(){
    setInterval(()=>{
    const fecha  =  new Date();
    const horas =  fecha.getHours();
    const minutos = fecha.getMinutes();
    const segundos = fecha.getSeconds();
    console.log(`${horas}: ${minutos}: ${segundos}`);
    }, 1000)
}

relojRapido();