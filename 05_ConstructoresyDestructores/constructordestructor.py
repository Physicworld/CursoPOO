class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Objeto {self.nombre} creado")

    def __del__(self):
        print(f"Objeto {self.nombre} destruido")

def mi_funcion():
    obj_f = MiClase("F")
    del obj_f

obj_a = MiClase("A")
del obj_a
mi_funcion()
obj_b = MiClase("B")
obj_c = MiClase("C")

del obj_b
del obj_c

