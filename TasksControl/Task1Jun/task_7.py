# Дан список. Проверить, все ли элементы в нем уникальные. Если найдены
# дубликаты, записать их в новый список. Результаты вывести на экран.

from random import randint

in_list = [randint(1, 10) for i in range(10)]
print(in_list)
duplicate_list = []

for i in in_list:
    if in_list.count(i) > 1 and i not in duplicate_list:
        duplicate_list.append(i)

print('Список дубликатов: ', duplicate_list)