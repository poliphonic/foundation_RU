# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

s_list = [*['зима'] * 2, *['весна'] * 3, *['лето'] * 3, *['осень'] * 3, 'зима']
s_dict = {key: value for key, value in enumerate(s_list, 1)}
# print(s_list[int(input())])
print(s_dict[int(input())])