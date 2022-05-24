import re


def verificar_email(email):
    patron = r'^\S\w+\@\w+\.com'
    busqueda = re.search(patron, email)
    if busqueda:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


def verificar_emailes(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


verificar_email("45cvke3@hgfgmail.com")

verificar_emailes("     4_7!!!5cvke3@hgfgmail.com")


#P2


def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")


#p3

def verificar_cp(cp):
    patron = r'\w\w\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
