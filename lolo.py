import tkinter
from tkinter import *

def Ventana_principal():
    Main_window = tkinter.Tk()
    Main_window.geometry('300x200')
    
    
    Entrada_datos = Entry(Main_window).place(x = '75', y = '20')
       
    botonP = Button(Main_window, text = 'p').place(x = '70', y = '40')
    botonQ = Button(Main_window, text = 'q').place(x = '105', y = '40')
    buttonR = Button(Main_window, text = 'r').place(x = '140', y = '40')
    botonand = Button(Main_window, text = 'y').place(x = '70', y = '65')
    boton_Or = Button(Main_window, text = 'o').place(x = '105', y = '65')
    boton_igual = Button(Main_window, text = '='). place(x = '140', y = '65')
    
    tkinter.mainloop()

Ventana_principal()
    
