# Дан список.
# Необходимо вывести список в обратном порядке

from random import randint

list_1 = [randint(1, 100) for i in range(10)]

print(sorted(list_1, reverse=True))