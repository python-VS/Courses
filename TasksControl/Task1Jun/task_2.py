# Дано два списка, например, [1, 2, 3] и [11, 22, 33]. Необходимо создать
# третий список вида [1, 11, 2, 22, 3, 33]. Результаты вывести на экран.

from random import randint

list_a = [randint(1, 99) for i in range(3)]
list_b = [randint(1, 99) for i in range(3)]
print(list_a, list_b)

list_all = []

for x in range(len(list_b)):
    list_all.append(list_a[x])
    list_all.append(list_b[x])

print(f'Объединенный список: {list_all}')