# p1
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass


num_1 = Alumno("Juana", 24)
print(num_1.nombre)


# p2
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass


class Gato(Mascota):
    pass


michi = Gato(3, "michigan", 4)
huski = Perro(1, "odi", 4)

print(huski.nombre)


class Carros:
    def __init__(self, color, modelo, anio):
        self.color = color
        self.modelo = modelo
        self.anio = anio


class Deportivo(Carros):
    pass


ferrari = Deportivo('rojo',"hgfd",2020)


#p3
class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass


class Automovil(Vehiculo):
    pass

fiesta = Automovil()


