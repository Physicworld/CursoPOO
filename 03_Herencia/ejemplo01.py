class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        return "Guau"


class Gato(Animal):
    def sonido(self):
        return "Miau"


# Uso
perro = Perro("Rex")
gato = Gato("Michi")
print(perro.nombre, "dice", perro.sonido())  # Rex dice Guau
print(gato.nombre, "dice", gato.sonido())  # Michi dice Miau
