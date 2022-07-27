from random import randint

list_1 = [randint(0, 10000) for _ in range(0, 10000)]
list_2 = [randint(0, 10000) for _ in range(0, 10000)]
print(sorted(list(set(list_1) & set(list_2))))
