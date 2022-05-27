#p1
mi_archivo = open('mi_archivo.txt','w')
cambiar = mi_archivo.write("Nuevo texto")
mi_archivo.close()

mi_archivo = open('mi_archivo.txt','r')
print(mi_archivo.read())
mi_archivo.close()

#p2
mi_archivo = open('mi_archivo.txt','a')
cambiar = mi_archivo.write("Nuevo inicio de sesión")
mi_archivo.close()

mi_archivo = open('mi_archivo.txt','r')
print(mi_archivo.read())
mi_archivo.close()

#p3
mi_registro = open('registro.txt','a')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for elemento in registro_ultima_sesion:
    mi_registro.writelines(elemento + '\t')
mi_registro.close()

mi_registro = open('registro.txt','r')
print(mi_registro.read())
mi_registro.close()