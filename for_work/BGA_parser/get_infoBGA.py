import requests, re
from tkinter import Tk, END, ttk

ref = input('Введите артикул: ')
url = f'https://store.bgautomotive.co.uk/Product/GetProductList/?searchText=~~~~~{ref}~True~~'
req = requests.get(url)

_json = req.json()
list_ = _json["productList"]

pattern1 = r"\(\w.{0,50}$|( Saloon )|( Hatchback )|( Van )|(Estate Front-Wheel Drive)|(Estate)|(Station Wagon)"
pattern2 = r"^19|^20"
vehicles = []
for i in list_:
    a = i["manufacturer"], i["modelSeries"], i["engineSize"], i["fuelType"], i["modelYearFrom"], i["modelYearTo"], i["engineCodes"]
    vehicles.append(a)
vehicles.sort()

root = Tk()
root.title("BGA")
root.geometry("550x500")

# определяем столбцы
columns = ("manufacturer", "modelSeries", "engineSize", "fuelType", "modelYearFrom", "modelYearTo", "engineCodes")

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill='both', expand=1)

# определяем заголовки
tree.heading("manufacturer", text="Марка")
tree.heading("modelSeries", text="Модель")
tree.heading("engineSize", text="Объем")
tree.heading("fuelType", text="Топливо")
tree.heading("modelYearFrom", text="год с")
tree.heading("modelYearTo", text="год по")
tree.heading("engineCodes", text="ДВС")
tree.column("#1", stretch='no', width=70)
tree.column("#2", stretch='no', width=60)
tree.column("#3", stretch='no', width=100)
tree.column("#4", stretch='no', width=70)
tree.column("#5", stretch='no', width=60)
tree.column("#6", stretch='no', width=100)
tree.column("#7", stretch='no', width=100)
# добавляем данные
for car in vehicles:
    tree.insert("", END, values=car)

root.mainloop()
