mi_archivo = open('Prueba.txt')

print(mi_archivo.read())

mi_archivo.close()

# p1
mi_texto = open('texto.txt')
print(mi_texto.read())

#p2
mi_texto = open('texto.txt')
primera_linea = mi_texto.readline()
print(primera_linea)
mi_texto.close()

# p3
mi_texto = open('texto.txt')
linea = mi_texto.readlines()
print(linea[1])
mi_texto.close()