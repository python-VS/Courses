# Имеется список с произвольными данными.
# Необходимо преобразовать его во множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.
# Результаты выведите на экран. Использовать lambda-функции.

from collections.abc import Hashable

f = [1, 'strrrr', [5, 6], {6, 9}, {'b': 5, 'h': 7}, 6.66]

my_lambda = lambda x: set(i for i in x if isinstance(i, Hashable) == True)

print(my_lambda(f))
