# Пользователь вводит строку и символ.
# Необходимо определить индексы первого и последнего вхождения символа в строке,
# при этом нельзя использовать строковые методы для поиска.


a = input('Введите строку:')
b = input('Введите символ:')
result = []
flag = False
n = 1

for i,element in enumerate(a):
    if flag:
        if n > len(b)-1:
            flag = False
            n = 1
        elif element == b[n]:
            n += 1
        elif element != b[n]:
            result = result[:-1]
            n = 1
            flag = False
    if element == b[0] and not flag:
        flag = True
        result.append(i)

for item in result:
    print('Вхождение на ' + str(item) + ' индексе')