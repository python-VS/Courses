from tkinter import Tk, ttk, END, Text
import pyperclip, re


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
    list1 = list(in_text_content.split(sep='\n'))
    list2 = []

    for w in list1:
        w = re.sub(r'\r', r'', w)
        if w != '':
            list2.append(w)
        else:
            pass

    for i in list2:
        for x in list2:
            if i != x:
                z = f'{i}\t{x}\n'
                out_text.insert(0.0, z)
            else:
                pass

if __name__ == '__main__':
    root = Tk()
    root.title('Crosses')
    root.geometry("700x850+400+130")  # ширина х высота + позиция х\у
    root.resizable(False, False)  # растягивание границ окна
    #root.iconbitmap(default="favicon.ico")

    in_text = Text(root, wrap='word', width=80)
    in_text.grid(row=0, column=0, columnspan=5)


    btn1 = ttk.Button(root, text='Вставить', command=insert_text_buff).grid(row=1, column=1)
    btn2 = ttk.Button(root, text='Очистить', command=delete_text_in).grid(row=1, column=2)
    btn3 = ttk.Button(root, text='Обработать', command=get_text_input).grid(row=1, column=3)

    out_text = Text(root, wrap='word')
    out_text.grid(row=2, column=0, columnspan=5)

    btn4 = ttk.Button(root, text='Скопировть', command=copy_text_buff).grid(row=3, column=1)
    btn5 = ttk.Button(root, text='Очистить', command=delete_text_out).grid(row=3, column=2)
    btn6 = ttk.Button(root, text='Сохранить').grid(row=3, column=3)

    root.mainloop()