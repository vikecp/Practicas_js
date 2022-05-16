from random import choice


def lanzar_moneda():
    caras_moneda = ['Cara', 'Cruz']
    resultado = choice(caras_moneda)
    return resultado


print(lanzar_moneda())

lista_numeros = [1, 2, 3, 4, 5, 6, 7]


def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        lista.clear()
        texto = 'La lista se autodestruirá'
        print(texto)
    else:
        texto = 'La lista fue salvada'
        print(texto)
    return lista


res_moneda = lanzar_moneda()

p = probar_suerte(res_moneda, lista_numeros)
print(p)
