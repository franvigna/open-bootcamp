# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Define a function to get the output for selected option
def selection():
    label.config(text="{}".format(radio.get()))
    
def reset():
    radio.set(None)
    label.config(text='')
    
    
radio = StringVar()
radio.set(None)

Label(text="Cual es tu lenguaje de programacion favorito?", font=('Aerial 11')).pack()

# Define radiobutton for each options
r1 = Radiobutton(win, text="C++", variable=radio, value="C++", command=selection)
r1.pack(anchor=N)

r2 = Radiobutton(win, text="Python", variable=radio, value="Python", command=selection)
r2.pack(anchor=N)

r3 = Radiobutton(win, text="Java", variable=radio, value="Java", command=selection)
r3.pack(anchor=N)


# Define a label widget
label = Label(win)
label.pack()

Button(win, text="reset", command=reset).pack()

win.mainloop()