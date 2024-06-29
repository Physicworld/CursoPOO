class Motor:
    def __init__(self):
        self.temperatura = 0
        self.combustible = 100

    def encender(self):
        print("Motor encendido")
        self.temperatura += 50

    def apagar(self):
        print("Motor apagado")
        self.temperatura = 0

    def acelerar(self):
        if self.combustible > 0:
            self.temperatura += 10
            self.combustible -= 1
            print("Acelerando. Temperatura:", self.temperatura, "Combustible:", self.combustible)
        else:
            print("Sin combustible. No se puede acelerar.")

class SistemaElectrico:
    def __init__(self):
        self.bateria = 100

    def encender_luces(self):
        if self.bateria > 0:
            print("Luces encendidas")
            self.bateria -= 5
        else:
            print("Batería agotada. No se pueden encender las luces.")

    def tocar_bocina(self):
        if self.bateria > 0:
            print("¡Beep! ¡Beep!")
            self.bateria -= 1
        else:
            print("Batería agotada. No se puede tocar la bocina.")

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
        print("Velocidad actual:", self.velocidad, "km/h")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10
            print("Frenando. Velocidad actual:", self.velocidad, "km/h")
        else:
            print("El coche ya está detenido")

    def encender_luces(self):
        self.sistema_electrico.encender_luces()

    def tocar_bocina(self):
        self.sistema_electrico.tocar_bocina()

# Uso del coche
coche = Coche()
coche.arrancar()
coche.acelerar()
coche.acelerar()
coche.encender_luces()
coche.tocar_bocina()
coche.frenar()
coche.detener()