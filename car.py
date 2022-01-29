#!/usr/bin/env python3

# Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните
# доступ к атрибутам, выведите результат. Вызовите методы и покажите
# результат.


class Car:

    def __init__(self, speed, color, name, is_police=False):
        """
        speed: an integer
        color: a string
        name: a string
        is_police: a boolean
        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.current_speed = 0

    def go(self):
        """
        return: the string 'car_name is on its way'
        """
        self.current_speed = self.speed
        return f'{self.name} is on its way'

    def stop(self):
        """
        return: the string 'car_name stopped'
        """
        self.current_speed = 0
        return f'{self.name} stopped'

    def turn(self, direction):
        """
        direction: a string
        return: the string 'car_name turned direction'
        """
        return f'{self.name} turned {direction}'

    def show_speed(self):
        """
        return: None
        print the current speed of the car
        """
        print(f'Current speed of {self.name} is {self.current_speed}')


class TownCar(Car):

    def show_speed(self):
        """
        return: None
        print the current speed of the car, then the warning message if
            current speed is higher than 60
        """
        super().show_speed()
        if self.current_speed > 60:
            print('Over speed! Slow down, please!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        """
        return: None
        print the current speed of the car, then the warning message if
            current speed is higher than 40
        """
        super().show_speed()
        if self.current_speed > 40:
            print('Over speed! Slow down, please!')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        """
        speed: an integer
        color: a string
        name: a string
        """
        super().__init__(speed, color, name, is_police=True)


cooper = TownCar(68, 'red', 'Mini Cooper')
print(f'Name of the car - {cooper.name}')
print(f'Its normal speed - {cooper.speed} miles per hour')
print(f'Its color - {cooper.color}')
print(f'It is {"" if cooper.is_police else "not "}a police car')
cooper.show_speed()
print(cooper.go())
print(cooper.turn('right'))
print(cooper.turn('left'))
print(cooper.turn('back'))
cooper.show_speed()
print(cooper.stop())
cooper.show_speed()
print()

delorean = SportCar(88, 'silver', 'DeLorean')
print(f'Name of the car - {delorean.name}')
print(f'Its normal speed - {delorean.speed} miles per hour')
print(f'Its color - {delorean.color}')
print(f'It is {"" if delorean.is_police else "not "}a police car')
delorean.show_speed()
print(delorean.go())
print(delorean.turn('right'))
print(delorean.turn('left'))
print(delorean.turn('back'))
delorean.show_speed()
print(delorean.stop())
delorean.show_speed()
print()

jeep = WorkCar(58, 'khaki', 'Jeep')
print(f'Name of the car - {jeep.name}')
print(f'Its normal speed - {jeep.speed} miles per hour')
print(f'Its color - {jeep.color}')
print(f'It is {"" if jeep.is_police else "not "}a police car')
jeep.show_speed()
print(jeep.go())
print(jeep.turn('right'))
print(jeep.turn('left'))
print(jeep.turn('back'))
jeep.show_speed()
print(jeep.stop())
jeep.show_speed()
print()

ford = PoliceCar(78, 'white', 'Ford')
print(f'Name of the car - {ford.name}')
print(f'Its normal speed - {ford.speed} miles per hour')
print(f'Its color - {ford.color}')
print(f'It is {"" if ford.is_police else "not "}a police car')
ford.show_speed()
print(ford.go())
print(ford.turn('right'))
print(ford.turn('left'))
print(ford.turn('back'))
ford.show_speed()
print(ford.stop())
ford.show_speed()
