from tkinter import *
import threading
import time
import random as ran
import tkinter.font as tkFont

root = Tk()
root.title("抽号软件_基于Tkinter")
root.geometry('300x300')
fontStyle = tkFont.Font(size=50)#family="Regular",
label1 = Label(root,text='0',font=fontStyle,height=3,width=13,fg='red')
label1.pack()


def create():
    while True:
        num = ran.randint(1,52)
        return num

def rand():
    while(True):
        if (bsn % 2) == 0:
            time.sleep(0.001)
            continue
        else:
            label1['text'] = create()
            time.sleep(0.04)

def rand_():
    global bsn
    bsn += 1


bsn = 1
b = Button(root, text="点击抽号", command = rand_, height=3, width=16)
#b.place(x=150,y=250)
b.pack()

t = threading.Thread(target=rand,args=(),name='thread-refresh')
t.setDaemon(True)
t.start()

root.mainloop()
