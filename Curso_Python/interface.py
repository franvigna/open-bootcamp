import tkinter
from tkinter import ttk
import random
from tkinter import filedialog
from tkinter import colorchooser

window = tkinter.Tk()


############LABEL AND WINDOW################
# label1 = tkinter.Label(window, text = "LABEL 1", bg= "yellow", fg="blue")
# label1.pack(ipadx=45, ipady=30, fill='x')

# label2 = tkinter.Label(window, text = "LABEL 3", bg= "red", fg="white")
# label2.pack(ipadx=45, ipady=30,  fill='x')

# label3 = tkinter.Label(window, text = "LABEL 1", bg= "blue", fg="yellow")
# label3.pack(ipadx=45, ipady=30,  fill='x')

# label4 = tkinter.Label(window, text = "LABEL 3", bg= "white", fg="green")
# label4.pack(ipadx=45, ipady=30, side='left')

# label5 = tkinter.Label(window, text = "LABEL 3", bg= "orange", fg="black")
# label5.pack(ipadx=45, ipady=30, side='left')

# label6 = tkinter.Label(window, text = "LABEL 3", bg= "green", fg="red")
# label6.pack(ipadx=45, ipady=30, side='right')



# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=5)


######lista#######

# lista = ['windows','MACos','linux','amigaOS','OS/2']
# lista_items = tkinter.StringVar(value=lista)
# listbox = tkinter.Listbox(window, height=20, listvariable=lista_items)

# listbox.grid(column=0,row=0,sticky=tkinter.W)

################radiobuton##############
# selected = tkinter.StringVar()

# r1 = ttk.Radiobutton(window,text='Si', value='1', variable=selected)
# r2 = ttk.Radiobutton(window,text='No', value='2', variable=selected)
# r3 = ttk.Radiobutton(window,text='No se', value='3', variable=selected)

# r1.grid(column=0,row=1,pady=10,padx=10,sticky=tkinter.W)
# r2.grid(column=0,row=2,pady=10,padx=10,sticky=tkinter.W)
# r3.grid(column=0,row=3,pady=10,padx=10,sticky=tkinter.W)

# #######CHECKBOX###############
# def mifuncion():
#     print('clickeado')
# seleccionado = tkinter.StringVar()
# checkbox = ttk.Checkbutton(window,text='Acepto las condiciones', variable=seleccionado, command=mifuncion)
# checkbox.grid(column=0, row=0)


#############LOGIN#################

# frame =ttk.Frame(window)

# label = ttk.Label(frame, text='hola')

# label.grid(column=0,row=0,sticky=tkinter.W,padx=50,pady=50)

# label.grid(column=0,row=0,sticky=tkinter.W)


# #ETIQUETA USUARIO
# username_label = ttk.Label(window, text='Username: ')
# username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5,pady=5)

# #CAMPO USUARIO
# username_entry = ttk.Entry(window)
# username_entry.grid(column=1,row=0, sticky=tkinter.E, padx=5,pady=5)

# #ETIQUETA CONTRASEÑA
# password_label = ttk.Label(window, text='Password: ')
# password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5,pady=5)

# #CAMPO CONTRASEÑA
# password_entry = ttk.Entry(window, show="*")
# password_entry.grid(column=1,row=1, sticky=tkinter.E, padx=5,pady=5)

# #BOTON
# login_button = ttk.Button(window, text='Login ')
# login_button.grid(column=1,row=3, sticky=tkinter.E, padx=5,pady=5 )

##########PLACE##############

# colors = ['blue','red','yellow','purple','green','black']

# for x in range(0,20):
#     color = random.randint(0,len(colors)-1)
#     color2 = random.randint(0,len(colors)-1)
 
    
#     label1 = tkinter.Label(window, text="RANDOMM",bg=colors[color], fg=colors[color2],padx=random.randint(0,50),pady=random.randint(0,50) )
    
#     label1.place(x=random.randint(0,100),y=random.randint(0,100),)

##############EVENTOS###################
# def saludar(event):
#     print('han hecho click en saludar')
    
# def saludarDobleClick(event):
#     print('click doble')
# def salir(event):
#     print('adios')
#     window.quit()
# boton = ttk.Button(window,text='haz click')
# boton.pack()
# boton.bind('<Button-1>',saludar)
# boton.bind('<Double-1>',saludarDobleClick)


# botonSalir = tkinter.Button(window,text='salir',bg='red')
# botonSalir.pack()
# botonSalir.bind('<Button-1>',salir)


###########OPEN FILE################

file = filedialog.askopenfilename()
color = colorchooser.askcolor(initialcolor='#ffffff')


window.mainloop()
