#Даны два кортежа.
# Найти элементы, которые содержаться и в первом и во втором кортеже и вывести на экран.

from random import randint

tuple_1 = tuple((randint(1, 20) for _ in range(10)))
tuple_2 = tuple((randint(1, 20) for _ in range(10)))
list_1 = []

for x in tuple_1:
    if x in list_1:
        continue
    for y in tuple_2:
        if x == y:
            list_1.append(x)
            break

print(tuple_1)
print(tuple_2)
print('Пересечения: ', tuple(list_1))