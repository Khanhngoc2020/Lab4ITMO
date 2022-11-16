import tkinter
from tkinter import *
import pygame
from PIL import ImageTk, Image
from tkinter import messagebox
from create_key import keyCreate

def click():
    # создать сообщение для "забыть пароль"
    messagebox.showerror(title = 'ERROR', message='Соединение нестабильно, проверьте соединение еще раз.')

def welcomeKe():
    messagebox.showinfo(title='Success', message='Your character is Kevin')
def welcomeAn():
    messagebox.showinfo(title='Success', message='Your character is Anton')
def welcomeLi():
    messagebox.showinfo(title='Success', message='Your character is Lisa')
def welcomeLu():
    messagebox.showinfo(title='Success', message='Your character is Lucky')
def welcomeBob():
    messagebox.showinfo(title='Success', message='Your character is Bob')


def createWindow():
    code = str(codeInput.get())

    window.destroy()
    newWindow = Tk()
    newWindow.geometry('1280x720')
    newWindow.title('Lost in the universe')
    BG2 = ImageTk.PhotoImage(Image.open('image/Choose (2).jpeg'))
    label=Label(newWindow,image=BG2)
    label = tkinter.Label(newWindow, image=BG2)
    label.place(x=0, y=0)

    lb = Label(newWindow, text='Here is your code: ' + keyCreate(code),
               font=('Times New Roman', 15),bg='white',fg='dark blue').place(x=500, y=220)


    keFrame = Frame(newWindow, background='grey')
    keFrame.place(x = 100, y = 600)
    ke = Button(keFrame,command=welcomeKe, text='Kevin', font=('Consolas', 10), width=10).pack(side=BOTTOM)

    anFrame = Frame(newWindow,background='grey')
    anFrame.place(x=340,y=600)
    an = Button(anFrame,command=welcomeAn, text='Anton', font=('Consolas', 10), width=10).pack(side=BOTTOM)

    liFrame = Frame(newWindow,background='grey')
    liFrame.place(x=600,y=600)
    li = Button(liFrame,command=welcomeLi, text='Lisa', font=('Consolas', 10), width=10).pack(side=BOTTOM)

    luFrame = Frame(newWindow,background='grey')
    luFrame.place(x = 850,y=600)
    lu = Button(luFrame, command=welcomeLu, text='Lucky', font=('Consolas', 10), width=10).pack(side=BOTTOM)

    bobFrame = Frame(newWindow,background='grey')
    bobFrame.place(x=1107, y=600)
    bob = Button(bobFrame, command=welcomeBob, text='Bob', font=('Consolas', 10), width=10).pack(side=BOTTOM)

    newWindow.mainloop()

#_______
window = Tk()
window.geometry('1280x720')

BG = ImageTk.PhotoImage(Image.open('image/BG.png'))
panel = tkinter.Label(window, image=BG)
panel.pack()

icon = PhotoImage(file ='image/icon.png')
window.iconphoto(True, icon)

#Назвать имя для игры
window.title("Lost in the universe")

#---------------------
#создать логин
label = Label(window, )
frame = Frame(window,bg='Gray')
frame.place(x=550, y=330)
login = Button(frame, command=createWindow,text="Вход",font=('Consolas', 10), width=10).pack(side=BOTTOM)

frame1 = Frame(window,bg='Gray')
frame1.place(x=720 , y=330)
forget = Button(frame1, command=click, text="Забыть пароль", font=('Consolas', 10), width=15).pack(side=BOTTOM)

user_name = Label(window, text='Username: ').place(x=550, y = 250)
userEntry = Entry(window, width = 30).place(x = 650, y = 250)
passwork = Label(window, text='Password: ').place(x=550, y = 290)
passEntry = Entry(window, width = 30, show='*').place(x = 650, y = 290)

lb = Label(window, text='Enter your code').place(x = 550, y =200)
note = Label(window, text='Введите случайное букво в 6-й позиции и 3 случайные числа в 7-й 8-й и 9-й позициях').place(x = 780, y =200)

codeInput = Entry(window, font=('Times New Roman', 10))
codeInput.place(x=650, y=200)
codeInput.focus()


#---------------------
#создать анимацию

#-------------------------
pygame.mixer.init()

def play():
    pygame.mixer.music.load('Two Step.mp3')
    pygame.mixer.music.play(loops= 0)
def stop():
    pygame.mixer.music.stop()

musicBu = Button(window,command=play, text='song', font=('Helvetica', 10), width=6)
musicBu.place(x = 560, y = 370)

stopBu = Button(window,command=stop,text='stop',font=('Helvetica', 10), width=6)
stopBu.place(x = 750, y = 370)

window.mainloop()
