lista = [1, 2, 2, 3, 4, 5, 66, 6, 7]

lista.append(0)

# agregar una lista a una lista
lista.extend(lista)

# reverse invertir una lista
lista = lista[::-1]
print(lista)

# invertir lista
lista.reverse()
print(lista)

# insertar un elemento en una posicion especifica
lista.insert(0,10)
print(lista)

# remove elimina un elemento de la lista
lista.remove(0)
print(lista)

# quita el primer elemento que hay
lista.pop(1)
print(lista)

# cuenta la cantidad de veces que aparece un elemento en la lista
print(lista.count(3))