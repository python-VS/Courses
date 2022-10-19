# Напишите функцию sum_range(start, end),
# которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sum_range(start, end):
    if start > end:
        x = [i for i in range(end, start+1)]
    else:
        x = [i for i in range(start, end+1)]
    print(sum(x))

a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

sum_range(a, b)
