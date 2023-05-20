#!/usr/bin/env python3

# Реализовать базовый класс Worker (работник).
# Определить атрибуты: name, surname, position (должность), income
# (доход). Последний атрибут должен быть защищённым и ссылаться на
# словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income).
# Проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать
# методы экземпляров.


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        """
        name: a string
        surname: a string
        position: a string
        wage: an integer
        bonus: a integer
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        """
        name: a string
        surname: a string
        position: a string
        wage: an integer
        bonus: a integer
        """
        super().__init__(name, surname, position, wage, bonus)
        self._income = self._income

    def get_full_name(self):
        """
        return: a string, name + ' ' + surname
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
        return: an integer, wage + bonus
        """
        return self._income['wage'] + self._income['bonus']


sherlock = Position('Sherlock', 'Holmes', 'detective consultant', 12000, 70)
print(f'Name - {sherlock.name}')
print(f'Surname - {sherlock.surname}')
print(f'Position - {sherlock.position}')
print(f'Income - {sherlock._income}')
print(f'Wage - {sherlock._income["wage"]}')
print(f'Bonus - {sherlock._income["bonus"]}')
print(f'Full name - {sherlock.get_full_name()}')
print(f'Total income - {sherlock.get_total_income()}')

jim = Position('Jim', 'Moriarty', 'criminal consultant', 700, 1200000)
print(f'Name - {jim.name}')
print(f'Surname - {jim.surname}')
print(f'Position - {jim.position}')
print(f'Income - {jim._income}')
print(f'Wage - {jim._income["wage"]}')
print(f'Bonus - {jim._income["bonus"]}')
print(f'Full name - {jim.get_full_name()}')
print(f'Total income - {jim.get_total_income()}')
