from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.14 * self.radio

circulo = Circulo(5)

print("Area del circulo: ", circulo.area())
print("Area del perimetro: ", circulo.perimetro())
