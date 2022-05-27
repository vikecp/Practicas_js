# p1
lista_numeros = [2,3,5,-2]

def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True

r = todos_positivos(lista_numeros)
print(r)

#p2
lista_numeross = [1,2,3,100,23]
def suma_menores(lista_numeross, suma=0):
    for n in lista_numeross:
        if n in range(0,1000):
            suma = suma + n
        else:
            pass
    return suma

s = suma_menores(lista_numeross)
print(s)


#p3
lista_num = [1,2,3,4,5,6]
def cantidad_pares(lista_num,count_pares=0):
    for numero in lista_num:
        if numero%2 == 0:
            count_pares += 1
        else:
            pass
    return count_pares

pares = cantidad_pares(lista_num)
print(pares)




