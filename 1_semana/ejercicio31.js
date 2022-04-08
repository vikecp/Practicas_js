/*Calcular el tipo de angulo que es */

function angulo(grados){
    let res = "";
    if(grados < 90){
        res = "Es un angulo agudo";
    }else if(grados === 90){
        res = "Angulo recto";
    }else if(grados > 90 && grados <180){
        res = "Es un angulo Obtuso";
    }else if(grados === 180){
        res = "Es un angulo llano";
    }else if(grados > 180 && grados < 360){
        res = "Angulo concavo"
    }else{
        res = "Angulo completo"
    }

    return res;
}

console.log(angulo(120));