# p1
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota.respirar()


# p2
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(cls.vivo)


Jugador.revivir()



# p3
class Personaje1:
    def lanzar_flecha(self, cantidad_flechas):
        cantidad_flechas -= 1
        return print(cantidad_flechas)

p1 = Personaje1()
p1.lanzar_flecha(67)


# otro ejemplo
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        print(self.cantidad_flechas)

p2 = Personaje(23)
p2.lanzar_flecha()
