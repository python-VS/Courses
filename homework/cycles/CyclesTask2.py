a = input('Введите строку:')
b = input('Введите символ:')
indexes = [i for i in range(len(a)) if a[i] == b]
print(f"Символ {b} под индексами {a}")