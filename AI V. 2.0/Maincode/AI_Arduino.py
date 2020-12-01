print("Hello from {CMS} AI Arduino community. " + "http://cmsplanes.ezyro.com")
import os
import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
from subprocess import *
import webbrowser

root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('AI Arduino')
frame.config(background='brown')
label = Label(frame, text="AI Arduino",bg='brown',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="C:\\Users\\praso_\\Dropbox\\My PC (LAPTOP-2R3CKJJJ)\\Desktop\\AI V. 2.0\\Maincode\\AnyConv.com__AnyConv.com__AI.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)

def lite():
    tkinter.messagebox.showinfo("Lite mode","Lite mode will help in saving your device battery.")
def lite_a():
    tkinter.messagebox.showinfo("Lite mode","Lite mode disabled.")
def hel():
   webbrowser.open("http://cmsplanes.ezyro.com")

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Prasoon rai.")


def anotherWin():
   tkinter.messagebox.showinfo("About",'AI Arduino\n Made Using\n-Python\n')

def setting():
    Popen("settings.bat")


menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Manager",menu=subm1)
subm1.add_command(label="More",command=hel)
subm1.add_command(label="Settings",command=setting)
subm1.add_command(label="Enable Lite mode", command=lite)
subm1.add_command(label="Disable Lite mode", command=lite_a)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Contributors",command=Contri)

def Open():
    Popen('python AI_Main.py')


but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='Talk!',command=Open,font=('helvetica 15 bold'))
but5.place(x=210,y=478)


root.mainloop()
