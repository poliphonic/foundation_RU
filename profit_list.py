#!/usr/bin/env python3

# Создать вручную и заполнить несколькими строками текстовый файл, в
# котором каждая строка будет содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в
# расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000,
# "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

from json import dump
d = {}
with open('firms.txt') as inf:
    for line in inf:
        firm, ownership, revenue, cost = line.split()
        d[firm] = int(revenue) - int(cost)
temp = [value for value in d.values() if value > 0]
res = [d, {'average profit': int(sum(temp) / len(temp))}]
with open('firms.json', 'w') as ouf:
    dump(res, ouf, ensure_ascii=False)
