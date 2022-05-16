# juego tipo juego ahorcado con algunas modificaciones
from random import choice
app = f"""
Hola soy Woopa he elegido una palabra secreta y quiero que la adivines!
Recuerda que solo tienes 6 intentos.
A continuacion te muestro tu palabra: 
"""
print(app)

lista_palabras = ['oso', 'bicicleta', 'torta', 'computadora', 'agua']
lista_incorrectas = []
lista_correcta = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabras):
    palabra_secreta = choice(lista_palabras)
    letras_unicas = len(set(palabra_secreta))

    return palabra_secreta,letras_unicas

#pedir letra
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida



def imprimir_guiones(palabra):
    guiones = 0
    for letra in palabra:
        guiones += 1
    return guiones*'_'

