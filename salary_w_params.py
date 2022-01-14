#!/usr/bin/env python3

# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах * ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv
try:
    hours, rate, bonus = map(int, argv[1:])
    print(hours * rate + bonus)
except ValueError:
    print('There must be exactly three integers')
