def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

if __name__ == "__main__":
    print("Калькулятор")
    print("Сложение: 10 + 5 =", add(10, 5))
    print("Вычитание: 10 - 5 =", subtract(10, 5))
    print("Умножение: 10 * 5 =", multiply(10, 5))
    print("Деление: 10 / 5 =", divide(10, 5))
