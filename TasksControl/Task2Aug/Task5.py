dict_1 = {1: 'a', 2: 'b', 3: 'c'}
symb_1 = input('введите значение:')
values_all = list(dict_1.values())

for i in values_all:
    if i != symb_1:
        print('Такого значения в словаре нет!')

    else:
        print('Такое значение в словаре есть!')
        break
