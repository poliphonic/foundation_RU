#!/usr/bin/env python3

# Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделённых пробелами. Программа должна подсчитывать сумму
# чисел в файле и выводить её на экран.

from random import randint
cnt = 0
with open('random.txt', 'w+') as file:
    for length in range(randint(2, 20)):
        file.write(f'{randint(1, 101)}\n')
    file.seek(0)
    for num in file:
        cnt += int(num)
print(cnt)
