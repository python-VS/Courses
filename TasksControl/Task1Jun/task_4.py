# Квадратное уравнение имеет вид ax2 + bx + c = 0. Пользователь вводит a, b и c.
# Необходимо вычислить значение x. Результаты вывести на экран.
# Математические подсказки:
# сначала вычисляют дискриминант по формуле D = b2 - 4ac
# Если D > 0, то  x1 = (-b + D1/2 ) / (2a) и x2 = (-b - D1/2 ) / (2a)
# Если D = 0, то x = -b  / (2a)
# Если D < 0, то корней нет.

a = float(input('Введите, пожалуйста, a: '))
b = float(input('Введите, пожалуйста, b: '))
c = float(input('Введите, пожалуйста, c: '))

discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    print(f'x1 = {(-b + discriminant ** (1 / 2)) / (2 * a)}, '
          f'x2 = {(-b - discriminant ** (1 / 2))  / (2 * a)}')
elif discriminant == 0:
    print(f'У уравнения один корень {-b / (2 * a)}')
else:
    print('Корней нет!')