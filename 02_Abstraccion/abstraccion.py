from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.14 * self.radio


# Uso
circulo = Circulo(5)
print("Área del círculo:", circulo.area())  # Área del círculo: 78.5
print("Perímetro del círculo:", circulo.perimetro())  # Perímetro del círculo: 31.400000000000002
