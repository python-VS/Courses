# Вводится 2 целых числа.
# Необходимо вывести их сумму.
# В случае, если одно или оба введенных параметра не являются целым числом, необходимо вывести конкатенацию введенных строк.
# Используйте механизм исключений.

try:
    num_1 = input('Введите число 1: ')
    num_2 = input('Введите число 2: ')
    res_sum = int(num_1) + int(num_2)
except (ValueError):
    print(num_1 + num_2)
else:
    print(res_sum)