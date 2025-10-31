import math
from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import FigureColor

class Circle(GeometricFigure):
    figure_type = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "{} цвета {} радиусом {}. Площадь: {:.2f}".format(
            self.figure_type, self.color.color, self.radius, self.area()
        )
