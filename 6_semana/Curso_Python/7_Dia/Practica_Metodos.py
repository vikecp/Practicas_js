# p1
class Perro:

    def ladrar(self):
        print("Guau!")


perro1 = Perro()
perro1.ladrar()

#p2
class Mago:

    def lanzar_hechizo(self):
        print('¡Abracadabra!')


merlin = Mago()
merlin.lanzar_hechizo()

# p3
class Alarma():
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


parar = Alarma()
parar.postergar(12)