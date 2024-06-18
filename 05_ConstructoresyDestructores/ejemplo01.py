class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Objeto {self.nombre} creado")

    def __del__(self):
        print(f"Objeto {self.nombre} destruido")

obj = MiClase("A")
del obj
