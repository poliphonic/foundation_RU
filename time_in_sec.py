#!/usr/bin/env python3

# Пользователь вводит время в секундах. Переведите время в часы, минуты
# и секунды и выведите в формате чч:мм:сс. Используйте форматирование
# строк.

hours, left_time = divmod(int(input()), 3600)
minutes, seconds = divmod(left_time, 60)
print(f'{hours % 24:02}:{minutes:02}:{seconds:02}')
