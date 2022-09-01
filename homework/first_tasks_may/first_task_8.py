# Пользователь вводит номер месяца (от 1 до 12),
# необходимо выяснить к какому времени года принадлежит месяц и вывести на экран.

month = int(input('Введите номер месяца: '))
fall, winter, spring, summer = [9, 10, 11], [12, 1, 2], [3, 4, 5], [6, 7, 8]

if month in winter:
    print('Месяц относится к зиме')
elif month in spring:
    print('Месяц относится к весне')
elif month in summer:
    print('Месяц относится к лету')
elif month in fall:
    print('Месяц относится к осени')
else:
    print('Это не номер месяца')