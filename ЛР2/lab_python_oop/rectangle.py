from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import FigureColor

class Rectangle(GeometricFigure):
    figure_type = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} цвета {} шириной {} и высотой {}. Площадь: {:.2f}".format(
            self.figure_type, self.color.color, self.width, self.height, self.area()
        )
