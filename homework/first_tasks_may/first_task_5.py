# Пользователь вводит количество секунд.
# Необходимо рассчитать сколько дней, часов, минут и секунд соответствуют данному количеству секунд
# и вывести в формате дни:часы:минуты:секунды.

seconds = int(input('Введите секунды: '))
days = seconds // (60 * 60 * 24)
hours = (seconds - days * (60 * 60 * 24)) // (60 * 60)
minutes = (seconds - days * (60 * 60 * 24) - hours * (60 * 60))

res_seconds = seconds - days
print('Результат: ' +str(days) + ':' + str(hours) + ':' + str(minutes) + ':' + str(seconds))