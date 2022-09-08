# Дан список чисел. Вычислить сумму всех чисел: с for-циклом, с while-циклом.
# Результаты вывести на экран.

from random import randint

list_1 = [randint(1, 99) for i in range(10)]
sum_1 = 0

for x in list_1:
    sum_1 += x

print(f'Сумма через цикл "for" {sum_1}')


sum_2 = 0
a = 0

while a < len(list_1):
    sum_2 += list_1[a]
    a += 1
print(f'Сумма через цикл "while" {sum_2}')