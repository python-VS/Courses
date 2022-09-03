# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

from random import randint

list_1 = [randint(0, 10) for _ in range(0, 10)]
list_2 = [randint(0, 10) for _ in range(0, 10)]

print(list_1)
print(list_2)
print(sorted(list(set(list_1) & set(list_2))))
