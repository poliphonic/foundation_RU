#!/usr/bin/env python3

# Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в
# степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый —
# возведение в степень с помощью оператора **. Второй — более сложная
# реализация без оператора **, предусматривающая использование цикла.


def my_func(num1, num2):
    """
    num1: a positive float
    num2: a negative integer
    return: num1 ** num2
    """
    # return round(num1 ** num2, 6)
    power = 1
    for i in range(abs(num2)):
        power *= num1
    return round(1 / power, 6)


n1 = float(input('Введите действительное положительное число: '))
n2 = int(input('Введите целое отрицательное число: '))
print(f'{n1} в степени {n2} равно', my_func(n1, n2))