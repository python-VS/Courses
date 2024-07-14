from io import BytesIO
from PIL import Image, ImageTk
import requests
from tkinter import Tk, ttk, filedialog, PhotoImage, messagebox


def receiving_foto_info():
    global in_text_content
    in_text_content = in_text.get().rstrip().lstrip()
    label2.configure(text='Загрузка изображения...')

    root.update()

    global url_pic
    url_pic = f'https://catalogue.oris.com.tr/img/products/{in_text_content.rstrip().lstrip()}.jpg'

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


def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=(("Image files", "*.jpg"), ("All files", "*.*")), initialfile=f'{in_text_content}.jpg')
    if filepath != "":
        img = requests.get(url_pic)
        with open(filepath, "wb") as file:
            file.write(img.content)

def open_file():
    filepath_open = filedialog.askopenfilename(title="Выбор файла", filetypes=(('Все форматы', '*'), ('Текст', '*.txt')))
    with open(filepath_open, 'r', encoding='utf-8') as lst:  # открытие файла-списка необходимых брендов
        global list_ref
        list_ref = [line.strip('\n') for line in lst]

def save_files():
    url_pict = 'https://catalogue.oris.com.tr/img/products/'  # +артикул.jpg
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
        with open(file_path_gr + '/' + x +'.jpg', "wb") as file_:
            file_.write(response2.content)
    messagebox.showinfo(title='Информация', message='Скачивание завершено!')


root = Tk()
root.title('Download ORIS images')
root.geometry("860x800+230+30")
root.resizable(False, True)
root.iconbitmap(default="D:\\PycharmProjects\\Courses\\for_work\\downOris_images\\logo.ico")

label1 = ttk.Label(root, text='Введите артикул ORIS:')
label1.pack()
in_text = ttk.Entry(root, width=20)
in_text.pack()
btn1 = ttk.Button(root, text='Загрузить', command=receiving_foto_info)
btn1.pack()
btn2 = ttk.Button(root, text='Сохранить', command=save_file)
btn2.pack()
image_oris = PhotoImage(file='D:\\PycharmProjects\\Courses\\for_work\\downOris_images\\orislogo.png')
label2 = ttk.Label(root, borderwidth=2, width=100, image=image_oris)
label2.pack()

btn3 = ttk.Button(root, text=f'Загрузить список', command=open_file)
btn3.pack(fill='x', padx=100)
btn4 = ttk.Button(root, text=f'Выбрать место сохранения', command=save_files)
btn4.pack(fill='x', padx=100)

root.mainloop()
