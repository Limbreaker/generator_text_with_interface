from tkinter import *


# TKINTER_SETTINGS
root = Tk()
root['bg'] = '#C8D3A6'
root.title('Генератор текста')
root.geometry('700x350')
root.resizable()


message = StringVar()
message2 = StringVar()
message3 = StringVar()
message_entry = Entry(textvariable=message)
message_entry2 = Entry(textvariable=message2)
message_entry3 = Entry(textvariable=message3)
message_entry2.place(relx=.50, rely=.31, relwidth=0.6, relheight=0.1, anchor="c")
message_entry.place(relx=.50, rely=.16, relwidth=0.6, relheight=0.1, anchor="c")
message_entry3.place(relx=.50, rely=.46, relwidth=0.6, relheight=0.1, anchor="c")
lb = Label(text='Название')
lb.place(relx=0.1, rely=.13)
lb2 = Label(text='Ссылка')
lb2.place(relx=0.1, rely=.28)
lb3 = Label(text='Время')
lb3.place(relx=0.1, rely=.43)


def text_gen(num):
    title = message.get()
    link = message2.get()
    time = message3.get()
    w = Text(root, height=7, width=86, borderwidth=4, wrap=WORD)
    w.place(relx=0, rely=0.61)
    text = ''
    if num == 1:
        text = f"""[boxes] 

        [boxcontent title="{title}" icon="fa-users" link="{link}" linktext="Перейти до відеоконференції" target="_blank"]{time}. Відеоконференція [/boxcontent]

[/boxes]"""
    elif num == 2:
        text = f"""[boxes]

        [boxcontent color="info" title=" Практичний самотренінг:  {title}" icon="fa-users" link="{link}" linktext="Перейти до відеоконференції" target="_blank"]{time}. Відеоконференція [/boxcontent]

[/boxes]"""
    elif num == 3:
        text = f"""[boxes] 

        [boxcontent title="Індивідуальне  заняття: {title} " icon="fa-users" link="{link}" linktext="Перейти до відеоконференції" target="_blank"]{time}. Відеоконференція [/boxcontent] 

[/boxes]"""

    w.insert(5.0, text)
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(text)
    clip.destroy()


def setup_btn1():
    text_gen(1)


def setup_btn2():
    text_gen(2)


def setup_btn3():
    text_gen(3)


def copy_button(INFO_TO_COPY):
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(INFO_TO_COPY)
    clip.destroy()


def clear_button():
    message_entry2.delete(0, END)
    message_entry.delete(0, END)
    message_entry3.delete(0, END)
    w = Text(root, height=7, width=86, borderwidth=4, wrap=WORD)
    w.place(relx=0, rely=0.61)


btn = Button(text='Занятие', background='#3BE3A1',command=setup_btn1)
btn.place(relx=0.15, rely=0.53)

btn = Button(text='Практичний самотренінг', background='#0D9FBF', command=setup_btn2)
btn.place(relx=0.35, rely=0.53)

btn = Button(text='Індивідуальне заняття', background='#EBE438', command=setup_btn3)
btn.place(relx=0.65, rely=0.53)

btn = Button(text='clear', background='#df798b', command=clear_button)
btn.place(relx=0.87, rely=0.30)

if __name__ == "__main__":
    root.mainloop()
