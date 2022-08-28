#Дан кортеж с температурой за несколько дней (каждый элемент – средняя температура за день).
# Посчитать среднюю температуру в течении всех дней.
# Результаты вывести на экран.

from random import randint

temper = tuple([randint(25, 32) for i in range(10)])
print(temper)
print(round(sum(temper) / len(temper), 2))