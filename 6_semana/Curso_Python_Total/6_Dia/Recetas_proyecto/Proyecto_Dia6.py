# Recetario
import os
from pathlib import Path, PureWindowsPath
from os import system


# 2
def informar_ruta():
    ruta = Path(Path.home(), 'Documents', 'Practicas_Prof', '6_semana', 'Curso_Python', '6_Dia', 'Recetas_proyecto',
                'Recetas')
    ruta_windows = PureWindowsPath(ruta)
    return ruta_windows


# 3
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

# Llamar las funciones
mi_ruta = informar_ruta()
num_recetas = contar_recetas(mi_ruta)

# menu del sistema
def inicio():
    system('cls')
    print('*' * 40)
    print("Bienvenid@ a tu administrador de recetas")
    print('*' * 40)
    print('\n')
    print(f'La ruta del recetario es: {mi_ruta}\n\n')
    print(f'Total de recetas: {num_recetas}\n\n')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        menu_detalles = """
        Elige una opcion:
        [1] - Leer una receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa
        """
        print(menu_detalles)
        eleccion_menu = input()
    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) +1):
        eleccion_correcta =input("\nElije una categoria: ")
    return  lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in  ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador +=1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\n Elije una receta: ")
    return lista[int(eleccion_receta) -1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    exite = False

    while not exite:
        print("Escribe el nombre de tu receta:")
        nombre_receta = input() + '.txt'
        print("Escribe tu receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            exite = True
        else:
            print("esa receta ya existe")


def crear_categoria(ruta):
    exite = False

    while not exite:
        print("Escribe el nombre de tu categoria:")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu receta {nombre_categoria} ha sido creada")
            exite = True
        else:
            print("esa categoria ya existe")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminda")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'si':
        eleccion_regresar = input("\nEscriba si para volver al menu: ")


finalizar = False

while not finalizar:
    menu = inicio()
    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 6:
        finalizar = True


