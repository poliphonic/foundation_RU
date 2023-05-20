#!/usr/bin/env python3

# Создать программный файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка.

with open('empty_end.txt', 'w', encoding='utf-8') as ouf:
    line = input()
    while line:
        ouf.write(f'{line}\n')
        line = input()
