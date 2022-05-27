#p1
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa("blanco", 4)

# p2
class Cubo:
    caras = 6
    def __init__(self,color):
        self.color = color
cubo_rojo = Cubo("rojo")

#p3
class Personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
harry_potter = Personaje("Humano",True,17)

