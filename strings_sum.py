#  Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#  Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
num = input()
if num.startswith('-'):
    print(int(num) - int(2 * num[1:]) - int(3 * num[1:]))
else:
    print(int(num) + int(2 * num) + int(3 * num))
