# Напишите генератор custom_ange(start, end, step),
# который генерирует все целые числа от значения «start» до величины «end» включительно с шагом «step».
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
# «step» по умолчанию равен = 1.
# Также не допускать ввод дробных чисел

def input_int(welcome_string: str) -> int:
    while True:
        try:
            number = int(input(welcome_string))
        except ValueError:
            print('Вы ввели не целое число.')
        else:
            return number


def custom_range(_start: int, _end: int, _step: int = 1):
    # _start, _end = (_start, _end) if _start <= _end else (_end, _start)
    if _start > _end:
        _start, _end = _end, _start

    # _item = _start
    # while _item < _end:
    #     yield _item
    #     _item += _step

    for i in range(_start, _end + 1, _step):
        yield i

    # yield from range(_start, _end + 1, _step)


start = input_int('Введите, пожалуйста, значение start: ')
end = input_int('Введите, пожалуйста, значение end: ')
step = input_int('Введите, пожалуйста, значение step: ')

new_range = custom_range(start, end, step)
for item in new_range:
    print(item)