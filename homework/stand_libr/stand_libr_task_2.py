# Напишите программу, которая выводит факториал введенного числа.
# Код нахождения факториала должен быть написан в одну строку.

from math import factorial


def input_int(welcome_string: str) -> int:
    while True:
        try:
            number = int(input(welcome_string))
            if number <= 0:
                raise ValueError('Допустимы только положительные числа.')
        except ValueError:
            print('Вы ввели не целое число.')
        else:
            return number


if __name__ == '__main__':
    num = input_int('Введите, пожалуйста, число: ')
    print(factorial(num))
