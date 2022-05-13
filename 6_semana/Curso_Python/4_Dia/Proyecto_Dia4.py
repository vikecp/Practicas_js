from random import randint
app = """
------Juego para adivinar el número secreto!------
"""
nombre = input("Hola, ¿Cómo te llamas?: ")

# crear numero random
num_secreto = randint(1,100)

# inicio
inicio = f"""{app}
Hola {nombre}, Soy Woopa!!! Y he pensado un número secreto
entre el 1 al 100 y tienes 8 intentos para adivinar cual es!!! 
¿Te animas?
el numero secreot es {num_secreto}
"""
print(inicio)
numero_ingresar = int(input("Escribe el numero que crees que es el secreto: "))

#loop para intentos
intentos = 8

# validaciones
if numero_ingresar < 1 or numero_ingresar > 101:
    res = f"El numero {numero_ingresar} que ingresaste no es valido, recurda que solo puedes ingresar numeros del 1 al 100"
    print(res)
elif 0 < numero_ingresar <= 100:
    while intentos > 1:
        if numero_ingresar < num_secreto:
            res2 = "El numero es incorrecto, y es MENOR al numero secreto"
            print(res2)
            numero_ingresar = int(input("Escribe el numero que crees que es el secreto: "))
        elif numero_ingresar > num_secreto:
            res3 = "El numero es incorrecto, y es MAYOR al numero secreto"
            print(res3)
            numero_ingresar = int(input("Escribe el numero que crees que es el secreto: "))
        else:
            res4 = f"Felicidades el numero {numero_ingresar} es el numero que era secreto"
            num_intentos = 8 - intentos
            print(res4)
            print(f"Adivinar sólo te costo {num_intentos} intentos, Eres muy buen adivinador")
            break
        intentos = intentos - 1
    if intentos == 1:
        print("Te acabaste tus intentos")












