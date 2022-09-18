# Дан список чисел.
# Отсортировать числа по возрастанию по алгоритму Bubble Sort.
# Результаты вывести на экран

from random import randint

list_1 = ([randint(1, 11) for i in range(10)])
print(list_1)
for i in range(len(list_1)):
    for j in range(len(list_1) - 1):
        if list_1[j] > list_1[j + 1]:
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
print(list_1)