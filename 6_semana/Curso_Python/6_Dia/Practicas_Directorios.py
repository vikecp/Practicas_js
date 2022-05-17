import os

#obtines la ruta
ruta = os.getcwd()
print(ruta)

#Cambiar de directorio
ruta = os.chdir('C:\\Users\\virginia\\Documents\\Practicas_Prof\\6_semana\\Curso_Python\\6_Dia')

arc = open('Prueba.txt')

print(arc.read())

otro_archivo = open('C:\\Users\\virginia\\Documents\\Practicas_Prof\\6_semana\\Curso_Python\\6_Dia\\Prueba.txt')
print(otro_archivo.read())

# Abrir el archivo desde cualquier sistema operativo
from pathlib import Path
carpeta = Path('/Users/virginia/Documents/Practicas_Prof/6_semana/Curso_Python/6_Dia') / 'Prueba.txt'
mi_archivo = open(carpeta)
print(mi_archivo.read())






