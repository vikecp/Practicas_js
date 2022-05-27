#p1 contar el numero de argumentos que recibiria

def cantidad_atributos(**kwargs):
    contador = 0
    for n in kwargs:
        contador += 1
    return contador

#p2
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

#p3
def describir_persona(nombre ,**kwargs):
    print(f"Características de {nombre}:")
    texto = ''
    for clave,valor in kwargs.items():
        texto = f"{clave}: {valor}"
        print(texto)
    return texto





