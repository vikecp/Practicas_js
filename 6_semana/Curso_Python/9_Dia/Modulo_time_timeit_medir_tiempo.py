# time = cuanto tiempo tarda en ejecutarse el codigo
import time
def prueba_for(num):
    lista = []
    for n in range(1, num +1):
        lista.append(n)
    return lista
# cuanto se tardo
inicio = time.time()
prueba_for(10)
fin = time.time()

def prueba_while(num):
    lista = []
    contador = 1
    while contador <= num:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_while(10)
fin = time.time()

# timeit  cuanto dura la ejecucion de un codigo repitiendolo muchas veces
import timeit

declaracion = """
prueba_for(10)
"""
mi_setup = """
def prueba_for(num):
    lista = []
    for n in range(1, num +1):
        lista.append(n)
    return lista
"""
duracion = timeit.timeit(declaracion, mi_setup, number=1000000)
print(duracion)