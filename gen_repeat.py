#!/usr/bin/env python3

# Реализовать итератор, повторяющий элементы некоторого списка,
# определенного заранее.
# Подсказка: использовать функцию cycle() модуля itertools. Обратите
# внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
# предусмотреть условие его завершения.

from itertools import cycle
seq = input('Enter data through the space: ').split()
cnt = 0
for item in cycle(seq):
    if cnt >= 10:
        break
    print(item)
    cnt += 1
