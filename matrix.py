#!/usr/bin/env python3

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список
# списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода
# матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый
# элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, matrix):
        """
        matrix: a list
        """
        self.matrix = matrix
        self.shape = (len(self.matrix), len(self.matrix[0]))

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, seq)) for seq in self.matrix])

    def __add__(self, other):
        if self.shape == other.shape:
            return Matrix([[a + b for a, b in zip(x, y)]
                           for x, y in zip(self.matrix, other.matrix)])
        else:
            return 'The matrices have to be the same shape!'


m1 = Matrix([[31, 32], [37, 43], [51, 86]])
m2 = Matrix([[3, 5], [2, 4], [-1, 64]])
m3 = Matrix([[8, 3], [7, 1], [6, -8]])
print(m1 + m2 + m3)
