# Процедурная версия решения биквадратного уравнения
#------------------------------------------------------
import sys   # используется для получения аргументов командной строки
import math  # используется для математических функций (например, sqrt)

def input_coefficient(name, args, index):
    """Функция получает коэффициент (из командной строки или с клавиатуры) с проверкой корректности."""
    while True:  
        try:
            
            value = args[index] if len(args) > index else input(f"Введите коэффициент {name}: ")
            return float(value)  
        except ValueError:
            # Если введено не число — выводим сообщение и повторяем ввод
            print(f"Ошибка: коэффициент {name} должен быть числом. Повторите ввод.")

def solve_biquadratic(a, b, c):
    """Решает биквадратное уравнение A*x^4 + B*x^2 + C = 0"""
    print(f"\nРешаем уравнение: ({a})x⁴ + ({b})x² + ({c}) = 0")  

    if a == 0:  
        print("Ошибка: коэффициент A не может быть равен 0 (это не биквадратное уравнение).")
        return []  

    D = b**2 - 4*a*c  
    print(f"Дискриминант D = {D:.4f}")  

    if D < 0:  
        print("Действительных корней нет (дискриминант отрицателен).")
        return [] 

    # Вычисляем два значения y (это x²)
    y1 = (-b + math.sqrt(D)) / (2*a)
    y2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Промежуточные значения: y₁ = {y1:.4f}, y₂ = {y2:.4f}") 
    roots = []  # Список для хранения корней уравнения

    # Для каждого найденного y ищем действительные корни x
    for y in [y1, y2]:
        if y > 0:  
            roots.extend([math.sqrt(y), -math.sqrt(y)])  
        elif y == 0:  
            roots.append(0.0)

    if roots:  # Если корни найдены
        roots = sorted(roots)  # Сортируем их по возрастанию
        print("Действительные корни уравнения:", ", ".join(f"{r:.4f}" for r in roots)) 
    else:
        print("Действительных корней нет (y < 0).")  

    return roots 


def main():
    """Главная функция программы."""
    args = sys.argv[1:]  # Список аргументов командной строки (пропускаем имя файла)
    a = input_coefficient("A", args, 0)  
    b = input_coefficient("B", args, 1)  
    c = input_coefficient("C", args, 2)  

    solve_biquadratic(a, b, c)  


if __name__ == "__main__": 
    main()