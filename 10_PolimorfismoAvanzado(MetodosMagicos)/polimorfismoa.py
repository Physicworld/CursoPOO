import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        """Sobrecarga del operador + para sumar dos puntos."""
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """Sobrecarga del operador - para restar dos puntos."""
        return Punto(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        """Sobrecarga del operador * para multiplicar un punto por un escalar."""
        return Punto(self.x * escalar, self.y * escalar)

    def __truediv__(self, escalar):
        """Sobrecarga del operador / para dividir un punto por un escalar."""
        return Punto(self.x / escalar, self.y / escalar)

    def __eq__(self, otro):
        """Sobrecarga del operador == para comparar dos puntos."""
        return self.x == otro.x and self.y == otro.y

    def __str__(self):
        """Representación en string del punto."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Representación oficial del punto."""
        return f"Punto({self.x}, {self.y})"

    def distancia_al_origen(self):
        """Calcula la distancia del punto al origen (0, 0)."""
        return math.sqrt(self.x**2 + self.y**2)

    def distancia_a(self, otro):
        """Calcula la distancia entre este punto y otro punto."""
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt(dx**2 + dy**2)

    @staticmethod
    def punto_medio(p1, p2):
        """Método estático para calcular el punto medio entre dos puntos."""
        return Punto((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

# Ejemplo de uso
p1 = Punto(1, 2)
p2 = Punto(3, 4)

# Suma de puntos
p3 = p1 + p2
print("p1 + p2 =", p3)  # (4, 6)

# Resta de puntos
p4 = p2 - p1
print("p2 - p1 =", p4)  # (2, 2)

# Multiplicación por escalar
p5 = p1 * 3
print("p1 * 3 =", p5)  # (3, 6)

# División por escalar
p6 = p2 / 2
print("p2 / 2 =", p6)  # (1.5, 2.0)

# Comparación de puntos
print("p1 == p2:", p1 == p2)  # False
print("p1 == Punto(1, 2):", p1 == Punto(1, 2))  # True

# Distancia al origen
print("Distancia de p1 al origen:", p1.distancia_al_origen())

# Distancia entre dos puntos
print("Distancia entre p1 y p2:", p1.distancia_a(p2))

# Punto medio
pm = Punto.punto_medio(p1, p2)
print("Punto medio entre p1 y p2:", pm)

# Representación de los puntos
print("Representación de p1:", repr(p1))