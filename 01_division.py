#!/usr/bin/env python3
# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def division(num1, num2):
    """
    num1: an integer
    num2: an integer
    return: num1 / num2
    """
    return round(num1 / num2, 6)


try:
    n1, n2 = int(input('Введите делимое: ')), int(input('Введите делитель: '))
    print(f'Если разделить {n1} на {n2}, получится', division(n1, n2))
except ValueError:
    print('Вводить можно только целые числа!')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
