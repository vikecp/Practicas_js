# juego palitos si escoges un numero y te toca el palito mas corto pierdes
from random import shuffle
palitos = ['-', '--','---','----']

# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# pedir intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

#comprobar intento
def checar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print('Esta vez te has salvado')
    print(f'Te ha tocado {lista[intento-1]}')

#mezclar funciones
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
checar_intento(palitos_mezclados,seleccion)