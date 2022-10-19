# Имеется файл file.txt с текстом на латинице.
# Напишите программу, которая выводит следующую статистику по тексту:
# - количество букв латинского алфавита;
# - число слов;
# - число строк

my_file = 'file.txt'
fn = open(my_file, "r", encoding="utf-8")
data = fn.read()
letters = len([i for i in data if i.isalpha()])
words = len(data.split())
lines = data.count('\n') + 1

print(f'Текст содержит: {lines} строк, {words} слов и {letters} букв')