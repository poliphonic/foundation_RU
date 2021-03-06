#!/usr/bin/env python3

# Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения
# на реальном примере. Запрашивать у пользователя данные и заполнять
# список необходимо только числами.
# Примечание: длина списка не фиксирована. Элементы запрашиваются
# бесконечно, пока пользователь сам не остановит работу скрипта, введя,
# например, команду «stop». При этом скрипт завершается, сформированный
# список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить
# только числа и строки. Во время ввода пользователем очередного
# элемента необходимо реализовать проверку типа элемента. Вносить его в
# список, только если введено число. При этом работа скрипта не должна
# завершаться.


class NumsOnly(Exception):

    def __str__(self):
        return 'Вы ввели недопустимые символы!'


seq = []
print('Для выхода из программы нажмите "!"')
num_str = input('Вводите числа, каждое на новой строке:\n')
while num_str != '!':
    try:
        for char in num_str:
            if char not in '1234567890.-':
                raise NumsOnly
        seq.append(float(num_str) if '.' in num_str else (int(num_str)))
    except (ValueError, NumsOnly):
        error = NumsOnly()
        print(error)
    finally:
        num_str = input()
print(seq)
