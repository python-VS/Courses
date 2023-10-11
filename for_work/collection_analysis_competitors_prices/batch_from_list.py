import pandas as pd
from datetime import date
import numpy as np
import os

current_date = str(date.today().strftime('%Y-%m-%d'))  # определяем текущ дату ДД.ММ.ГГГГ
brand = input("Введите бренд для анализа: ")
files = [i for i in os.listdir('.') if os.path.isfile(i)]  # список файлов в текущей папке

with open('tm_list.txt', 'r', encoding='utf-8') as lt:  # открытие файла-списка необходимых брендов
    list_brands = [line.strip('\n') + '.xlsx' for line in lt]

def pars_data_single():
    # dataFrame для данных:
    # открытие файла с нужными столбцами
    data_a = pd.read_excel(f'{brand}.xlsx', sheet_name="Данные о товарах по бренду", usecols=['No ', 'No 2', 'Description', 'Item Comment', 'Trade Mark Name', 'Manager', 'АССОРТ\nРБ', 'Unit\nPrice', 'Currency\nCode'])

    tm1 = data_a.iloc[2]['Trade Mark Name']  # вытягиваем бренд для использования

    data_b = data_a[data_a['АССОРТ\nРБ'] == 'ДА']  # фильтр по условию
    data_final = data_b.rename(columns={"No ": "Номер1", "No 2": "Номер2", "Description": "Описание", "Item Comment": "Примечание",
        "Trade Mark Name": "Бренд", "Manager": "ПМ", "Unit\nPrice": "ОПТ РБ", "Currency\nCode": "Валюта"})  # переименование заголовков
    data_final["Валюта"] = data_final["Валюта"].fillna('EUR')  # заполнение пустых ячеек валютой
    data_final["ОПТ РБ"] = pd.to_numeric(data_final["ОПТ РБ"])  # преобразование в числовой формат

    # dataFrame для ABC:
    abc_1 = pd.read_excel('ABC.xlsx', names=["Номер1", "1", "2", "3", "4", "ABC"])  # открытие файла с присвоением заголовков
    abc_2 = abc_1.iloc[:, [0,5]]  # оставляем 1 и 6 столбы

    # dataFrame для цен Армтек:
    arm_1 = pd.read_excel('arm.xlsx', sheet_name="Лист1", usecols=[3,72])  # открытие файла и забор 4 и 73 столбов
    arm_1.columns = ['Номер1', 'Цена\nАРМТЕК\nEUR']  # присвоение заголовков

    # dataFrame для цен Мотехс:
    mot_1 = pd.read_excel('mot.xlsx', sheet_name="Лист1", usecols=[3,72])  # открытие файла и забор 4 и 73 столбов
    mot_1.columns = ['Номер1', 'Цена\nМОТЕХС\nEUR']  # присвоение заголовков

    # dataFrame для себестоимости:
    ost = pd.read_excel('Остатки товаров по коду производителя.xlsx')  # открытие файла
    ost2 = ost[(ost['Себестоимость\nединицы'] > 0) & (ost['Код склада'] == 'SHATE-S01')]
    ost3 = ost2[['Код\nтовара', 'Остаток', 'Себестоимость\nостатков']]  # выбор столбцов
    ost4 = ost3.rename(columns={"Код\nтовара": "Номер1", "Себестоимость\nостатков": "ССТ остатков"})  # переименование заголовков
    ost5 = ost4.pivot_table(index="Номер1", values=["Остаток", "ССТ остатков"], aggfunc="sum")  # сводная таблица
    ost5["Себест ед."] = ost5["ССТ остатков"] / ost5["Остаток"]  # добавление столбца для вывода сст за ед.
    ost_final = ost5

    # dataFrame для продаж:
    sales_1 = pd.read_excel('КУБ_Продажи.xlsx', names=['TM', 'Номер1', 'Номер 2', 'Название', 'АССОРТ_РБ', '2018', '2019', '2020', '2021', '2022', '2023', 'Общий итог'])
    sales_2 = sales_1.iloc[:, [1,9,10]]

    # сбор в одну таблицу:
    res = data_final.merge(ost_final, how='left', left_on='Номер1', right_on='Номер1')
    res.drop(columns=['ССТ остатков'], axis=1, inplace=True, errors='raise')
    res['Остаток'] = res['Остаток'].fillna(0)  # заполение пустых ячеек 0
    res['Себест ед.'] = res['Себест ед.'].round(2).fillna(0.00)  # заполение пустых ячеек 0.00 + округление до 2х знаков после запятой
    res = res.merge(abc_2, how='left', left_on='Номер1', right_on='Номер1')

    res = res.assign(ТекМН=res['ОПТ РБ'] / res['Себест ед.'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН + исправление Inf на пустые при делении на 0

    res = res.merge(arm_1, how='left', left_on='Номер1', right_on='Номер1')  # добавление цен Армтек
    res = res.assign(РазнШатАрм=res['Цена\nАРМТЕК\nEUR'] / res['ОПТ РБ'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца для определения разницы цен с Армтек + исправление Inf на пустые при делении на 0
    res = res.merge(mot_1, how='left', left_on='Номер1', right_on='Номер1')  # добавление цен Мотехс
    res = res.assign(РазнШатМот=res['Цена\nМОТЕХС\nEUR'] / res['ОПТ РБ'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца для определения разницы цен с Мотехс + исправление Inf на пустые при делении на 0

    res = res.sort_values(by='Остаток', ascending=False)  # сортировка по убыванию по остаткам

    res['MIN\nЦена\nКонк'] = res[['Цена\nАРМТЕК\nEUR', 'Цена\nМОТЕХС\nEUR']].min(axis=1)  # добавляем столбец с минимальной ценой по всем конкурентам
    res = res.assign(РазнШатМИН=res['MIN\nЦена\nКонк'] / res['ОПТ РБ'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца для определения разницы цен с МИН КОНК + исправление Inf на пустые при делении на 0
    res = res.assign(МНподМИНконк=res['MIN\nЦена\nКонк'] / res['Себест ед.'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под МИН цены конк + исправление Inf на пустые при делении на 0

    res['Нов\nОПТ'] = res[['MIN\nЦена\nКонк', 'ОПТ РБ']].min(axis=1)  # добавление столбца с Новым ОПТ (минимальная из ТекущОпта и МинКонкурентов)
    res['Нов\nОПТ'] = pd.to_numeric(res["Нов\nОПТ"])  # преобразование в числовой формат

    res['Комментарии\nпо изменению ОПТ'] = ""  # добавление пустого столба для комментариев

    res = res.assign(Изменение=res['Нов\nОПТ'] / res['ОПТ РБ'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом разницы новый ОПТ/старый ОПТ + исправление Inf на пустые при делении на 0
    res = res.assign(НоваяМН=res['Нов\nОПТ'] / res['Себест ед.'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под новый ОПТ + исправление Inf на пустые при делении на 0

    res = res.merge(sales_2, how='left', left_on='Номер1', right_on='Номер1')  # добавляем столбцы с продажами
    res['2022'] = res['2022'].fillna(0)
    res['2023'] = res['2023'].fillna(0)
    res = res.assign(СуммаПродаж=res['2022'] + res['2023'])  #добавляем столб с суммой продаж 2022+2023

    res = res.assign(ТекМН_прод=(res['ОПТ РБ'] * res['СуммаПродаж']) / (res['Себест ед.'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под тек ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(БудМН_прод=(res['Нов\nОПТ'] * res['СуммаПродаж']) / (res['Себест ед.'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под нов ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(РазнТекАрмШат=(res['Цена\nАРМТЕК\nEUR'] * res['СуммаПродаж']) / (res['ОПТ РБ'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под тек ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(РазнБудАрмШат=(res['Цена\nАРМТЕК\nEUR'] * res['СуммаПродаж']) / (res['Нов\nОПТ'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под нов ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(РазнТекМотШат=(res['Цена\nМОТЕХС\nEUR'] * res['СуммаПродаж']) / (res['ОПТ РБ'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под тек ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(РазнБудМотШат=(res['Цена\nМОТЕХС\nEUR'] * res['СуммаПродаж']) / (res['Нов\nОПТ'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под нов ОПТ с учетом продаж + исправление Inf на пустые при делении на 0

    res = res.rename(columns={"РазнШатАрм": "Разн\nАрм/Шат", "РазнШатМот": "Разн\nМот/Шат", "РазнШатМИН": "Разн\nМИН/Шат", "МНподМИНконк": "МН\nпод\nМИН конк", "НоваяМН": "Новая\nМН", "СуммаПродаж": "Сумма\nПродаж"})  # переименование заголовков
    qty_rows = res.shape[0]

    with pd.ExcelWriter(f'Анализ_{tm1}_{current_date}.xlsx', engine='xlsxwriter') as wb:
        wb.book.set_properties({'author': 'Saharov', 'company': 'Shate-M Plus', 'comments': 'created with python'})
        res.to_excel(wb, sheet_name=f'анализ_{tm1}', freeze_panes=(2, 2), index=False, startrow=1)  # сохранение в файла [freeze_panes=(row, col), startrow(с какой строки сверху вставлять ДФ)
        sheet = wb.sheets[f'анализ_{tm1}']
        sheet.autofilter(1, 0, 1, 32)  # установка автофильтра (1я строка, 1й столб, посл строка, посл столб)
        sheet.set_tab_color('#FF9900')  # установка цвета вкладки листа
        sheet.set_row(1, 60)  # ширина строки (1я / 60пикс)
        sheet.autofit()  # автоподбор ширины столбцов

        sheet.write('M1', f'=SUBTOTAL(1,M3:M{qty_rows + 2})')
        sheet.write('O1', f'=SUBTOTAL(1,O3:O{qty_rows + 2})')
        sheet.write('Q1', f'=SUBTOTAL(1,Q3:Q{qty_rows + 2})')
        sheet.write('S1', f'=SUBTOTAL(1,S3:S{qty_rows + 2})')
        sheet.write('T1', f'=SUBTOTAL(1,T3:T{qty_rows + 2})')
        sheet.write('W1', f'=SUBTOTAL(1,W3:W{qty_rows + 2})')
        sheet.write('X1', f'=SUBTOTAL(1,X3:X{qty_rows + 2})')

        sheet.write('AB1', f'=SUBTOTAL(1,AB3:AB{qty_rows + 2})')
        sheet.write('AC1', f'=SUBTOTAL(1,AC3:AC{qty_rows + 2})')
        sheet.write('AD1', f'=SUBTOTAL(1,AD3:AD{qty_rows + 2})')
        sheet.write('AE1', f'=SUBTOTAL(1,AE3:AE{qty_rows + 2})')
        sheet.write('AF1', f'=SUBTOTAL(1,AF3:AF{qty_rows + 2})')
        sheet.write('AG1', f'=SUBTOTAL(1,AG3:AG{qty_rows + 2})')

        sheet.write('M3', '=IFERROR(G3/K3-1,"")')
        sheet.write('O3', '=IFERROR(IF(N3="","",N3/G3-1),"")')
        sheet.write('Q3', '=IFERROR(IF(P3="","",P3/G3-1),"")')
        sheet.write('R3', '=MIN(N3, P3)')
        sheet.write('S3', '=IFERROR(IF(R3=0,"",R3/G3-1),"")')
        sheet.write('T3', '=IFERROR(IF(R3=0,"",R3/K3-1),"")')
        sheet.write('W3', '=U3/G3-1')
        sheet.write('X3', '=IFERROR(U3/K3-1,"")')
        sheet.write('AB3', '=IFERROR((G3*AA3)/(K3*AA3)-1,"")')
        sheet.write('AC3', '=IFERROR((U3*AA3)/(K3*AA3)-1,"")')
        sheet.write('AD3', '=IFERROR(IF(N3="","",(N3*AA3)/(G3*AA3)-1),"")')
        sheet.write('AE3', '=IFERROR(IF(N3="","",(N3*AA3)/(U3*AA3)-1),"")')
        sheet.write('AF3', '=IFERROR(IF(P3="","",(P3*AA3)/(G3*AA3)-1),"")')
        sheet.write('AG3', '=IFERROR(IF(P3="","",(P3*AA3)/(U3*AA3)-1),"")')

        # настройка общего формата столбцов
        cell_format = wb.book.add_format({'bold': 0, 'font_color': 'black', 'bg_color': '#FFFFFF', 'font_name': 'Calibri', 'font_size': 8, 'border': 0})

        # настройка индивидуальных форматов столбцов
        cell_format_opt = wb.book.add_format({'bold': 0, 'font_color': 'black', 'bg_color': '#32CD32', 'font_size': 9})  # цвет ячеек салатовый
        cell_format_new_opt = wb.book.add_format({'bold': 1, 'font_color': 'black', 'bg_color': '#FFFF00', 'font_size': 9})  # цвет ячеек желтый
        cell_format_cost = wb.book.add_format({'bold': 0, 'font_color': 'black', 'bg_color': '#C0C0C0', 'font_size': 9})  # цвет ячеек серый
        cell_format_perc = wb.book.add_format({"num_format": "0.0%", 'border': 0, 'font_size': 8})
        cell_format_min = wb.book.add_format({'bold': 1, 'font_color': 'black', 'bg_color': '#1E90FF', 'font_size': 9})  # цвет ячеек голубой

        cell_format_condit1 = wb.book.add_format({'bold': 0, 'italic': 0, 'bg_color': '#FFA07A', 'border': 0})  # шаблон условного форматирования (красный цвет ячейки)
        cell_format_condit2 = wb.book.add_format({'bold': 0, 'italic': 0, 'bg_color': '#00FF00', 'border': 0})  # шаблон условного форматирования (зеленый цвет ячейки)
        cell_format_condit3 = wb.book.add_format({'bold': 0, 'italic': 0, 'bg_color': '#FFFFFF', 'border': 0})  # шаблон условного форматирования (белый цвет ячейки)
        merge_format = wb.book.add_format({'bold': True, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#9370DB', 'font_size': 10})

        sheet.set_column(0, 32, 10, cell_format) # Установка стиля для 20 первых столбов (1й столб, посл столб, ширина, формат)
        sheet.set_column(6, 6, 8, cell_format_opt) # Установка стиля для 7 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(10, 10, 8, cell_format_cost) # Установка стиля для 11 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(20, 20, 8, cell_format_new_opt) # Установка стиля для 11 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(17, 17, 8, cell_format_min) # Установка стиля для 18 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(12, 12, 8, cell_format_perc)
        sheet.set_column(14, 14, 8, cell_format_perc)
        sheet.set_column(16, 16, 8, cell_format_perc)
        sheet.set_column(18, 19, 8, cell_format_perc)
        sheet.set_column(22, 23, 8, cell_format_perc)
        sheet.set_column(27, 32, 8, cell_format_perc)
        sheet.merge_range('Y1:AA1','Продажи', merge_format)

        sheet.conditional_format('O2:O5000', {'type': 'cell', 'criteria': '<', 'value': 0, 'format': cell_format_condit1})  # условное форматирование столба O "если меньше 0, то красный цвет"
        sheet.conditional_format('O2:O5000', {'type': 'cell', 'criteria': '>', 'value': 0, 'format': cell_format_condit2})  # условное форматирование столба O "если больше 0, то зеленый цвет"
        sheet.conditional_format('O2:O5000', {'type': 'blanks', 'format': cell_format_condit3})  # условное форматирование столба O "если пусто, то белый цвет"

        sheet.conditional_format('Q2:Q5000', {'type': 'cell', 'criteria': '<', 'value': 0, 'format': cell_format_condit1})  # условное форматирование столба Q "если меньше 0, то красный цвет"
        sheet.conditional_format('Q2:Q5000', {'type': 'cell', 'criteria': '>', 'value': 0, 'format': cell_format_condit2})  # условное форматирование столба Q "если больше 0, то зеленый цвет"
        sheet.conditional_format('Q2:Q5000', {'type': 'blanks', 'format': cell_format_condit3})  # условное форматирование столба Q "если пусто, то белый цвет"

        sheet.conditional_format('S2:S5000', {'type': 'cell', 'criteria': '<', 'value': 0, 'format': cell_format_condit1})  # условное форматирование столба S "если меньше 0, то красный цвет"
        sheet.conditional_format('S2:S5000', {'type': 'cell', 'criteria': '>', 'value': 0, 'format': cell_format_condit2})  # условное форматирование столба S "если больше 0, то зеленый цвет"
        sheet.conditional_format('S2:S5000', {'type': 'blanks', 'format': cell_format_condit3})  # условное форматирование столба Q "если пусто, то белый цвет"


    global tm_gl
    tm_gl = tm1


def pars_data_gr(x):
    # dataFrame для данных:
    # открытие файла с нужными столбцами
    data_a = pd.read_excel(x, sheet_name="Данные о товарах по бренду", usecols=['No ', 'No 2', 'Description', 'Item Comment', 'Trade Mark Name', 'Manager', 'АССОРТ\nРБ', 'Unit\nPrice', 'Currency\nCode'])

    tm1 = data_a.iloc[2]['Trade Mark Name']  # вытягиваем бренд для использования

    data_b = data_a[data_a['АССОРТ\nРБ'] == 'ДА']  # фильтр по условию
    data_final = data_b.rename(columns={"No ": "Номер1", "No 2": "Номер2", "Description": "Описание", "Item Comment": "Примечание",
        "Trade Mark Name": "Бренд", "Manager": "ПМ", "Unit\nPrice": "ОПТ РБ", "Currency\nCode": "Валюта"})  # переименование заголовков
    data_final["Валюта"] = data_final["Валюта"].fillna('EUR')
    data_final["ОПТ РБ"] = pd.to_numeric(data_final["ОПТ РБ"])

    # dataFrame для ABC:
    abc_1 = pd.read_excel('ABC.xlsx', names=["Номер1", "1", "2", "3", "4", "ABC"])  # открытие файла с присвоением заголовков
    abc_2 = abc_1.iloc[:, [0,5]]  # оставляем 1 и 6 столбы

    # dataFrame для цен Армтек:
    arm_1 = pd.read_excel('arm.xlsx', sheet_name="Лист1", usecols=[3,72])  # открытие файла и забор 4 и 73 столбов
    arm_1.columns = ['Номер1', 'Цена\nАРМТЕК\nEUR']  # присвоение заголовков

    # dataFrame для цен Мотехс:
    mot_1 = pd.read_excel('mot.xlsx', sheet_name="Лист1", usecols=[3,72])  # открытие файла и забор 4 и 73 столбов
    mot_1.columns = ['Номер1', 'Цена\nМОТЕХС\nEUR']  # присвоение заголовков

    # dataFrame для себестоимости:
    ost = pd.read_excel('Остатки товаров по коду производителя.xlsx')  # открытие файла
    ost2 = ost[(ost['Себестоимость\nединицы'] > 0) & (ost['Код склада'] == 'SHATE-S01')]   # фильтр по 2 условиям
    ost3 = ost2[['Код\nтовара', 'Остаток', 'Себестоимость\nостатков']]  # выбор столбцов
    ost4 = ost3.rename(columns={"Код\nтовара": "Номер1", "Себестоимость\nостатков": "ССТ остатков"})  # переименование заголовков
    ost5 = ost4.pivot_table(index="Номер1", values=["Остаток", "ССТ остатков"], aggfunc="sum")  # сводная таблица
    ost5["Себест ед."] = ost5["ССТ остатков"] / ost5["Остаток"]  # добавление столбца для вывода сст за ед.
    ost_final = ost5

    # dataFrame для продаж:
    sales_1 = pd.read_excel('КУБ_Продажи.xlsx', names=['TM', 'Номер1', 'Номер 2', 'Название', 'АССОРТ_РБ', '2018', '2019', '2020', '2021', '2022', '2023', 'Общий итог'])
    sales_2 = sales_1.iloc[:, [1,9,10]]

    # сбор в одну таблицу:
    res = data_final.merge(ost_final, how='left', left_on='Номер1', right_on='Номер1')
    res.drop(columns=['ССТ остатков'], axis=1, inplace=True, errors='raise')
    res['Остаток'] = res['Остаток'].fillna(0)  # заполение пустых ячеек 0
    res['Себест ед.'] = res['Себест ед.'].round(2).fillna(0.00)  # заполение пустых ячеек 0.00 + округление до 2х знаков после запятой
    res = res.merge(abc_2, how='left', left_on='Номер1', right_on='Номер1')

    res = res.assign(ТекМН=res['ОПТ РБ'] / res['Себест ед.'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН + исправление Inf на пустые при делении на 0

    res = res.merge(arm_1, how='left', left_on='Номер1', right_on='Номер1')  # добавление цен Армтек
    res = res.assign(РазнШатАрм=res['Цена\nАРМТЕК\nEUR'] / res['ОПТ РБ'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца для определения разницы цен с Армтек + исправление Inf на пустые при делении на 0
    res = res.merge(mot_1, how='left', left_on='Номер1', right_on='Номер1')  # добавление цен Мотехс
    res = res.assign(РазнШатМот=res['Цена\nМОТЕХС\nEUR'] / res['ОПТ РБ'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца для определения разницы цен с Мотехс + исправление Inf на пустые при делении на 0

    res = res.sort_values(by='Остаток', ascending=False)  # сортировка по убыванию по остаткам

    res['MIN\nЦена\nКонк'] = res[['Цена\nАРМТЕК\nEUR', 'Цена\nМОТЕХС\nEUR']].min(axis=1)  # добавляем столбец с минимальной ценой по всем конкурентам
    res = res.assign(РазнШатМИН=res['MIN\nЦена\nКонк'] / res['ОПТ РБ'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца для определения разницы цен с МИН КОНК + исправление Inf на пустые при делении на 0
    res = res.assign(МНподМИНконк=res['MIN\nЦена\nКонк'] / res['Себест ед.'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под МИН цены конк + исправление Inf на пустые при делении на 0

    res['Нов\nОПТ'] = res[['MIN\nЦена\nКонк', 'ОПТ РБ']].min(axis=1)  # добавление столбца с Новым ОПТ (минимальная из ТекущОпта и МинКонкурентов)
    res['Нов\nОПТ'] = pd.to_numeric(res["Нов\nОПТ"])  # преобразование в числовой формат

    res['Комментарии\nпо изменению ОПТ'] = ""  # добавление пустого столба для комментариев

    res = res.assign(Изменение=res['Нов\nОПТ'] / res['ОПТ РБ'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом разницы новый ОПТ/старый ОПТ + исправление Inf на пустые при делении на 0
    res = res.assign(НоваяМН=res['Нов\nОПТ'] / res['Себест ед.'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под новый ОПТ + исправление Inf на пустые при делении на 0

    res = res.merge(sales_2, how='left', left_on='Номер1', right_on='Номер1')  # добавляем столбцы с продажами
    res['2022'] = res['2022'].fillna(0)
    res['2023'] = res['2023'].fillna(0)
    res = res.assign(СуммаПродаж=res['2022'] + res['2023'])  #добавляем столб с суммой продаж 2022+2023

    res = res.assign(ТекМН_прод=(res['ОПТ РБ'] * res['СуммаПродаж']) / (res['Себест ед.'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под тек ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(БудМН_прод=(res['Нов\nОПТ'] * res['СуммаПродаж']) / (res['Себест ед.'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под нов ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(РазнТекАрмШат=(res['Цена\nАРМТЕК\nEUR'] * res['СуммаПродаж']) / (res['ОПТ РБ'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под тек ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(РазнБудАрмШат=(res['Цена\nАРМТЕК\nEUR'] * res['СуммаПродаж']) / (res['Нов\nОПТ'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под нов ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(РазнТекМотШат=(res['Цена\nМОТЕХС\nEUR'] * res['СуммаПродаж']) / (res['ОПТ РБ'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под тек ОПТ с учетом продаж + исправление Inf на пустые при делении на 0
    res = res.assign(РазнБудМотШат=(res['Цена\nМОТЕХС\nEUR'] * res['СуммаПродаж']) / (res['Нов\nОПТ'] * res['СуммаПродаж']) - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН под нов ОПТ с учетом продаж + исправление Inf на пустые при делении на 0

    res = res.rename(columns={"РазнШатАрм": "Разн\nАрм/Шат", "РазнШатМот": "Разн\nМот/Шат", "РазнШатМИН": "Разн\nМИН/Шат", "МНподМИНконк": "МН\nпод\nМИН конк", "НоваяМН": "Новая\nМН", "СуммаПродаж": "Сумма\nПродаж"})  # переименование заголовков
    qty_rows = res.shape[0]

    with pd.ExcelWriter(f'Анализ_{tm1}_{current_date}.xlsx', engine='xlsxwriter') as wb:
        wb.book.set_properties({'author': 'Saharov', 'company': 'Shate-M Plus', 'comments': 'created with python'})
        res.to_excel(wb, sheet_name=f'анализ_{tm1}', freeze_panes=(2, 2), index=False, startrow=1)  # сохранение в файла [freeze_panes=(row, col), startrow(с какой строки сверху вставлять ДФ)
        sheet = wb.sheets[f'анализ_{tm1}']
        sheet.autofilter(1, 0, 1, 32)  # установка автофильтра (1я строка, 1й столб, посл строка, посл столб)
        sheet.set_tab_color('#FF9900')  # установка цвета вкладки листа
        sheet.set_row(1, 60)  # ширина строки (1я / 60пикс)
        sheet.autofit()  # автоподбор ширины столбцов

        sheet.write('M1', f'=SUBTOTAL(1,M3:M{qty_rows + 2})')
        sheet.write('O1', f'=SUBTOTAL(1,O3:O{qty_rows + 2})')
        sheet.write('Q1', f'=SUBTOTAL(1,Q3:Q{qty_rows + 2})')
        sheet.write('S1', f'=SUBTOTAL(1,S3:S{qty_rows + 2})')
        sheet.write('T1', f'=SUBTOTAL(1,T3:T{qty_rows + 2})')
        sheet.write('W1', f'=SUBTOTAL(1,W3:W{qty_rows + 2})')
        sheet.write('X1', f'=SUBTOTAL(1,X3:X{qty_rows + 2})')

        sheet.write('AB1', f'=SUBTOTAL(1,AB3:AB{qty_rows + 2})')
        sheet.write('AC1', f'=SUBTOTAL(1,AC3:AC{qty_rows + 2})')
        sheet.write('AD1', f'=SUBTOTAL(1,AD3:AD{qty_rows + 2})')
        sheet.write('AE1', f'=SUBTOTAL(1,AE3:AE{qty_rows + 2})')
        sheet.write('AF1', f'=SUBTOTAL(1,AF3:AF{qty_rows + 2})')
        sheet.write('AG1', f'=SUBTOTAL(1,AG3:AG{qty_rows + 2})')

        sheet.write('M3', '=IFERROR(G3/K3-1,"")')
        sheet.write('O3', '=IFERROR(IF(N3="","",N3/G3-1),"")')
        sheet.write('Q3', '=IFERROR(IF(P3="","",P3/G3-1),"")')
        sheet.write('R3', '=MIN(N3, P3)')
        sheet.write('S3', '=IFERROR(IF(R3=0,"",R3/G3-1),"")')
        sheet.write('T3', '=IFERROR(IF(R3=0,"",R3/K3-1),"")')
        sheet.write('W3', '=U3/G3-1')
        sheet.write('X3', '=IFERROR(U3/K3-1,"")')
        sheet.write('AB3', '=IFERROR((G3*AA3)/(K3*AA3)-1,"")')
        sheet.write('AC3', '=IFERROR((U3*AA3)/(K3*AA3)-1,"")')
        sheet.write('AD3', '=IFERROR(IF(N3="","",(N3*AA3)/(G3*AA3)-1),"")')
        sheet.write('AE3', '=IFERROR(IF(N3="","",(N3*AA3)/(U3*AA3)-1),"")')
        sheet.write('AF3', '=IFERROR(IF(P3="","",(P3*AA3)/(G3*AA3)-1),"")')
        sheet.write('AG3', '=IFERROR(IF(P3="","",(P3*AA3)/(U3*AA3)-1),"")')

        # настройка общего формата столбцов
        cell_format = wb.book.add_format({'bold': 0, 'font_color': 'black', 'bg_color': '#FFFFFF', 'font_name': 'Calibri', 'font_size': 8, 'border': 0})

        # настройка индивидуальных форматов столбцов
        cell_format_opt = wb.book.add_format({'bold': 0, 'font_color': 'black', 'bg_color': '#32CD32', 'font_size': 9})  # цвет ячеек салатовый
        cell_format_new_opt = wb.book.add_format({'bold': 1, 'font_color': 'black', 'bg_color': '#FFFF00', 'font_size': 9})  # цвет ячеек желтый
        cell_format_cost = wb.book.add_format({'bold': 0, 'font_color': 'black', 'bg_color': '#C0C0C0', 'font_size': 9})  # цвет ячеек серый
        cell_format_perc = wb.book.add_format({"num_format": "0.0%", 'border': 0, 'font_size': 8})
        cell_format_min = wb.book.add_format({'bold': 1, 'font_color': 'black', 'bg_color': '#1E90FF', 'font_size': 9})  # цвет ячеек голубой

        cell_format_condit1 = wb.book.add_format({'bold': 0, 'italic': 0, 'bg_color': '#FFA07A', 'border': 0})  # шаблон условного форматирования (красный цвет ячейки)
        cell_format_condit2 = wb.book.add_format({'bold': 0, 'italic': 0, 'bg_color': '#00FF00', 'border': 0})  # шаблон условного форматирования (зеленый цвет ячейки)
        cell_format_condit3 = wb.book.add_format({'bold': 0, 'italic': 0, 'bg_color': '#FFFFFF', 'border': 0})  # шаблон условного форматирования (белый цвет ячейки)
        merge_format = wb.book.add_format({'bold': True, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#9370DB', 'font_size': 10})

        sheet.set_column(0, 32, 10, cell_format) # Установка стиля для 20 первых столбов (1й столб, посл столб, ширина, формат)
        sheet.set_column(6, 6, 8, cell_format_opt) # Установка стиля для 7 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(10, 10, 8, cell_format_cost) # Установка стиля для 11 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(20, 20, 8, cell_format_new_opt) # Установка стиля для 11 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(17, 17, 8, cell_format_min) # Установка стиля для 18 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(12, 12, 8, cell_format_perc)
        sheet.set_column(14, 14, 8, cell_format_perc)
        sheet.set_column(16, 16, 8, cell_format_perc)
        sheet.set_column(18, 19, 8, cell_format_perc)
        sheet.set_column(22, 23, 8, cell_format_perc)
        sheet.set_column(27, 32, 8, cell_format_perc)
        sheet.merge_range('Y1:AA1','Продажи', merge_format)

        sheet.conditional_format('O2:O5000', {'type': 'cell', 'criteria': '<', 'value': 0, 'format': cell_format_condit1})  # условное форматирование столба O "если меньше 0, то красный цвет"
        sheet.conditional_format('O2:O5000', {'type': 'cell', 'criteria': '>', 'value': 0, 'format': cell_format_condit2})  # условное форматирование столба O "если больше 0, то зеленый цвет"
        sheet.conditional_format('O2:O5000', {'type': 'blanks', 'format': cell_format_condit3})  # условное форматирование столба O "если пусто, то белый цвет"

        sheet.conditional_format('Q2:Q5000', {'type': 'cell', 'criteria': '<', 'value': 0, 'format': cell_format_condit1})  # условное форматирование столба Q "если меньше 0, то красный цвет"
        sheet.conditional_format('Q2:Q5000', {'type': 'cell', 'criteria': '>', 'value': 0, 'format': cell_format_condit2})  # условное форматирование столба Q "если больше 0, то зеленый цвет"
        sheet.conditional_format('Q2:Q5000', {'type': 'blanks', 'format': cell_format_condit3})  # условное форматирование столба Q "если пусто, то белый цвет"

        sheet.conditional_format('S2:S5000', {'type': 'cell', 'criteria': '<', 'value': 0, 'format': cell_format_condit1})  # условное форматирование столба S "если меньше 0, то красный цвет"
        sheet.conditional_format('S2:S5000', {'type': 'cell', 'criteria': '>', 'value': 0, 'format': cell_format_condit2})  # условное форматирование столба S "если больше 0, то зеленый цвет"
        sheet.conditional_format('S2:S5000', {'type': 'blanks', 'format': cell_format_condit3})  # условное форматирование столба Q "если пусто, то белый цвет"


        global tm_gl
        tm_gl = tm1


if __name__ == '__main__':
    if brand == '':
        try:
            for x in list_brands:
                pars_data_gr(x)
        except Exception as e:
           print(e)
    else:
        try:
            pars_data_single()
            os.startfile(f'Анализ_{tm_gl}_{current_date}.xlsx')
        except Exception as e:
            print(e)
