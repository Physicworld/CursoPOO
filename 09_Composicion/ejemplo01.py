class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()
        print("Coche arrancado")

coche = Coche()
coche.arrancar()
