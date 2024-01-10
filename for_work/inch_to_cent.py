from tkinter import Tk, ttk


def inch_to_sm():
    i = float(input_inch.get())
    sm = round(i * 2.54, 2)
    label2["text"] = f'В сантиметрах: {sm}'


if __name__ == '__main__':
    root = Tk()
    root.configure(background='#F0F8FF')
    root.title('Inch to Sm')
    root.geometry("300x250+400+130")  # ширина х высота + позиция х\у
    root.resizable(False, False)  # растягивание границ окна

    label1 = ttk.Label(root, text='Введите значение в дюймах:')
    label1.pack(anchor='nw', padx=6, pady=6)

    input_inch = ttk.Entry(root)
    input_inch.pack(anchor='nw', padx=6, pady=6)

    btn = ttk.Button(root, text="Рассчитать", command=inch_to_sm)
    btn.pack(anchor='nw', padx=6, pady=6)

    label2 = ttk.Label(root)
    label2.pack(anchor='nw', padx=6, pady=6)

    root.mainloop()
