import socket
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel

def get_hostname_IP():
    global website
    website = in_text.get()
    try:
        lbl.configure(text=f'Hostname: {website}\nIP: {socket.gethostbyname(website)}')
    except socket.gaierror as error:
        lbl.configure(text=f'Неизвестное имя Хоста,\n ошибка:\n {error}')


if __name__ == '__main__':
    root = CTk()
    root.title('IP of website')
    root.geometry("250x150+400+130")  # ширина х высота + позиция х\у
    root.resizable(False, False)  # растягивание границ окна

    in_text = CTkEntry(root)
    in_text.pack()
    btn = CTkButton(root, text='Получить', command=get_hostname_IP)
    btn.pack()
    lbl = CTkLabel(root, text='')
    lbl.pack()

    root.mainloop()
