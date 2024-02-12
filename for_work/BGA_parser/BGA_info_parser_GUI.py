from io import BytesIO
from PIL import Image, ImageTk
import requests
from tkinter import Tk, ttk, END, Text, Entry, filedialog, Button, PhotoImage, Label
from customtkinter import CTk, CTkFrame, CTkButton, CTkTextbox, CTkEntry, CTkLabel


def get_text_input():
    global in_text_content
    in_text_content = in_text.get().rstrip().lstrip()
    label2.configure(text='Загрузка изображения...')
    root.update()
    global url
    url = f'https://store.bgautomotive.co.uk/Images/ProductImages/{in_text_content.rstrip().lstrip()}.jpg'
    try:
        response = requests.get(url, timeout=10)
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

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=(("Image files", "*.jpg"), ("All files", "*.*")), initialfile=f'{in_text_content}.jpg')
    if filepath != "":
        img = requests.get(url)
        with open(filepath, "wb") as file:
            file.write(img.content)

root = CTk()
root.title('Download BGA images')
root.geometry("700x550+400+130")  # ширина х высота + позиция х\у
root.resizable(False, False)  # растягивание границ окна
root.iconbitmap(default="bga_logo.ico")

frame1 = CTkFrame(root, border_width=1)
label1 = CTkLabel(frame1, text='Введите артикул BGA:')
label1.pack()

in_text = Entry(frame1, width=20)
in_text.pack()

btn1 = CTkButton(frame1, text='Загрузить', height=1, command=get_text_input)
btn1.pack()
frame1.pack(anchor='nw', fill='x', padx=5, pady=5)

frame2 = CTkFrame(root, border_width=1)
label2 = Label(frame2)
label2.pack()

btn2 = CTkButton(frame2, text='Сохранить', height=1, command=save_file)
btn2.pack()

frame2.pack(anchor='nw', fill='x', padx=5, pady=5)

root.mainloop()
