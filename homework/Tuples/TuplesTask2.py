# пользователь вводит строку
# преобразовать строку к кортежу
# подсчитать частоту встречающихся букв в строке
# вывести на экран в формате "символ: количество вхождений"

string_1 = input('Введите текст: ')
list_1 = []
print(string_1)
for i in string_1:
    if i not in list_1 and i.isalpha():
        print('Символ: "' + i + '" количество вхождений: ' + str(string_1.count(i)))
        list_1.append(i)
print(tuple(list_1))
