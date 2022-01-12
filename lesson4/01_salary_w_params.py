#!/usr/bin/env python3

# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах * ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv
try:
    seq = [int(i) for i in argv[1:]]
    assert len(seq) == 3
except ValueError:
    print('All the parameters have to be integers')
except AssertionError:
    print('There must be exactly three parameters, no more no less')
else:
    print(seq[0] * seq[1] + seq[2])
