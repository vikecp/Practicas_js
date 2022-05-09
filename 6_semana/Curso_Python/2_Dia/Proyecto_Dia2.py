programa = r"""
App para calcular las comisiones de los empleados
"""
name = input("Ingresa tu nombre: ")
ventas = float(input("Ingresa tus ventas: "))

comisiones = (13 * ventas) / 100
redondeo = round(comisiones,2)
print(f'{programa} \nOk {name} este mes ganaste ${redondeo} pesos, felicidades')