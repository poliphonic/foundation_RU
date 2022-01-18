#!/usr/bin/env python3

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator
with open('nums_in.txt') as inf:
    with open('nums_out.txt', 'w') as ouf:
        for line in inf:
            line = line.split(' - ')
            translator = Translator()
            result = translator.translate(line[0], scr='en', dest='ru')
            ouf.write(f'{result.text} - {line[1]}')
