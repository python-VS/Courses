import csv
import xlsxwriter
import os

list_files = os.listdir()
print(list_files)
filename = "Автоматическое закрытие Цен продажи РАСПРОДАЖА.CSV"

rows = []
with open(filename, "r", encoding="windows-1251") as fh:
    reader = csv.DictReader(fh, delimiter=";")
    rows = list(reader)

new_rows = []
manager = input('Введите фамилию менеджера:')
for row in rows:
    if row.get('Менеджер РБ') == manager:
        new_rows.append([
            ''.join(list(filter(str.isdigit, row.get('Код товара')))),
            row.get('Код товара 2'),
            row.get('Торговая марка название'),
            row.get('Описание'),
            '',
            row.get('Менеджер РБ'),
            row.get('Логист РБ'),
        ])

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Код товара')
worksheet.write(0, 1, 'Код товара 2')
worksheet.write(0, 2, 'Торговая марка название')
worksheet.write(0, 3, 'Описание')
worksheet.write(0, 4, 'Примечания')
worksheet.write(0, 5, 'Менеджер РБ')
worksheet.write(0, 6, 'Логист РБ')

row = 1
col = 0

for new_row in new_rows:
    for col, item in enumerate(new_row):
        worksheet.write(row, col, item)
    row += 1

workbook.close()
input()