# Дан список. Реализовать сортировку пузырьком. Результаты вывести на экран.

from random import randint

list_a = [randint(1, 55) for i in range(10)]
len_of_list = len(list_a)

swapped = False

for up_to_index in reversed(range(len_of_list - 1)):
    for index in range(0, up_to_index):
        next_index = index + 1
        if list_a[index] > list_a[next_index]:
            swapped = True
            list_a[index], list_a[next_index] = \
                list_a[next_index], list_a[index]

    if not swapped:
        break

print("Отсортированный по возрастанию список: ", list_a)