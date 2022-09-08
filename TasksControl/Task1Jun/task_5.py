# Пользователь вводит число. Необходимо вычислить его факториал. Результаты
# вывести на экран.
# Математические подсказки: Формулу можно представить в таком виде:
# n! = 1 * … * (n-2) * (n-1) * n.

number = int(input('Введите число, пожалуйста: '))
factorial = 1
next_number = 1

while next_number <= number:
    factorial *= next_number
    next_number += 1

print('Факториал равен: ', factorial)