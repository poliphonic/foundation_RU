#!/usr/bin/env python3

# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки».
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle
# (маркер).
# В каждом классе реализовать переопределение метода draw. Для каждого
# класса метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.


class Stationery:

    def __init__(self, title='Something of that can draw'):
        self.title = title

    def draw(self):
        """
        return: None
        print message
        """
        print(f'Just start drawing! {self.title}!')


class Pen(Stationery):

    def draw(self):
        """
        return: None
        print message
        """
        print(f'I gonna write letters in the notebook with my {self.title}.')


class Pencil(Stationery):

    def draw(self):
        """
        return: None
        print message
        """
        print(f'I gonna draw funny faces in the sketchbook with my '
              f'{self.title}.')


class Handle(Stationery):

    def draw(self):
        """
        return: None
        print message
        """
        print(f'I gonna picture an explanation of a difficult topic for my '
              f'pupils on the class board with my {self.title}.')


stationery = Stationery()
stationery.draw()

pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()
