# Напишите программу, которая содержит функцию calculation(),
# которая принимает два параметра и вычисляет сумму и разность.
# Кроме того, данная функция сразу должна возвращать и сумму и разность.
# Результат вывести на экран.

from random import randint

def calculation(x, y):
    return x + y, x - y

a = randint(1, 10)
b = randint(1, 10)

print(calculation(a, b))

