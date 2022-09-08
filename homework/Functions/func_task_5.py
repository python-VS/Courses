# Написать функцию-декоратор, которая вычисляет время выполнения декорируемой функции,
# а также выводит на экран имя функции и ее параметры.

import time

def decorator(func):
    def inner():
        print('tttttttt')
        func()
        print('gggggggggg')
    return inner()

def say():
    print('15651')

say = decorator(say)
say()
