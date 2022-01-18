#!/usr/bin/env python3

# Создать текстовый файл (не программно), сохранить в нём несколько
# строк, выполнить подсчёт строк и слов в каждой строке.

strings, words = 0, 0
with open('mashnin.txt') as inf:
    for line in inf:
        length = len(line.strip().replace('-', ' ').split())
        strings += 1
        words += length
        print(f'{strings} string - {length} words')
print(f'{strings} strings with {words} words in total')
