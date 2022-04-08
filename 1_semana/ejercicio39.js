/*dado un texto que sea un email valido */
let res = "";
function comprobarEmail(email){
    let testear_email = /^\w+@\w+\.\w+$/gi .test(email);
    if(testear_email){
        res = `${email} Es un email valido`;
    }else{
        res = `${email} No es un email valido`;
    }
    return res;
}

console.log(comprobarEmail("vike@gmail.com"));
console.log(comprobarEmail("fufi@jjfh"))