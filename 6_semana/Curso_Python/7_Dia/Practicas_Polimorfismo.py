#p1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
lista = [palabra, lista, tupla]

#objetos distintos con pero se llama al mismo metodo y cada uno con resultados distintos
for elemento in lista:
    print(len(elemento))


#p2
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

arquero = Arquero()
mago = Mago()
samurai = Samurai()

personajes = [arquero, mago, samurai]
for carta in personajes:
    carta.atacar()


#p3
class Mago():
    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")


# instancias
merlin = Mago()
arq = Arquero()
sam = Samurai()


def personaje_defender(personaje):
    personaje.defender()


personaje_defender(merlin)