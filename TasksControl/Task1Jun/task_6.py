# Даны два списка. Найти все элементы, которые находятся и в первом и во
# втором списке и записать их в третий список. Результаты вывести на экран.

from random import randint

list_1 = [randint(1, 10) for x in range(5)]
list_2 = [randint(1, 10) for y in range(5)]

intersection_list = []

for i in list_1:
    if i in list_2 and i not in intersection_list:
        intersection_list.append(i)

print('Результирующий список :', intersection_list)