# Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python.
# Результаты выведите на экран.

dict_1 = {'a':300, 'b':400}
dict_2 = {'c':300, 'd':600}
print(dict_1.update(dict_2))
print(dict_1)