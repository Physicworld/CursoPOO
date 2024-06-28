class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad  # atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser positiva")


# Uso
persona = Persona("Juan", 30)
print(persona.get_nombre())  # Juan
persona.set_edad(35)
print(persona.get_edad())  # 35
persona.set_edad(-5)  # La edad debe ser positiva