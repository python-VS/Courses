# В файле записано стихотворение. Выведите его на экран, а также укажите, каких
# слов в нем больше: начинающихся на гласную или на согласную букву (регистр не
# учитывается)?

vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхчцшщ'

with open('input.txt', 'r') as f:
    text = f.read()

text = text.lower()
without_punctuation = ''
for symbol in text:
    if symbol.isalpha() or symbol.isspace():
        without_punctuation += symbol

words = without_punctuation.split()

result_vowel_amount, result_consonant_amount = 0, 0
for word in words:
    if word[0] in vowels:
        result_vowel_amount += 1
    elif word[0] in consonants:
        result_consonant_amount += 1
print(
    f'Всего слов: {len(words)}'
    f'\nвсего слов начинающихся на гласную: {result_vowel_amount}'
    f'\nвсего слов начинающихся на согласную: {result_consonant_amount}')