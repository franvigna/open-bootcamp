from tkinter import *
import tkinter

window = Tk()

# Set the size of the windowdow
window.geometry("700x350")


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)



lista = ['Python','C++','Java','PHP','JavaScript']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=20, listvariable=lista_items)

listbox.grid(column=0,row=0,sticky=tkinter.W)


window.mainloop()