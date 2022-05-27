
lista_numeros = [1,2,34,45,56,2,34,56]
def reducir_lista(lista):
    elimina_duplicados = set(lista) # es un set
    lista_sin_duplicados = list(elimina_duplicados)
    mas_alto = max(lista_sin_duplicados)
    lista_sin_duplicados.remove(mas_alto)
    return lista_sin_duplicados
#promedio
def promedio(lista,suma = 0):
    for numero in lista:
        suma = suma + numero
    return suma/len(lista)

lista_promedio = reducir_lista(lista_numeros)
promedio(lista_promedio)
print(promedio(lista_promedio))

