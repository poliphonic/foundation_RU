#!/usr/bin/env python3

# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль —
# выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.

revenue = int(input('The revenue of your company is '))
cost = int(input('The cost of your company is '))
if revenue > cost:
    print('Your company has a profit')
    profit = revenue - cost
    print("Your return on sales is", int(profit / revenue * 100))
    employees = int(input('How many employees is in your company? '))
    print('Your profit per employee is', profit // employees)
else:
    print('Your company has a loss')
