# Пользователь вводит трехзначное число.
# Необходимо найти сумму цифр и вывести ее на экран.

number = int(input('Введите трехзначное число: '))
if 99 < number < 1000:
    units = number % 10  # выявляем единицы
    dozens = (number // 10) % 10  # выявляем десятки
    houndreth_place = number // 100  # выявляем сотки
    print('Сумма: ', units + dozens + houndreth_place)
else:
    print('Вы ввели не трехзначное число!!!')