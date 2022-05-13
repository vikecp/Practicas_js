#p1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
nombres_tuples = list(enumerate(lista_nombres))

for indice,nombre in nombres_tuples:
    print(f'{nombre} se encuentra en el índice {indice}')

#p2
palabra = "Python"
lista_indices = list(enumerate(palabra))
print(lista_indices)
print(lista_indices[2][1])

#p3 imprime los indices de los nombres que inicien con la letra M
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
nombres_indices = list(enumerate(lista_nombres)) #crea un tuple

for indice,nombre in nombres_indices:
    if nombre.startswith("M"):
        print(indice)

