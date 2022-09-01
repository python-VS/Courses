# Пользователь вводит длины двух катетов,
# необходимо найти длину гипотенузы и вывести ее на экран

from decimal import Decimal

katet_a = int(input("Введите длину Катета A: "))
katet_b = int(input("Введите длину Катета B: "))
hypot = (katet_a ** 2 + katet_b ** 2) ** 0.5
print('Длина гипотенузы: ', hypot)
