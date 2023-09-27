# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fib(n1):
    """
    Генератор чисел Фибоначчи
    :param n1: До какого числа генерируем последовательность чисел Фибоначчи
    :return: Список чисел Фибоначчи от 1 до n1
    """
    a, b = 0, 1
    for _ in range(n1):
        yield a
        a, b = b, a + b


def fib_n(n1):
    """
    Возвращает n1-ое число Фибоначчи из последовательности
    :param n1:
    :return:
    """
    _ = 0
    for _ in fib(n1):
        pass
    return _


if __name__ == '__main__':  # Сама программа
    print('Ряды чисел Фибоначчи 10 и 20 чисел')
    print(list(fib(10)))
    print(list(fib(20)))

    print(f'41-е число ряда Фибоначчи: {fib_n(41)}')

# Результат работы программы:
# C:\Work\python\dz4\Py4HW05\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW05/task03.py
# Ряды чисел Фибоначчи 10 и 20 чисел
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
# 41-е число ряда Фибоначчи: 102334155
#
# Process finished with exit code 0
