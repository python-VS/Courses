# Дан список чисел.
# Отсортировать числа по убыванию по алгоритму Insertion Sort.
# Результаты вывести на экран.

from random import randint

list_1 = ([randint(1, 11) for i in range(10)])
print(list_1)

for i in range(1, len(list_1)):
    item = list_1[i]
    j = i - 1
    while j >= 0 and item < list_1[j]:
        list_1[j + 1] = list_1[j]
        j -= 1
    list_1[j + 1] = item
print('отсортированный список: ', list_1)