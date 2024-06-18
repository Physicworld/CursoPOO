class Ave:
    def volar(self):
        pass

class Aguila(Ave):
    def volar(self):
        return "El águila vuela alto"

class Pinguino(Ave):
    def volar(self):
        return "El pingüino no puede volar"

# Uso
def hacer_volar(ave):
    print(ave.volar())

aguila = Aguila()
pinguino = Pinguino()

hacer_volar(aguila)    # El águila vuela alto
hacer_volar(pinguino)  # El pingüino no puede volar
