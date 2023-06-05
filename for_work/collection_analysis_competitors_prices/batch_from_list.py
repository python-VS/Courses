import pandas as pd
from datetime import date
import numpy as np
import os

current_date = str(date.today().strftime('%Y-%m-%d'))  # определяем текущ дату ДД.ММ.ГГГГ

with open ('tm_list.txt', 'r', encoding='utf-8') as lt:  # открытие файла-списка необходимых брендов
    list_brands = [line.strip('\n') + '.xlsx' for line in lt]


def pars_data(x):
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
    ost2 = ost[(ost['Себестоимость\nединицы'] > 0) & (ost['Код склада'] == 'SHATE-S01')]
    ost3 = ost2[['Код\nтовара', 'Остаток', 'Себестоимость\nостатков']]  # выбор столбцов
    ost4 = ost3.rename(columns={"Код\nтовара": "Номер1", "Себестоимость\nостатков": "ССТ остатков"})  # переименование заголовков
    ost5 = ost4.pivot_table(index="Номер1", values=["Остаток", "ССТ остатков"], aggfunc="sum")  # сводная таблица
    ost5["Себест ед."] = ost5["ССТ остатков"] / ost5["Остаток"]  # добавление столбца для вывода сст за ед.
    ost_final = ost5

    # сбор в одну таблицу:

    res = data_final.merge(ost_final, how='left', left_on='Номер1', right_on='Номер1')
    res.drop(columns=['ССТ остатков'], axis=1, inplace=True, errors='raise')
    res['Остаток'] = res['Остаток'].fillna(0)  # заполение пустых ячеек 0
    res['Себест ед.'] = res['Себест ед.'].round(2).fillna(0.00)  # заполение пустых ячеек 0.00 + округление до 2х знаков после запятой
    res = res.merge(abc_2, how='left', left_on='Номер1', right_on='Номер1')

    res = res.assign(ТекМН=res['ОПТ РБ'] / res['Себест ед.'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца с расчетом МН + исправление Inf на пустоые при делении на 0

    res = res.merge(arm_1, how='left', left_on='Номер1', right_on='Номер1')
    res = res.assign(РазнШатАрм=res['ОПТ РБ'] / res['Цена\nАРМТЕК\nEUR'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца для определения разницы цен с Армтек + исправление Inf на пустоые при делении на 0
    res = res.merge(mot_1, how='left', left_on='Номер1', right_on='Номер1')
    res = res.assign(РазнШатМот=res['ОПТ РБ'] / res['Цена\nМОТЕХС\nEUR'] - 1).replace([-np.inf, np.inf], ['', ''])  # добавление столбца для определения разницы цен с Мотехс + исправление Inf на пустоые при делении на 0
    res = res.sort_values(by='Остаток', ascending=False)  # сортировка по убыванию по остаткам
    #res['MIN'] = res.apply(lambda x: minni(x['Цена\nАРМТЕК\nEUR'], x['Цена\nМОТЕХС\nEUR']), axis =  1)

    res.insert(17, 'MIN', '')  # добавление столбца с пустыми значениями (индекс столбца, заголовок, значения ячеек)
    res.insert(18, 'Разн\nс\nнаш_ОПТ', '')  # добавление столбца с пустыми значениями (индекс столбца, заголовок, значения ячеек)
    res.insert(19, 'МН\nпод\nMIN', '')  # добавление столбца с пустыми значениями (индекс столбца, заголовок, значения ячеек)
    res.insert(20, 'Нов\nОПТ', '')  # добавление столбца с пустыми значениями (индекс столбца, заголовок, значения ячеек)

    with pd.ExcelWriter(f'Анализ_{tm1}_{current_date}.xlsx', engine='xlsxwriter') as wb:
        res.to_excel(wb, sheet_name=f'анализ_{tm1}', freeze_panes=(1, 0), index=False)  # сохранение в файла
        sheet = wb.sheets[f'анализ_{tm1}']
        sheet.autofilter(0, 0, 0, 20)  # установка автофильтра (1я строка, 1й столб, посл строка, посл столб)
        sheet.set_tab_color('#FF9900')  # установка цвета вкладки листа
        sheet.set_row(0, 60)  # ширина строки (1я / 60пикс)
        sheet.autofit()  # автоподбор ширины столбцов

        # настройка общего формата текста
        cell_format = wb.book.add_format()
        cell_format.set_bold(False)  # стиль "полужирный"
        cell_format.set_font_color('black')  # цвет шрифта
        cell_format.set_font_size(9)  # размер шрифта

        # настройка формата текста
        cell_format_opt = wb.book.add_format()
        cell_format_opt.set_bold()  # стиль "полужирный"
        cell_format_opt.set_font_color('black')  # цвет шрифта
        cell_format_opt.set_bg_color('#00FF7F')  # цвет ячеек
        cell_format_opt.set_font_size(9)  # размер шрифта

        cell_format_cost = wb.book.add_format()
        cell_format_cost.set_bold()  # стиль "полужирный"
        cell_format_cost.set_font_color('black')  # цвет шрифта
        cell_format_cost.set_bg_color('#C0C0C0')  # цвет ячеек
        cell_format_cost.set_font_size(9)  # размер шрифта

        cell_format_perc = wb.book.add_format()
        cell_format_perc.set_num_format(9)

        sheet.set_column(0, 16, 10, cell_format) # Установка стиля для 20 первых столбов (1й столб, посл столб, ширина, формат)
        sheet.set_column(6, 6, 8, cell_format_opt) # Установка стиля для 7 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(10, 10, 8, cell_format_cost) # Установка стиля для 11 столба (1й столб, посл столб, ширина, формат)
        sheet.set_column(12, 12, 8, cell_format_perc)
        sheet.set_column(14, 14, 8, cell_format_perc)
        sheet.set_column(16, 16, 8, cell_format_perc)


    global tm_gl
    tm_gl = tm1


if __name__ == '__main__':
    try:
        for x in list_brands:
            pars_data(x)
        #os.startfile(f'Анализ_{tm_gl}_{current_date}.xlsx')
    except Exception as e:
        print(e)