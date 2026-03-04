from abc import ABC, abstractmethod
import math

class IForma(ABC):
    @abstractmethod
    def obtener_area(self) -> float:
        """Contrato obligatorio para el cálculo de área."""
        pass

class Cuadrado(IForma):
    def __init__(self, lado: float):
        self.__lado = lado

    def obtener_area(self) -> float:
        return self.__lado ** 2

class Circulo(IForma):
    def __init__(self, radio: float):
        self.__radio = radio

    def obtener_area(self) -> float:
        return math.pi * (self.__radio ** 2)

class Triangulo(IForma):
    def __init__(self, base: float, altura: float):
        self.__base = base
        self.__altura = altura

    def obtener_area(self) -> float:
        return (self.__base * self.__altura) / 2

def imprimir_area(forma: IForma):
    """
    Polimorfismo puro: Recibe cualquier objeto que 
    firme el contrato de IForma.
    """
    print(f"El área procesada es: {forma.obtener_area():.2f}")


if __name__ == "__main__":
    figuras = [
        Cuadrado(5), 
        Circulo(15), 
        Triangulo(4, 3)
    ]

    for f in figuras:
        imprimir_area(f)





