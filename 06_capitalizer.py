#!/usr/bin/env python3
# Реализовать функцию int_func(), принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию int_func().

import string


def int_func(word):
    """
    word: a string
    return: capitalized word
    """
    return word.capitalize()


line = input('Введите строку из строчных латинских букв с пробелами: ').split()
for el in line:
    try:
        for letter in el:
            if letter not in string.ascii_lowercase:
                raise ValueError
    except ValueError:
        pass
    else:
        print(int_func(el), end=' ')
print()
