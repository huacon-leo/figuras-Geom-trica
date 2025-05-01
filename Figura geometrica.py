# Clase base FiguraGeometrica
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

    def perimetro(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")


# Clase Rectángulo que hereda de FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


# Clase Cuadrado que hereda de Rectángulo
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)  # Un cuadrado es un rectángulo con lados iguales


# Crear instancias
rectangulo = Rectangulo(4, 6)
cuadrado = Cuadrado(5)

print(f"Rectángulo: Área = {rectangulo.area()}, Perímetro = {rectangulo.perimetro()}")
print(f"Cuadrado: Área = {cuadrado.area()}, Perímetro = {cuadrado.perimetro()}")