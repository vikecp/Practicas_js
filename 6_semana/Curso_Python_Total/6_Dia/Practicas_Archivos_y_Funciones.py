#p1
def abrir_leer(archivo):
    mi_archivo = open(archivo)
    return mi_archivo.read()

#p2
def sobrescribir(archivo):
    mi_archivo = open(archivo, 'w')
    cambiar = mi_archivo.write("contenido eliminado")
    return cambiar

#p3
def registro_error(archivo):
    mi_archivo = open(archivo, 'a')
    cambiar = mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()
    return cambiar
