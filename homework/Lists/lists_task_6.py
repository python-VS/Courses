# Дан список.
# Необходимо определить, есть ли в списке повторяющиеся элементы,
# если да, то вывести на экран это значение

list_1 = [1, 2, 3, 'a', 4, 1, 6, 'a']
result = [i for i in set(list_1) if list_1.count(i) > 1]
print(result)