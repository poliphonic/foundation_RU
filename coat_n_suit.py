#!/usr/bin/env python3

# Реализовать проект расчёта суммарного расхода ткани на производство
# одежды. Основная сущность (класс) этого проекта — одежда, которая
# может иметь определённое название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V / 6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике
# полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора
# @property.

from abc import ABC, abstractmethod


class Clothing(ABC):

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothing):

    def __init__(self, size):
        """
        size: a natural number
        """
        self.size = size

    @property
    def fabric(self):
        """
        return: a float got by formula size / 6.5 + .5
        """
        return round(self.size / 6.5 + .5, 2)

    def __add__(self, other):
        return f'Потребуется {round(self.fabric + other.fabric, 2)} м ткани.'


class Suit(Clothing):

    def __init__(self, height):
        """
        size: a float
        """
        self.height = height

    @property
    def fabric(self):
        """
        return: a float got by formula height * 2 + .3
        """
        return round(self.height * 2 + .3, 2)

    def __add__(self, other):
        return f'Потребуется {round(self.fabric + other.fabric, 2)} м ткани.'


coat = Coat(48)
suit = Suit(1.78)
print(coat + suit)
