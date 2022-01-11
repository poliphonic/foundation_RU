#!/usr/bin/env python3

# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(num1, num2, num3):
    """
    num1: an integer
    num2: an integer
    num3: an integer
    return: A sum of two biggest numbers.
    """
    return sum(sorted([num1, num2, num3])[1:])


n1, n2, n3 = map(int, input('Введите три целых числа через пробел: ').split())
print('Сумма двух самых больших из них равна', my_func(n1, n2, n3))
