from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry

def inch_to_sm():
    i = float(input_inch.get())
    sm = round(i * 2.54, 2)
    label2.configure(text=f'В сантиметрах: {sm}')


if __name__ == '__main__':
    root = CTk()
    root.configure(background='#F0F8FF')
    root.title('Inch to Sm')
    root.geometry("300x150+400+130")  # ширина х высота + позиция х\у
    root.attributes("-toolwindow", False)
    root.resizable(False, False)  # растягивание границ окна

    label1 = CTkLabel(root, text='Введите значение в дюймах:')
    label1.pack(anchor='nw', padx=6, pady=6)

    input_inch = CTkEntry(root)
    input_inch.pack(anchor='nw', padx=6, pady=6)

    btn = CTkButton(root, text="Рассчитать", command=inch_to_sm)
    btn.pack(anchor='nw', padx=6, pady=6)

    label2 = CTkLabel(root, text="")
    label2.pack(anchor='nw', padx=6, pady=6)

    root.mainloop()
