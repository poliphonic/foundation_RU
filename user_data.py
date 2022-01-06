#!/usr/bin/env python3

# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_data(name, surname, year, city, email, phone):
    """
    name: a string
    surname: a string
    year: a string
    city: a string
    email: a string
    phone: a string
    return: A string with input user info.
    """
    return '{} {}, was born in {}, lives in {}. Contacts: email - {}, phone' \
           ' - {}.'.format(name, surname, year, city, email, phone)


nm, snm = input('Your name: '), input('Your surname: ')
yr, ct = input('Your birth year: '), input('Your city of living: ')
eml, phn = input('Your e-mail: '), input('Your phone number: ')
print(user_data(city=ct, email=eml, name=nm, phone=phn, surname=snm, year=yr))