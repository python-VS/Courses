# Напишите функцию inspect_function(),
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
# В результате работы она выводит следующие данные:
# -название анализируемой функции,
# -наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.)

import inspect
from collections.abc import Callable


def sum_range(_start: int, _end: int, _step: int = 0) -> int:
    _start, _end = (_start, _end) if _start <= _end else (_end, _start)
    return sum(range(_start, _end, _step))


def inspect_function(func: Callable):
    print(f'Название функции: {func.__name__}')
    print('Принимаемые параметры:')
    for param in inspect.signature(func).parameters.values():
        print(' - ' + param.name, param.kind, sep=': ')


inspect_function(sum_range)
