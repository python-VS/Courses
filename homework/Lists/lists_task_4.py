# Дан список.
# Необходимо вывести список в обратном порядке

import random

list_1 = [random.randint(1, 100) for i in range(10)]

print(sorted(list_1, reverse=True))