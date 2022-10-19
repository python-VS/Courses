# С клавиатуры в одной строке вводится произвольное количество вещественных
# чисел. Запишите их в файл, расположив каждое число на отдельной строке.

while True:
    try:
        input_floats = list(map(float, input().split()))
    except ValueError:
        print('Введите снова')
    else:
        break

with open('output.txt', 'w') as file:
    for _float in input_floats:
        file.write(str(_float) + '\n')
