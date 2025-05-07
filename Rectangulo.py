from Figura geometrica import Figura geometrica

class Rectangulo(Figura geometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Rectángulo de alto {self._alto}, ancho {self._ancho}, área {self.area()}'
