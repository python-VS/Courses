# Дана строка, содержащая натуральные числа и слова. Необходимо сформировать
# список из чисел, содержащихся в этой строке. Результаты вывести на экран.
# Например, задана строка "abc83 cde7 1 b 24". На выходе мы должны получить
# список [83, 7, 1, 24].

string_a = 'abc83 cde7 1 b 24'
string_with_spaces_and_nums = ''

for symbol in string_a:
    if not symbol.isdigit() and not symbol.isspace():
        string_with_spaces_and_nums += ' '
    else:
        string_with_spaces_and_nums += symbol

list_of_strings = string_with_spaces_and_nums.split(' ')

result_list = []
for i in list_of_strings:
    if i.isdigit():
        result_list.append(int(i))

print(f'Результирующий список {result_list}')