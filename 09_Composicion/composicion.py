class Motor:
    def __init__(self):
        self.temperatura = 0
        self.combustible = 100

    def encender(self):
        print("Motor Encendido!")
        self.temperatura += 50

    def apagar(self):
        self.temperatura = 0

    def acelerar(self):
        if self.combustible > 0:
            self.temperatura += 1
            self.combustible -= 1
            print(f"Acelerando. Temperatura {self.temperatura}, Combustible: {self.combustible}%")
        else:
            print("Sin combustible. No se puede acelerar.")


class SistemaElectrico:
    def __init__(self):
        self.bateria = 100

    def encender_luces(self):
        if self.bateria >= 5:
            print("Luces Encendidas")
            self.bateria -= 5
        else:
            print("No hay bateria suficiente para encender luces")

    def tocar_bocina(self):
        if self.bateria >= 1:
            print("Beep! Beep!")
            self.bateria -= 1
        else:
            print("No hay bateria suficiente para tocar bocina")

class Coche:
    def __init__(self):
        self.motor = Motor()
        self.sistema_electrico = SistemaElectrico()
        self.velocidad = 0

    def arrancar(self):
        self.motor.encender()
        print("Coche arrancado")

    def detener(self):
        self.motor.apagar()
        self.velocidad = 0
        print("Coche detenido")

    def acelerar(self):
        self.motor.acelerar()
        self.velocidad += 10
        print(f"Velocidad Actual: {self.velocidad} km/h")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10
            print(f"Frenando. Velocidad actual: {self.velocidad}")
        else:
            print("El coche ya esta detenido")

    def enceder_luces(self):
        self.sistema_electrico.encender_luces()

    def tocar_bocina(self):
        self.sistema_electrico.tocar_bocina()

coche = Coche()
coche.arrancar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.enceder_luces()
coche.tocar_bocina()
coche.frenar()
coche.frenar()
coche.detener()