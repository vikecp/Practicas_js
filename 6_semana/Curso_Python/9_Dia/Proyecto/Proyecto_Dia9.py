from pathlib import Path
import os
import math
import re
import time
import datetime

inicio = time.time()
ruta = Path('/Users/virginia/Documents/Practicas_Prof/6_semana/Curso_Python/9_Dia/Proyecto/Descomprimir/Mi_Directorio')

patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
num_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            resultado = buscar_numero(Path(carpeta, arch), patron)
            if resultado != '':
                num_encontrados.append(resultado.group())
                archivos_encontrados.append(arch.title())


def mostrar_todo():
    indice = 0
    print("-" * 50)
    print(f'Fecha de Busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('Archivo\t\t\tNro. Serie')
    print('-------\t\t\t----------')

    for a in archivos_encontrados:
        print(f'{a}\t{num_encontrados[indice]}')
        indice +=1
    print('\n')

    print(f'Numeros encontrados: {len(num_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print("-" * 50)


crear_listas()
mostrar_todo()

