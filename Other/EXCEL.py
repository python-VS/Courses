# Чтение ecxel-файла
import openpyxl # прикрутили модуль

book = openpyxl.open('FRECCIA_ДЕТАЛИ_ДВС.xlsx', read_only=True) # создали переменную, в нее открываем нужный файл

sheet = book.active

#print(sheet[1][0].value)

for row in range(sheet.max_column+1, sheet.max_row+1):
    pin = sheet[row][0].value
    description = sheet[row][1].value
    brand = sheet[row][5].value
    abc = sheet[row][6].value
    qty_sales = sheet[row][11].value
    print(pin, description, brand, abc, qty_sales)