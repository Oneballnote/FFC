import tkinter
from tkinter import font
from tkinter.constants import INSERT    
from Smain import impresion

pepe = []
def Ventana_principal():
    Inicio = tkinter.Tk()
    Inicio.title("Calculadora de proposiciones")
    Inicio.geometry('500x450')
    
    #Texto en la primer entrada
    def Insertp():
        Proposicion.insert(INSERT, "P")
    def Insertq():
        Proposicion.insert(INSERT, "Q")
    def Insertr():
        Proposicion.insert(INSERT, "R") 
    def Insertnot():
        Proposicion.insert(INSERT, "~")
    def Insertand():
        Proposicion.insert(INSERT, "∧")        
    def Insertor():
        Proposicion.insert(INSERT, "∨") 
    def Insertimpli():
        Proposicion.insert(INSERT, "→") 
    
    def Insertp():
        Comparacion_de_proposiciones.insert(INSERT, "P")
    def Insertq():
        Comparacion_de_proposiciones.insert(INSERT, "Q")
    def Insertr():
        Comparacion_de_proposiciones.insert(INSERT, "R") 
    def Insertnot():
        Comparacion_de_proposiciones.insert(INSERT, "~")
    def Insertand():
        Comparacion_de_proposiciones.insert(INSERT, "∧")        
    def Insertor():
        Comparacion_de_proposiciones.insert(INSERT, "∨") 
    def Insertimpli():
        Comparacion_de_proposiciones.insert(INSERT, "→")
    
    def impresion():
        lolo = Proposicion.get("1.0","end-1c")
        ImpresionDeTablas = tkinter.Tk()
        ImpresionDeTablas.title("Tablas")
        ImpresionDeTablas.geometry('500x450')
        datos = tkinter.Label(ImpresionDeTablas,text = lolo, font = ("MS Sans Serif", 15)).pack()
    
        tkinter.mainloop()
    
    def impresion2():
        lolo = Comparacion_de_proposiciones.get("1.0","end-1c")
        ImpresionDeTablas = tkinter.Tk()
        ImpresionDeTablas.title("Tablas")
        ImpresionDeTablas.geometry('500x450')
        datos = tkinter.Label(ImpresionDeTablas,text = lolo, font = ("MS Sans Serif", 15)).pack()
    
        tkinter.mainloop()
    
    #VentanaDeAjustes.configure(bg = Color_de_fondo)
    Titulo = tkinter.Label(text = "Tablas de verdad",font = ("MS Sans Serif", 15)).place(x = 160, y = 1)
   
    #Zona de proposiciones 
    Proposicion = tkinter.Text(Inicio, width = 30, 
                               height = 2, font = ("MS Sans Serif", 12))
    Proposicion.place(x = 125, y = 25)
    
    #Botones de proposiciones primitivas
    BotonP = tkinter.Button(Inicio, text = "P", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertp).place(x = 77, y = 80)
    BotonQ = tkinter.Button(Inicio, text = "Q", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertq).place(x = 165, y = 80)
    BotonR = tkinter.Button(Inicio, text = "R", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertr).place(x = 251, y = 80)
    
    #Botones de conjunciones
    BotonNot = tkinter.Button(Inicio, text = "Not", width = 5, 
                              height = 2, font = ("Roboto", 11), command = Insertnot).place(x = 336, y = 80)
    BotonAnd = tkinter.Button(Inicio, text = "And", width = 5, 
                              height = 2, font = ("Roboto", 11), command = Insertand).place(x = 77, y = 135)
    BotonOr = tkinter.Button(Inicio, text = "Or", width = 5, 
                             height = 2, font = ("Roboto", 11), command = Insertor).place(x = 165, y = 135)
    BotonImplicacion = tkinter.Button(Inicio, text = "→", width = 5, 
                                      height = 2, font = ("Roboto", 11), command = Insertimpli).place(x = 251, y = 135)
    BotonIgual = tkinter.Button(Inicio, text = "=", width = 5, 
                                height = 2, font = ("Roboto", 11), command = impresion).place(x = 336, y = 135)
    
    #Divisior
    Division = tkinter.Label(text = "-"*71).place(x = 0, y = 195)
    
    #Verificar si dos son iguales
    separacion = tkinter.Label(Inicio,text = "Comparación de proposiciones", font = ("MS Sans Serif", 15)).place(x = 115, y = 225)
    
    Comparacion_de_proposiciones = tkinter.Text(Inicio, width = 30, 
                                                height = 2, font = ("MS Sans Serif", 12))
    Comparacion_de_proposiciones.place(x = 125, y = 260)
    
    #Botones de proposiciones primitivas
    BotonP = tkinter.Button(Inicio, text = "P", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertp).place(x = 77, y = 310)
    BotonQ = tkinter.Button(Inicio, text = "Q", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertq).place(x = 165, y = 310)
    BotonR = tkinter.Button(Inicio, text = "R", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertr).place(x = 251, y = 310)
    
    ##Botones de conjunciones
    BotonNot = tkinter.Button(Inicio, text = "Not", width = 5, 
                            height = 2, font = ("Roboto", 11), command = Insertnot).place(x = 336, y = 310)
    BotonAnd = tkinter.Button(Inicio, text = "And", width = 5, 
                            height = 2, font = ("Roboto", 11), command = Insertand).place(x = 77, y = 365)
    BotonOr = tkinter.Button(Inicio, text = "Or", width = 5, 
                             height = 2, font = ("Roboto", 11), command = Insertor).place(x = 165, y = 365)
    BotonImplicacion = tkinter.Button(Inicio, text = "→", width = 5, 
                                      height = 2, font = ("Roboto", 11), command = Insertimpli).place(x = 251, y = 365)
    BotonIgual = tkinter.Button(Inicio, text = "=", width = 5, 
                                height = 2, font = ("Roboto", 11), command = impresion2).place(x = 336, y = 365)
    
      
    
    tkinter.mainloop() 
    
Ventana_principal()
