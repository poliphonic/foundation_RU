#!/usr/bin/env python3

# Начните работу над проектом «Расширяющийся склад». Создайте класс,
# описывающий склад. А также класс «Волшебная коробка», который будет
# базовым для классов-наследников. Эти классы — конкретные типы
# магических предметов (волшебные палочки, книги заклинаний, зелья). В
# базовом классе определите параметры, общие для приведённых типов. В
# классах-наследниках реализуйте параметры, уникальные для каждого типа
# предметов.
# Разработайте методы, которые отвечают за приём предметов на склад и
# передачу в определённый магазин на Косой Аллее. Для хранения данных о
# наименовании и количестве предметов, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).
# Валидатор использовать не буду, у меня пользователь не вводит данные.

from functools import reduce


class ExpandingStorage:

    def __init__(self):
        self.__total = 1
        self.__used = 0
        self.__num = 2
        box_list = ['Magic box', 'Wand box', 'Spell book box', 'Potion box']
        self.__storage = {name: dict(number=0, length=0, width=0, height=0,
                                     content='nothing') for name in box_list}

    def __str__(self):
        space = f'Total space of Magic Expanding Storage - {self.__total}'
        if self.__used == self.__total:
            free = 'there is no free space'
        else:
            free = f'free space - {self.__total - self.__used} cu ft'
        inventory = []
        for key, value in self.__storage.items():
            if self.__storage[key]['number'] > 0:
                inventory.append(f'{self.__storage[key]["number"]} {key}(es)')
        if not inventory:
            inventory = 'There is nothing'
        elif len(inventory) == 1:
            inventory = f'There is {inventory[0][:-4].lower()}'
        else:
            inventory = f'There are {", ".join(inventory).lower()}'
        return f'{space} cu ft, {free}. {inventory}.'

    def add_box(self, item):
        """
        item: object of MagicBox class
        return: a string with a massage of success
        change values of self.used and self.storage
        """
        if item.name not in self.__storage:
            print('You cannot add this item to the Storage. Try to cast.')
            return
        measurements = [item.length, item.width, item.height]
        self.__used += reduce(lambda x, y: x * y, measurements)
        while self.__used > self.__total:
            self.use_expand_spell()
            # there's no counter spell!
        cnt = f'{item.quantity} {item.content}' if item.quantity else 'nothing'
        self.__storage[item.name]['number'] += 1
        self.__storage[item.name]['length'] += item.length
        self.__storage[item.name]['width'] += item.width
        self.__storage[item.name]['height'] += item.height
        self.__storage[item.name]['content'] = cnt
        name = f'The {item.name.lower()}'
        return f'{name} was successfully added to the Magic Expanding Storage.'

    def use_expand_spell(self):
        """
        return: None
        change a value of self.total
        """
        self.__total = self.__num ** self.__num
        self.__num += 1

    def take_box(self, item):
        """
        item: object of MagicBox class
        return: a string reported about request condition
        change values of self.used and self.storage
        """
        if not self.__storage[item.name]['number']:
            return 'There is no such box in the Magic Expanding Storage.'
        else:
            self.__storage[item.name]['number'] -= 1
            if not self.__storage[item.name]['number']:
                self.__storage[item.name]['content'] = 'nothing'
            self.__storage[item.name]['length'] -= item.length
            self.__storage[item.name]['width'] -= item.width
            self.__storage[item.name]['height'] -= item.height
            measurements = [item.length, item.width, item.height]
            self.__used -= reduce(lambda x, y: x * y, measurements)
            books, potions = 'Flourish & Blotts', 'Slug and Jiggers Apothecary'
            idk = 'no one knows where.'
            if item.name == 'Wand box':
                return 'The box with wands has been sent to "Ollivanders".'
            elif item.name == 'Spell book box':
                return f'The box with spell books has been sent to "{books}".'
            elif item.name == 'Potion box':
                return f'The box with potions has been sent to "{potions}".'
            else:
                return f'The magic box has been sent somewhere, {idk}'


class MagicBox:

    def __init__(self, name='Magic box', length=1, width=1, height=1,
                 quantity=0, content='nothing'):
        """
        name: a string
        length: an integer
        width: an integer
        height: an integer
        quantity: an integer
        content: a string
        """
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.quantity = quantity
        self.content = content
        if not length % 2 and not width % 2 and not height % 2:
            self.reduce_box_spell()

    def __str__(self):
        num = f'{self.quantity} ' if self.quantity else ''
        return f'This is a {self.name}. It contains {num}{self.content}.'

    def reduce_box_spell(self):
        """
        return: None
        change self.info if condition
        """
        self.length = self.length // 2
        self.width = self.width // 2
        self.height = self.height // 2
        print(f'{self.name} was successfully reduced.')


class WandBox(MagicBox):

    def __init__(self):
        content = 'wands in their own boxes'
        super().__init__(name='Wand box', quantity=100, content=content)


class SpellBookBox(MagicBox):

    def __init__(self):
        content = 'books of spells'
        super().__init__(name='Spell book box', quantity=4, content=content)


class PotionBox(MagicBox):
    def __init__(self):
        content = 'test-tubes with different potions'
        super().__init__(name='Potion box', quantity=25, content=content)


tent = ExpandingStorage()
print(tent)
empty = MagicBox(length=2, width=2, height=2)
print(empty)
wand = WandBox()
print(wand)
book = SpellBookBox()
print(book)
potion = PotionBox()
print(potion)
print(tent.add_box(empty))
print(tent)
print(tent.add_box(wand))
print(tent)
print(tent.add_box(book))
print(tent)
print(tent.add_box(potion))
print(tent)
print(tent.take_box(empty))
print(tent)
print(tent.take_box(wand))
print(tent)
print(tent.take_box(book))
print(tent)
print(tent.take_box(potion))
print(tent)
