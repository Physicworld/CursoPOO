class MiClase:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor > 0:
            self._valor = nuevo_valor
        else:
            print("El nuevo valor debe ser positivo")

obj = MiClase(10)
print(obj.valor)

obj.valor = 20
print(obj.valor)

obj.valor = -5