# Пользователь вводит два числа: делимое и делитель.
# Вам необходимо найти целое и остаток от деления, не используя операторы % и //,
# и вывести их на экран.
# (Результаты должны быть такие, как при использовании % и //)

a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))

print('Результат целое: ', a // b)
print('Результат остаток: ', a % b)