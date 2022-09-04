# создать словарь из строки 'pythonist' через:
# ключи - буквы строки, значения - числа кол-ва вхождений буквы в строку
# вывести на экран словарь

string_1 = 'pythonist'
list_1 = list(string_1)
dict_1 = dict.fromkeys(list_1, 3)

for key in dict_1:
    print(key)
print(dict_1)