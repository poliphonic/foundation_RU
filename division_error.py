#!/usr/bin/env python3

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на ноль. Проверьте его работу на данных, вводимых пользователем. При
# вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class DivisionError(Exception):

    def __str__(self):
        return 'На ноль делить нельзя!'


try:
    x, operator, y = input('Введите первое число, пробел, знак операции над '
                           'числами, пробел, второе число:\n').split()
    if not float(y) and operator in '//%':
        raise DivisionError
except DivisionError as error:
    print(error)
else:
    print(eval(f'{x} {operator} {y}'))
