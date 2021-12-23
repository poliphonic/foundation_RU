# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в
# переменные, выведите на экран.

name = input('What is your name? ')
quest = ' '.join(input('What is your quest? ').split()[1:])
colour = input('What is your favourite colour? ')
print(f'So your name is {name}, you {quest}, and your favourite colour is '
      f'{colour}. Right. Off you go.')

# даже если бы у пользователя запрашивались числа, которые не
# запрашиваются, я бы не стала приводить их к типу int, потому что это
# не нужно здесь
