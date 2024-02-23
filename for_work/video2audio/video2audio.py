import os
import moviepy.editor
from tkinter import Tk, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from customtkinter import CTk, CTkLabel, CTkButton

def open_file():
    global filepath_open
    filepath_open = askopenfilename(
        title="Выбор файла",
        filetypes=(
            ('All-files', '*'),
            ('MPEG-file', ('*.mpg', '*.mpeg')),
            ('MP4-file', '*.mp4'),
            ('AVI-file', '*.avi'),
            ('QuickTime', '*.mov')))
    global file_name
    file_name = os.path.basename(filepath_open)
    file_name = os.path.splitext(file_name)[0]
    if filepath_open != "":
        open_label["text"] = f'Выбран файл: \n"{filepath_open}"'
    else:
        open_label["text"] = f'Файл не выбран!'


def save_file():
    filepath_save = asksaveasfilename(
        title='Сохранение файла',
        defaultextension='.mp3',
        filetypes=(('All-files', '*'), ('MP3-file', '*.mp3')),
        initialfile=f'{file_name}.mp3')
    video = moviepy.editor.VideoFileClip(filepath_open)
    audio = video.audio
    audio.write_audiofile(filepath_save)


if __name__ == '__main__':
    root = CTk()
    root.configure(background='#F0F8FF')
    root.title('Video To Audio')
    root.geometry("400x200+400+130")  # ширина х высота + позиция х\у
    root.resizable(False, False)  # растягивание границ окна
    root.iconbitmap(default="oil.ico")

    open_button = CTkButton(root, text='Открыть видео-файл', command=open_file)
    open_button.pack()

    open_label = ttk.Label(root, text='"Выберите видео-файл"', background='yellow')
    open_label.pack()

    save_button = CTkButton(root, text='Сохранить как \n аудио-файл', command=save_file)
    save_button.pack()

    root.mainloop()
