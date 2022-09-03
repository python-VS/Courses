# Дан список.
# Необходимо поменять местами самый большой и самый маленький элементы списка.
# Результаты вывести на экран.

from random import randint

list_1 = [randint(1, 10) for i in range(6)]
print(list_1)
a, b = list_1.index(min(list_1)), list_1.index(max(list_1))
list_1[a], list_1[b] = list_1[b], list_1[a]
print(list_1)