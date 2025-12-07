from app import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("Тест add пройден")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0
    print("Тест subtract пройден")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    print("Тест multiply пройден")

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(1, 2) == 0.5
    print("Тест divide пройден")

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Должно быть исключение"
    except ValueError:
        print("Тест divide_by_zero пройден")

if __name__ == "__main__":
    print("Запуск тестов")
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("Все тесты пройдены успешно")
