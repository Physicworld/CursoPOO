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
            print("El valor debe ser positivo")

obj = MiClase(10)
print(obj.valor)  # 10
obj.valor = 20
print(obj.valor)  # 20
obj.valor = -5    # El valor debe ser positivo
