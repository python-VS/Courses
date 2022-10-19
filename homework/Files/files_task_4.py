# Напишите программу, которая получает на вход строку с названием текстового файла,
# и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками *
# (количество звездочек равно количеству букв в слове).
# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
# Все слова в этом файле записаны в нижнем регистре.
# Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова.
# Замена производится независимо от регистра:
# если файл forbidden_words.txt содержит запрещенное слово exam,
# то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

with open('forbidden_words.txt') as f:
    forbidden_words = {word: '*' * len(word) for word in f.read().split()}

with open(input()) as f:
    s = f.read()
    s_lower = s.lower()

for forbidden_word in forbidden_words:
    s_lower = s_lower.replace(forbidden_word, forbidden_words[forbidden_word])

print(*map((lambda c1, c2: '*' if c2 == '*' else c1), s, s_lower), sep='')
