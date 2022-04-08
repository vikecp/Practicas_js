/**Dado un array de alumnos cuantos estan reprobados y cuantos pasaron */

function reprobados(alumnos){
    let reprobados = 0, aprobados = 0;
    for(alumno of alumnos){
        if(alumno[1] >= 6){
            aprobados++;
        }else{
            reprobados++;
        }
    }

    return {
        "Aprobados": aprobados,
        "Reprobados": reprobados
    }
    
}

console.log(reprobados([
    ["Victor", 10],
    ["juan", 4],
    ["Salma", 7],
    ["vike", 8],
    ["omar", 10]
]))