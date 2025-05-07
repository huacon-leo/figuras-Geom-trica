class FiguraGeometrica:
    def __init__(self, alto=0, ancho=0):
        self._alto = alto
        self._ancho = ancho

    def get_alto(self):
        return self._alto

    def set_alto(self, alto):
        self._alto = alto

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return f'Alto: {self._alto}, Ancho: {self._ancho}'

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Cuadrado de lado {self._alto}, área {self.area()}'

class Rectangulo(FiguraGeometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Rectángulo de alto {self._alto}, ancho {self._ancho}, área {self.area()}'

if __name__ == "__main__":
    cuadrado = Cuadrado(7)
    print(cuadrado)

    rectangulo = Rectangulo(4, 6)
    print(rectangulo)


