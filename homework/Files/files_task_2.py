# Напишите программу, которая принимает поисковый запрос и выводит названия текстовых файлов,
# содержащих искомую подстроку.
# Все файлы располагаются в заданной директории.

import os


folder = os.getcwd()
answer = set()
search = input('Введите текст для поиска: ')
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    with open(filepath, 'r', encoding='utf-8') as fp:
        for line in fp:
            if search in line:
                answer.add(filename)

for i in answer:
    print(f'Текст найден в файле: {i}')