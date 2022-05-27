# p1
num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
     print(f"{num2} es mayor que {num1}")
elif num1 == num2:
    print(f"{num1} y {num2} son iguales")


#p2
edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad>=18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

#p3
habla_ingles = True
sabe_python = False
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python")