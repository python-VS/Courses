# Дан список чисел,
# необходимо удалить все вхождения числа 20 из него.
# Результаты вывести на экран.

list_1 = [1, 20, 3, 20, 6, 5, 20]
print([i for i in list_1 if i != 20])