#p1
def suma_cuadrados(*args):
    suma = 0
    for n in args:
        suma += n**2
    return suma

print(suma_cuadrados(2,3,5,-7))

#p2
def suma_absolutos(*args):
    suma = 0
    for n in args:
        abso = abs(n)
        suma += abso
    return suma

print(suma_absolutos(2,3,5,-7))

#p3
def numeros_persona(nombre, *args):
    suma_numeros = 0
    for n in args:
        suma_numeros += n
    return f'{nombre} la suma de tus números es {suma_numeros}'
print(numeros_persona("vike",2,3,5,-7))