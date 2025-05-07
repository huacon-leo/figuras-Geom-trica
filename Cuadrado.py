from Figura geometrica import Figura geometrica

class Cuadrado(Figura geometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Cuadrado de lado {self._alto}, área {self.area()}'

