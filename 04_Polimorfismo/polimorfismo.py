class Ave:
    def volar(self):
        pass

class Aguila(Ave):
    def volar(self):
        return "El aguila vuela alto"

class Pinguino(Ave):
    def volar(self):
        return "El pinguino no puede volar"

aguila = Aguila()
pinguino = Pinguino()

aves = [aguila, pinguino]

def hacer_volar(ave):
    print(ave.volar())

for i in range(len(aves)):
    hacer_volar(aves[i])
