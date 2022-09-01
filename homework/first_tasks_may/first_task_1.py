# Пользователь вводит сторону квадрата,
# необходимо рассчитать площадь квадрата, периметр и длину диагонали,
# после чего вывести это все на экран

side_sqr = input('Введите длину стороны квадрата: ')
side_sqr = int(side_sqr)
square = side_sqr ** 2
perimeter = side_sqr * 4
diagonal = side_sqr * (2 ** 0.5)

print('Сторона квадрата:', side_sqr)
print('Площадь квадрата: ', square)
print('Периметр квадрата: ', perimeter)
print('Диагональ квадрата: ', diagonal)