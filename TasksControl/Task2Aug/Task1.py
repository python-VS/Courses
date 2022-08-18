# вывести на экран
# если хотя бы один элемент не целое число - вывести исх.кортеж


from random import randint

my_tuple = tuple([randint(1, 100) for _ in range(10)])
#my_tuple += ('a', 1.1,)
print(my_tuple)
for i in my_tuple:
    if type(i) != int:
        print("Обнаружено нецелое число", my_tuple)
        break
else:
    print('Отсортированный кортеж: ', sorted(my_tuple))