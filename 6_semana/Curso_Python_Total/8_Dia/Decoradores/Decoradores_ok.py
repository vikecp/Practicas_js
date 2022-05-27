def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra_funcion


# Pasen funciones a decoradas

#@decorar_saludo # si pongo este no puedo llamar solo a mayus, siempre pasara la funcion decorada
def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayuscula) # con esto puedo llamar a los dos metodos
mayuscula_decorada("vike")

minuscula("vikEEEEE")
