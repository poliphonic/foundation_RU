#!/usr/bin/env python3

# Создать класс TrafficLight (светофор).
# Определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный,
# жёлтый, зелёный.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 3 секунды, третьего (зелёный) — 7.
# Переключение между режимами должно осуществляться только в указанном
# порядке (красный, жёлтый, зелёный).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его
# нарушении выводить соответствующее сообщение и завершать скрипт.

from termcolor import cprint
from time import sleep


class TrafficLight:

    __color = ('red', 'yellow', 'green')

    @classmethod
    def running(cls):
        """
        return None
        print colored squares in this order: red, yellow, green
        """
        for light in TrafficLight.__color:
            cprint(123, light, on_color=f'on_{light}')
            sleep(3) if light == 'yellow' else sleep(7)


switch_lights = TrafficLight()
try:
    assert switch_lights._TrafficLight__color == ('red', 'yellow', 'green')
except AssertionError:
    cprint('Attention! Private attribute was changed! Access denied!', 'red')
else:
    switch_lights.running()
