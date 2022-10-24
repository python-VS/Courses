# Напишите программу Python для отображения календаря для в заданной локали.
# (модуль calendar)

import calendar
import datetime


if __name__ == '__main__':
    now = datetime.datetime.now()
    _calendar = calendar.LocaleTextCalendar(firstweekday=1, locale='ru_RU.utf8',)
    _calendar.prmonth(now.year, now.month)
