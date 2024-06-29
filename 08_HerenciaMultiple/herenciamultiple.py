class A:
    def metodo(self):
        print("Metodo de A")


class B:
    def metodo(self):
        print("Metodo de B")


class C(B, A):
    def metodo(self):
        print("Metodo Mixto - C")

obj = C()
obj.metodo()
