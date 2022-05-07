from pyparsing import col


[1, "hi", 1.22, True,[1,2,3,4]]

colors = ['red', 'green', 'pink']
# constructor
number_list = list((1,2,3,4))
print(number_list)

# Crear una lista apartir de un rango

#r = list(range(1,10))
#print(r)

# Saber si un elemento existe en una lista
print('green' in colors) # res: true

# Cambiar los datos de una lista
colors[1] = "yellow"
print(colors)

# Agrega un elemento al final
colors.append('violet');

# agregar varios elementos 
colors.extend(['orange', 'blue', 'gray'])

# agregar en cierta posicion
colors.insert(1, "violet")

# remover el ultimo elemento
colors.pop()

# eliminar un especificp
colors.remove('green')

# quitar todo
colors.clear()

# ordenar alfabe
colors.sort()

# ordenar de manera inversa
colors.sort(reverse=True)

#Saber los indices
colors.index("red")

# contar cuantas veces existe
colors.count("red")
