#Дан список чисел.
# Превратите его в список квадратов этих чисел.
# Результаты вывести на экран.

from random import randint

list_1 = [randint(1, 10) for _ in range(10)]

print([i ** 2 for i in list_1])