# Juego de dados
from random import randint


def lanzar_dados():
    lado1 = randint(1, 6)
    lado2 = randint(1, 6)
    return lado1, lado2
print(lanzar_dados())


def evaluar_jugada(num1, num2):
    suma_dados = num1 + num2
    texto = ''
    if suma_dados <= 6:
        texto = f'La suma de tus dados es {suma_dados}. Lamentable'
    elif 6 < suma_dados < 10:
        texto = f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    elif suma_dados >= 10:
        texto = f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'
    return texto


lanza1, lanza2 = lanzar_dados()

p = evaluar_jugada(lanza1, lanza2)
print(p)
