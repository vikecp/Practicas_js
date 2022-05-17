from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/virginia/Documents/Practicas_Prof/6_semana/Curso_Python/6_Dia') / 'Prueba.txt'

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)


print(carpeta.read_text()) #no se tiene que abrir ni cerrar nuestro archivo

print(carpeta.name) # devuelve el nombre del archvio

print(carpeta.suffix)

print(carpeta.stem)

if not carpeta.exists():
    print("No existe")
else:
    print("Si exixte")
