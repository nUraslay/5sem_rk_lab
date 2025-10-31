from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    """Абстрактный класс Геометрическая фигура"""

    @abstractmethod
    def area(self):
        """Вычисление площади фигуры"""
        pass
