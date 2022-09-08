# Пользователь вводит строку. В строке заменить пробелы звездочкой. Если
# встречается подряд несколько пробелов, то их следует заменить одним знаком
# "*", пробелы в начале и конце строки удалить. Результаты вывести на экран.

in_string = input('Пожалуйста, введите  строку: ')
striped_string = in_string.strip()

one_space_between_string = ''

for index in range(len(striped_string) - 1):
    if striped_string[index] == ' ' and striped_string[index + 1] == ' ':
        continue
    one_space_between_string += striped_string[index]

print(f"Результрующая строка : "
      f"{one_space_between_string.strip().replace(' ', '*')}")