from io import BytesIO
from PIL import Image, ImageTk
import requests
import re
from tkinter import Tk, ttk, END, filedialog, PhotoImage, Canvas, messagebox


def receiving_foto_info():
    global in_text_content
    in_text_content = in_text.get().rstrip().lstrip()
    label2.configure(text='Загрузка изображения...')

    for item1 in tree.get_children():  # чистка данных таблицы
        tree.delete(item1)

    for item2 in tree_.get_children():  # чистка данных таблицы
        tree_.delete(item2)

    root.update()

    global url_pic
    url_pic = f'https://store.bgautomotive.co.uk/Images/ProductImages/{in_text_content.rstrip().lstrip()}.jpg'

    try:
        response = requests.get(url_pic, timeout=10)
    except requests.exceptions.Timeout:
        label2.configure(text='Ошибка времени ожидания')
    else:
        if response.status_code != 200:
            label2.configure(text=f'HTTP ошибка {response.status_code}')
        else:
            pil_image = Image.open(BytesIO(response.content))
            image = ImageTk.PhotoImage(pil_image)
            label2.configure(image=image, text='')
            label2.image = image

    url_data = f'https://store.bgautomotive.co.uk/Product/GetProductList/?searchText=~~~~~{in_text_content.rstrip().lstrip()}~True~~'
    req = requests.get(url_data)

    _json = req.json()
    list_ = _json["productList"]

    pattern1 = r"\(\w.{0,50}$|( Saloon )|( Hatchback )|( Van )|(Estate Front-Wheel Drive)|(Estate)|(Station Wagon)"
    pattern2 = r"^19|^20"
    vehicles = []

    for i in list_:
        a = i["manufacturer"], i["modelSeries"], i["engineSize"], i["fuelType"], i["modelYearFrom"], i["modelYearTo"], i["engineCodes"]
        vehicles.append(a)

    vehicles.sort()
    # добавляем данные
    for car in vehicles:
        tree.insert("", END, values=car)

    url_det = f'https://store.bgautomotive.co.uk/Product/GetProductDetails/?productCode={in_text_content.rstrip().lstrip()}'
    req_ = requests.get(url_det)

    _json_ = req_.json()
    _list_ = _json_["productExtendedDetails"]

    data_ = []

    for t in _list_:
        u = t["attribute"], t["attributeValue"]
        data_.append(u)

    for it in data_:
        tree_.insert("", END, values=it)

def sort_col_tree(col, reverse):
    l = [(tree.set(k, col), k) for k in tree.get_children("")]  # получаем все значения столбцов в виде отдельного списка
    l.sort(reverse=reverse)  # сортируем список
    for index,  (_, k) in enumerate(l):  # переупорядочиваем значения в отсортированном порядке
        tree.move(k, "", index)
    tree.heading(col, command=lambda: sort_col_tree(col, not reverse))  # в следующий раз выполняем сортировку в обратном порядке

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=(("Image files", "*.jpg"), ("All files", "*.*")), initialfile=f'{in_text_content}.jpg')
    if filepath != "":
        img = requests.get(url_pic)
        with open(filepath, "wb") as file:
            file.write(img.content)

def open_list():
    filepath_open = filedialog.askopenfilename(title="Выбор файла", filetypes=(('Все форматы', '*'), ('Текст', '*.txt')))
    with open(filepath_open, 'r', encoding='utf-8') as lst:  # открытие файла-списка необходимых брендов
        global list_ref
        list_ref = [line.strip('\n') for line in lst]

def save_files():
    url_pict = 'https://store.bgautomotive.co.uk/Images/ProductImages/'  # +артикул.jpg
    file_path_gr = filedialog.askdirectory()
    for x in list_ref:
        i = str(url_pict + x + '.jpg')
        try:
            response2 = requests.get(i, timeout=10)
        except requests.exceptions.Timeout:
            label2.configure(text='Ошибка времени ожидания')
        else:
            if response2.status_code != 200:
                label2.configure(text=f'HTTP ошибка {response2.status_code}')
                continue
        with open(file_path_gr + '/' + x +'.jpg', "wb") as file_:
            file_.write(response2.content)
    messagebox.showinfo(title='Информация', message='Скачивание завершено!')

#---------------------------------------------------------------------------------------------------------#
root = Tk()
root.title('Download BGA images')
root.geometry("1260x750+400+130")  # ширина х высота + позиция х\у
root.resizable(False, True)  # растягивание границ окна
root.iconbitmap(default="bga_logo.ico")
root.config(cursor="arrow")
root.event_add('<<Paste>>', '<Control-igrave>')
root.event_add('<<Copy>>', '<Control-ntilde>')
#---------------------------------------------------------------------------------------------------------#
frame1 = ttk.Frame(root, border=1, height=300, width=250)

label1 = ttk.Label(frame1, text='Введите артикул BGA:')
label1.pack()
in_text = ttk.Entry(frame1, width=20)
in_text.pack()
btn1 = ttk.Button(frame1, text='Загрузить', command=receiving_foto_info)
btn1.pack()
btn2 = ttk.Button(frame1, text='Сохранить', command=save_file)
btn2.pack()
image_label2 = PhotoImage(file='BESTUNDERPRESSURE-1.png')
label2 = ttk.Label(frame1, borderwidth=2, width=100, image=image_label2)
label2.pack()

##w_canv = 400  # ширина канвы
##python_image = Image.open("RC0132.jpg")  # представили изображение в виде объекта PIL.Image
##w, h = python_image.size  # узнаем размеры Ш х В
##new_h = int(h * w_canv / w)  # расчет новой высоты под ширину канвы
##scaled_image = python_image.resize((w_canv, new_h), Image.Resampling.LANCZOS)  # растянули/сжали + метод передискретизации
##canvas = Canvas(root, bg="white", width=w_canv, height=new_h)
##canvas.pack(anchor='nw', expand=1)
##image4canvas = ImageTk.PhotoImage(scaled_image)  # представили изображение в виде объекта PIL, с которым умеет работать канва
##canvas.create_image(0, 0, anchor='nw', image=image4canvas)  # нарисовали изображение на канве (отступ слева px, отступ сверху px)

columns_ = ("attribute", "attributeValue")
tree_ = ttk.Treeview(frame1, columns=columns_, show="headings")
tree_.pack(fill='both', expand=1)
tree_.heading("attribute", text="Информация")
tree_.heading("attributeValue", text="Значение")
tree_.column("#1", stretch='no', width=200)
tree_.column("#2", stretch='no', width=100)
tree_.yview_scroll(number=1, what="units")

btn3 = ttk.Button(frame1, text=f'Загрузить список', command=open_list)
btn3.pack(fill='x', anchor='center', padx=200)
btn4 = ttk.Button(frame1, text=f'Выбрать место сохранения', command=save_files)
btn4.pack(fill='x', anchor='center', padx=200)

frame1.pack(anchor='nw', fill='both', padx=5, pady=5, side='left')
#---------------------------------------------------------------------------------------------------------#

frame2 = ttk.Frame(root, border=1, height=50, width=50)

columns = ("manufacturer", "modelSeries", "engineSize", "fuelType", "modelYearFrom", "modelYearTo", "engineCodes")

tree = ttk.Treeview(frame2, columns=columns, show="headings")
tree.pack(fill='both', expand=1)

tree.heading("manufacturer", text="Марка", command=lambda: sort_col_tree(0, False))
tree.heading("modelSeries", text="Модель", command=lambda: sort_col_tree(1, False))
tree.heading("engineSize", text="Объем", command=lambda: sort_col_tree(2, False))
tree.heading("fuelType", text="Топливо", command=lambda: sort_col_tree(3, False))
tree.heading("modelYearFrom", text="год с", command=lambda: sort_col_tree(4, False))
tree.heading("modelYearTo", text="год по", command=lambda: sort_col_tree(5, False))
tree.heading("engineCodes", text="ДВС", command=lambda: sort_col_tree(6, False))
tree.column("#1", stretch='no', width=70)
tree.column("#2", stretch='no', width=220)
tree.column("#3", stretch='no', width=40)
tree.column("#4", stretch='no', width=70)
tree.column("#5", stretch='no', width=50)
tree.column("#6", stretch='no', width=50)
tree.column("#7", stretch='no', width=100)

scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')

tree["yscrollcommand"]=scrollbar.set

frame2.pack(anchor='ne', fill='both', padx=10, pady=10, side='right')
#---------------------------------------------------------------------------------------------------------#
root.mainloop()
