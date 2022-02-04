#!/usr/bin/env python3

# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках класса
# реализовать два метода. Первый, с декоратором @classmethod. Он должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.


class Date:

    def __init__(self, date):
        """
        date: a string
        """
        self.date = date

    def __str__(self):
        return Date.validator(Date.extractor(self.date))

    @classmethod
    def extractor(cls, date):
        """
        date: a string
        return: a tuple of three elements
        """
        day, month, year = [int(i) for i in date.split('-')]
        return day, month, year

    @staticmethod
    def validator(obj):
        """
        obj: a tuple
        return: one string if condition else the other
        """
        if 0 < obj[0] < 32 and 0 < obj[1] < 13 and 0 < obj[2] < 2023:
            # no future :(
            return 'This is correct date.'
        else:
            return 'This is incorrect date. Check your data.'


today = Date('26-01-2022')
print(today)
tomorrow = Date('32-01-2022')
print(tomorrow)
