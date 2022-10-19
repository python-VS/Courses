# Написать функцию-декоратор, которая вычисляет время выполнения декорируемой функции,
# а также выводит на экран имя функции и ее параметры.

import time

RUSSIAN_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчщъьэюя'


def params_and_name_printer(func):
    def wrapper(*args, **kwargs):
        print(f'Название функции: {func.__name__}')
        print(f'Позиционные параметры: {args}')
        print(f'Ключевые параметры: {kwargs}')
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Время выполнения: {end - start}')
        return result
    return wrapper


@params_and_name_printer
def is_pangram(in_string: str) -> bool:
    in_string = in_string.lower()
    letter_counter = {
        letter: in_string.count(letter) for letter in RUSSIAN_ALPHABET
    }
    return 0 not in letter_counter.values()


_string = ''
is_pangram(_string)