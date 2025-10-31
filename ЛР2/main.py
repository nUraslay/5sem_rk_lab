from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

# внешний пакет - prettytable (pip install prettytable уже установлен)
from prettytable import PrettyTable

def main():
    N = 5  # замените на ваш номер варианта
    rect = Rectangle(N, N, "синий")
    circle = Circle(N, "зелёный")
    square = Square(N, "красный")

    print(rect)
    print(circle)
    print(square)

    table = PrettyTable(["Фигура", "Цвет", "Площадь"])
    table.add_row([rect.figure_type, rect.color.color, f"{rect.area():.2f}"])
    table.add_row([circle.figure_type, circle.color.color, f"{circle.area():.2f}"])
    table.add_row([square.figure_type, square.color.color, f"{square.area():.2f}"])

    print("\nТаблица фигур:")
    print(table)

if __name__ == "__main__":
    main()

# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass (обход блокировки - временный)
# venv\Scripts\activate
# python .\main.py (команда для запуска программы)
 
