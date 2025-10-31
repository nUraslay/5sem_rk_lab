# Объектно-ориентированная версия решения биквадратного уравнения
import sys   # для аргументов командной строки
import math  # для квадратных корней и других функций

class BiquadraticEquation:
    """Класс, описывающий биквадратное уравнение A*x^4 + B*x^2 + C = 0"""

    def __init__(self, a, b, c):
        # Конструктор класса: сохраняет коэффициенты как свойства объекта
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        """Метод для вычисления дискриминанта: D = B² - 4AC"""
        return self.b**2 - 4*self.a*self.c  

    def solve(self):
        """Метод решает уравнение и выводит действительные корни."""
        print(f"\nРешаем уравнение: ({self.a})x⁴ + ({self.b})x² + ({self.c}) = 0")  

        if self.a == 0:  
            print("Ошибка: коэффициент A не может быть равен 0 (это не биквадратное уравнение).")
            return []  

        D = self.discriminant()  
        print(f"Дискриминант D = {D:.4f}")  

        if D < 0:  
            print("Действительных корней нет (дискриминант отрицателен).")
            return []

       
        y1 = (-self.b + math.sqrt(D)) / (2*self.a)
        y2 = (-self.b - math.sqrt(D)) / (2*self.a)
        print(f"Промежуточные значения: y₁ = {y1:.4f}, y₂ = {y2:.4f}")

        roots = [] 

        
        for y in [y1, y2]:
            if y > 0:
                roots.extend([math.sqrt(y), -math.sqrt(y)]) 
            elif y == 0:
                roots.append(0.0)  

        if roots: 
            roots = sorted(roots)  
            print("Действительные корни уравнения:", ", ".join(f"{r:.4f}" for r in roots))
        else:
            print("Действительных корней нет (y < 0).")

        return roots  # Возвращаем список найденных корней


def get_coefficient(name, args, index):
    """Функция получает коэффициент из командной строки или с клавиатуры"""
    while True:  
        try:
            # Берем значение из аргументов, если есть, иначе запрашиваем ввод
            value = args[index] if len(args) > index else input(f"Введите коэффициент {name}: ")
            return float(value)  
        except ValueError:
            print(f"Ошибка: коэффициент {name} должен быть числом. Повторите ввод.")


def main():
    """Главная функция программы."""
    args = sys.argv[1:]  
    a = get_coefficient("A", args, 0)  
    b = get_coefficient("B", args, 1)  
    c = get_coefficient("C", args, 2)  

    equation = BiquadraticEquation(a, b, c)  # Создаем объект уравнения
    equation.solve()  


if __name__ == "__main__":  # Проверяем, запущен ли файл напрямую
    main() 