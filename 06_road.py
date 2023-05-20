#!/usr/bin/env python3

# Реализовать класс Road (дорога).
# Определить атрибуты length (длина) и width (ширина).
# Значения атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищёнными.
# Определить метод расчёта массы асфальта, необходимого для покрытия
# всей дороги.
# Использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины
# полотна.
# Проверить работу метода.
# Например: 20 м * 5000 м * 25 кг * 5 см = 12500 т.

from math import ceil


class Road:

    def __init__(self, length, width):
        """
        length: a natural number
        width: a natural number
        """
        self._length = length
        self._width = width

    def weight(self, mean=25, depth=5):
        """
        mean: a natural number
        depth: a natural number
        return: length * width * mean * depth / 1000 with round up
        """
        return f'{ceil(self._length * self._width * mean * depth / 1000)} т'


my_way = Road(5000, 20)
print(my_way.weight())
