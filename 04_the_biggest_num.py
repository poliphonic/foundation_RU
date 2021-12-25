# Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические
# операции.

# num = int(input())
# max_num = 0
# while num:
#     num, current_digit = divmod(num, 10)
#     if current_digit > max_num:
#         max_num = current_digit
# print(max_num)

print(max(list(input())))
