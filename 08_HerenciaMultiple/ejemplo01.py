class A:
    def metodo(self):
        print("Método de A")

class B:
    def metodo(self):
        print("Método de B")

class C(A, B):
    pass

obj = C()
obj.metodo()  # Método de A (MRO - Method Resolution Order)
