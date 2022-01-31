#!/usr/bin/env python3

# Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число». Реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта. Для этого
# создаёте экземпляры класса (комплексные числа), выполните сложение и
# умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class Complex:

    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imaginary = self.imag * other.real + self.real * other.imag
        return Complex(real, imaginary)

    def __str__(self):
        sign = '-' if self.imag < 0 else '+'
        return f'({self.real}{sign}{abs(self.imag)}j)'


num1 = Complex(2, -3)
num2 = Complex(5)
print(f'The first number is {num1}')
print(f'The second number is {num2}')
print(f'The sum of numbers is {num1 + num2}')
print(f'The product of numbers is {num1 * num2}')
