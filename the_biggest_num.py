# Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические
# операции.

# num = input()
# max_num = 0
# while num != '0':
#     num_int, current_digit = divmod(int(num), 10)
#     num = str(num_int)
#     if current_digit > max_num:
#         max_num = current_digit
# print(max_num)

print(max([int(char) for char in list(input())]))
