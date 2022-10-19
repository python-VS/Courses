# Напишите функцию, чтобы проверить, является ли строка панграммой или нет.
# Панграмма — фраза, содержащая в себе все буквы алфавита.

def pangram_check(s):
    p = set('abcdefghijklmnopqrstuvwxyz') == set(s.lower().replace(' ', ''))
    if p == True:
        print("Строка является панаграммой")
    else:
        print("Строка не является панаграммой")

a = input("Введите текст: ")

pangram_check(a)