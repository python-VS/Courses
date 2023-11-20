from tkinter import Tk, ttk, Button, Label, END, Text, BOTH, Frame
import pyperclip


data = ('551125B_CORTECO', '640VE31280000_MAHLE', '701010_TRW ENGINE COMPONENT', 'PV1456_PATRON', 'R6275/SNT_FRECCIA', 'V004307_BGA')
##def buff():
##    ttt = pyperclip.paste()
##    in_text = ttt.get()
def insert_text_buff():
    past = pyperclip.paste()
    in_text.insert(0.0, past)

def copy_text_buff():
    cop = out_text.get(0.0, END)
    pyperclip.copy(cop)

def delete_text_in():
    in_text.delete(0.0, END)

def delete_text_out():
    out_text.delete(0.0, END)

def get_text_input():
    in_text_content = in_text.get(0.0, END)
    _list = in_text_content.split(sep='\n')
    #out_text.insert(0.0, in_text_content)
    #in_text.delete(0.0, END)

    for i in _list:
        for x in _list:
            if i != x:
                z = f'{i}\t{x}\n'
                out_text.insert(0.0, z)
            else:
                pass


root = Tk()
root.title('Crosses')
root.geometry("500x550+400+130")  # ширина х высота + позиция х\у
root.resizable(True, True)  # растягивание границ окна
#root.iconbitmap(default="favicon.ico")

in_text = Text(root, wrap='word', width=40, height=10)
in_text.grid(row=0, column=0, columnspan=5)


btn1 = ttk.Button(root, text='Вставить', command=insert_text_buff).grid(row=1, column=1)
btn2 = ttk.Button(root, text='Очистить', command=delete_text_in).grid(row=1, column=2)
btn3 = ttk.Button(root, text='Обработать', command=get_text_input).grid(row=1, column=3)

out_text = Text(root, wrap='word', height=10)
out_text.grid(row=2, column=0, columnspan=5)

btn4 = ttk.Button(root, text='Скопировть', command=copy_text_buff).grid(row=3, column=1)
btn5 = ttk.Button(root, text='Очистить', command=delete_text_out).grid(row=3, column=2)
btn6 = ttk.Button(root, text='Сохранить').grid(row=3, column=3)

root.mainloop()