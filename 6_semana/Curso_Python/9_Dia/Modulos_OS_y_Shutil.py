# recorrer cada carpeta
from pathlib import Path
import os
ruta = Path('/Users/virginia/Documents/Practicas_Prof/6_semana/Curso_Python/9_Dia/Modulos_OS&Shutil')

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son: ')

    for sub in subcarpeta:
        print(f'\t{sub}')

    print("Los archivos son:")

    for arch in archivo:
        print(f'\t{arch}')
    print('\n')



