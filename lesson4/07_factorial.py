#!/usr/bin/env python3

# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в
# цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
# факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(num):
    """
    num: a natural number
    return: a generator of factorials from 1 to num inclusively
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
        yield factorial


for el in fact(int(input('Enter a natural number: '))):
    print(el)


