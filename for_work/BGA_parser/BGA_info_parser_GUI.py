from io import BytesIO
from PIL import Image, ImageTk
import requests
from tkinter import Tk, ttk, END, filedialog


def receiving_foto_info():
    global in_text_content
    in_text_content = in_text.get().rstrip().lstrip()
    label2.configure(text='Загрузка изображения...')

    for item in tree.get_children():  # чистка данных таблицы
        tree.delete(item)

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

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=(("Image files", "*.jpg"), ("All files", "*.*")), initialfile=f'{in_text_content}.jpg')
    if filepath != "":
        img = requests.get(url_pic)
        with open(filepath, "wb") as file:
            file.write(img.content)


root = Tk()
root.title('BGA PRODUCTS INFO-PARSER')
root.geometry("1200x550+400+130")  # ширина х высота + позиция х\у
root.resizable(True, True)  # растягивание границ окна
root.iconbitmap(default="D:\\PycharmProjects\\Courses\\for_work\\BGA_parser\\bga_logo.ico")
###############################################################################
frame1 = ttk.Frame(root, border=1, height=300, width=250)

label1 = ttk.Label(frame1, text='Введите артикул BGA:')
label1.pack()
in_text = ttk.Entry(frame1, width=20)
in_text.pack()
btn1 = ttk.Button(frame1, text='Загрузить', command=receiving_foto_info)
btn1.pack()
btn2 = ttk.Button(frame1, text='Сохранить', command=save_file)
btn2.pack()
label2 = ttk.Label(frame1)
label2.pack()

frame1.pack(anchor='nw', fill='both', padx=5, pady=5, side='left')
###############################################################################

frame2 = ttk.Frame(root, border=1, height=50, width=50)

columns = ("manufacturer", "modelSeries", "engineSize", "fuelType", "modelYearFrom", "modelYearTo", "engineCodes")

tree = ttk.Treeview(frame2, columns=columns, show="headings")
tree.pack(fill='both', expand=1)

tree.heading("manufacturer", text="Марка")
tree.heading("modelSeries", text="Модель")
tree.heading("engineSize", text="Объем")
tree.heading("fuelType", text="Топливо")
tree.heading("modelYearFrom", text="год с")
tree.heading("modelYearTo", text="год по")
tree.heading("engineCodes", text="ДВС")
tree.column("#1", stretch='no', width=70)
tree.column("#2", stretch='no', width=120)
tree.column("#3", stretch='no', width=40)
tree.column("#4", stretch='no', width=70)
tree.column("#5", stretch='no', width=50)
tree.column("#6", stretch='no', width=50)
tree.column("#7", stretch='no', width=100)

scrollbar = ttk.Scrollbar(orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')

tree["yscrollcommand"]=scrollbar.set

frame2.pack(anchor='ne', fill='both', padx=10, pady=10, side='right')

root.mainloop()