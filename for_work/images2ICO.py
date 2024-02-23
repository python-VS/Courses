from os.path import basename, splitext
from PIL.Image import open
from tkinter.ttk import Label
from tkinter.filedialog import askopenfilename, asksaveasfilename
from customtkinter import CTk, CTkButton

def open_file():
    global filepath_open
    filepath_open = askopenfilename(
        title="Выбор файла",
        filetypes=(
            ('All-files', '*'),
            ('JPEG-file', ('*.jpg', '*.jpeg')),
            ('PNG-file', '*.png'),
            ('BMP-file', '*.bmp'),
            ('GIF-file', '*.gif'),
            ('TIFF-file', ('*.tif', '*.tiff'))))
    global file_name
    file_name = basename(filepath_open)
    file_name = splitext(file_name)[0]
    if filepath_open != "":
        open_label["text"] = f'Выбран файл: \n"{filepath_open}"'
    else:
        open_label["text"] = f'Файл не выбран!'


def save_file():
    filepath_save = asksaveasfilename(
        title='Сохранение файла',
        defaultextension='.ico',
        filetypes=(('All-files', '*'), ('ICO-file', '*.ico')),
        initialfile=f'{file_name}.ico')
    logo = open(filepath_open)
    logo.save(filepath_save, format='ICO', sizes=[(32, 32)])


if __name__ == '__main__':
    root = CTk()
    root.configure(background='#F0F8FF')
    root.title('Images To ICO')
    root.geometry("400x200+400+130")
    root.resizable(False, False)

    open_button = CTkButton(root, text='Открыть изображение', command=open_file)
    open_button.pack()

    open_label = Label(root, text='"Выберите изображение"', background='yellow')
    open_label.pack()

    save_button = CTkButton(root, text='Сохранить как ICO', command=save_file)
    save_button.pack()

    root.mainloop()
