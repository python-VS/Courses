#Написать калькулятор.
# Пользователь вводит два числа и оператор.
# Необходимо вычислить результат операции и вывести на экран.
# Операторы, которые должен “знать” калькулятор: +, -, /, *, **, %, //.

number_1 = float(input('введите 1е число: '))
symbol = input('Введите тип операции (символ): ')
number_2 = float(input('Введите 2е число: '))

if symbol == '+':
    result = number_1 + number_2
    print('Результат: ' + str(result))
elif symbol == '-':
    result = number_1 - number_2
    print('Результат: ' + str(result))
elif symbol == '/':
    result = number_1 / number_2
    print('Результат: ' + str(result))
elif symbol == '*':
    result = number_1 * number_2
    print('Результат: ' + str(result))
elif symbol == '**':
    result = number_1 ** number_2
    print('Результат: ' + str(result))
elif symbol == '%':
    result = number_1 % number_2
    print('Результат: ' + str(result))
elif symbol == '//':
    result = number_1 // number_2
    print('Результат: ' + str(result))
else:
    print('Невозможно выполнить операцию!')