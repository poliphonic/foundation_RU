#!/usr/bin/env python3

# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

s_list = ['зима', 'весна', 'лето', 'осень', 'зима']
s_dict = {key: s_list[key // 3] for key in range(1, 13)}
# print(s_list[int(input()) // 3])
print(s_dict[int(input())])

