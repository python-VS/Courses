# Имеется список с произвольными данными.
# Необходимо преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.
# Результаты выведите на экран.

from collections.abc import Hashable

list_1 = [1, 'a', 5, 3.2, {1, 2, 3}]
x = {i for i in list_1 if isinstance(i, Hashable)}

print(x)