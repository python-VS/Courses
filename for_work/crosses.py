import pyperclip
from tkinter import Tk, ttk, Text, END, Button
from datetime import datetime as dt

# list_tm = input("Вставьте список для кроссировки: ")
# list_tm2 = set(list_tm.split(sep='\t'))
# print(f"Введенный список для обработки {list_tm2}")
test = ['85006300_AJUSA', 'HL6366_BGA', 'PI06-0057_FRECCIA']
def mixlist(my_list):
    for i in my_list:
        for x in my_list:
            if i != x:
                z = f'{i}\t{x}'
                print(z)
            else:
                pass

mixlist(test)
# pyperclip.copy(data)
print("Обработка завершена, данные скопированы в буфер обмена")

root = Tk()
root.title("Приложение на Tkinter")  # текст заголовка окна
root.geometry("400x350+400+300")  # размеры +позиционирование на экране
root.resizable(False, False)  # возможность растягивать размер окна (горизонт, вертикаль)
root.minsize(200, 200)   # минимальные размеры: ширина - 200, высота - 150
root.maxsize(400, 300)   # максимальные размеры: ширина - 400, высота - 300
root.iconbitmap(default="Hopstarter.ico")  # иконка окна
root.attributes("-fullscreen", False)  # установка полноэкранного режима
root.attributes("-alpha", 0.99)  # прозрачность
root.attributes("-toolwindow", False)  # отключение верхней панели окна (сворачивание и разворачивание)

lab = ttk.Label(root, text="Вставьте список товаров", font="Arial 12")
lab.pack()

txt_input = Text(root, width=40, height=10, font="Arial 10", wrap='word')

input_text = txt_input.get('1.0', END)
def pasting():
    txt_input.insert(0.0, test)

btn = Button(root)  # создаем кнопку из пакета ttk c тестом и подчеркиванием символа по индексу
btn.config(text="Click", underline=1, command=pasting)

txt_input.pack()
btn.pack()

root.mainloop()
