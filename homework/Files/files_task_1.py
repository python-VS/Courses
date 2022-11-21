# Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# - наименование товара;
# - количество товара (целое число);
# - цена (в рублях) товара за 1 шт. (целое число).
# Напишите программу, подсчитывающую общую стоимость заказа.


my_file = 'prices.txt'

def prices():
    with open(my_file, mode='r', encoding='UTF-8') as ff:
        data = ff.readlines()

    amount = 0
    for i in data:
        qty = int(i.split()[1])
        price = float(i.split()[-1])
        amount += qty * price
    return f'Сумма заказ: {amount}'

print(prices())
