import tkinter
from tkinter import font
from tkinter.constants import INSERT    
from Smain import tablas
pepe = []
def Ventana_principal():
    Inicio = tkinter.Tk()
    Inicio.title("Calculadora de proposiciones")
    Inicio.geometry('500x450')
    
    #Texto en el primer recuadro
    def Insertp():
        Proposicion.insert(INSERT, "P ")
    def Insertq():
        Proposicion.insert(INSERT, "Q ")
    def Insertr():
        Proposicion.insert(INSERT, "R ") 
    def Insertnot():
        Proposicion.insert(INSERT, "Not ")
    def Insertand():
        Proposicion.insert(INSERT, "∧ ")        
    def Insertor():
        Proposicion.insert(INSERT, "∨ ") 
    def Insertimpli():
        Proposicion.insert(INSERT, "→ ") 
    
    #Texto en el segundo recuadro
    def Insertp2():
        Comparacion_de_proposiciones.insert(INSERT, "P ")
    def Insertq2():
        Comparacion_de_proposiciones.insert(INSERT, "Q ")
    def Insertr2():
        Comparacion_de_proposiciones.insert(INSERT, "R ") 
    def Insertnot2():
        Comparacion_de_proposiciones.insert(INSERT, "Not ")
    def Insertand2():
        Comparacion_de_proposiciones.insert(INSERT, "∧ ")        
    def Insertor2():
        Comparacion_de_proposiciones.insert(INSERT, "∨ ") 
    def Insertimpli2():
        Comparacion_de_proposiciones.insert(INSERT, "→ ")
    
    def impresion():
        global Primerentrada 
        Primerentrada = Proposicion.get("1.0","end-1c")
        ImpresionDeTablas = tkinter.Tk()
        ImpresionDeTablas.title("Tablas")
        ImpresionDeTablas.geometry('500x450')
        datos = tkinter.Label(ImpresionDeTablas,text = Primerentrada, font = ("MS Sans Serif", 15)).pack()
    
        tkinter.mainloop()
    
    def impresion2():
        global segundaEntrada
        segundaEntrada = Comparacion_de_proposiciones.get("1.0","end-1c")
        ImpresionDeTablas = tkinter.Tk()
        ImpresionDeTablas.title("Tablas")
        ImpresionDeTablas.geometry('500x450')
        datos = tkinter.Label(ImpresionDeTablas,text = tablas(segundaEntrada), font = ("MS Sans Serif", 15)).pack()
    
        tkinter.mainloop()
    
    Inicio.configure(bg = "#252525")
    Titulo = tkinter.Label(text = "Tablas de verdad",font = ("MS Sans Serif", 15), bg = "#252525", fg = "#D5D5D5").place(x = 160, y = 1)
   
    #Zona de proposiciones 
    Proposicion = tkinter.Text(Inicio, width = 30, border = 0,
                               height = 2, font = ("MS Sans Serif", 12))
    Proposicion.place(x = 125, y = 25)
    
    #Botones de proposiciones primitivas
    BotonP = tkinter.Button(Inicio, text = "P", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertp, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 77, y = 80)
    BotonQ = tkinter.Button(Inicio, text = "Q", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertq, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 165, y = 80)
    BotonR = tkinter.Button(Inicio, text = "R", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertr, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 251, y = 80)
    
    #Botones de conjunciones
    BotonNot = tkinter.Button(Inicio, text = "Not", width = 5, 
                              height = 2, font = ("Roboto", 11), command = Insertnot, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 336, y = 80)
    BotonAnd = tkinter.Button(Inicio, text = "And", width = 5, 
                              height = 2, font = ("Roboto", 11), command = Insertand, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 77, y = 135)
    BotonOr = tkinter.Button(Inicio, text = "Or", width = 5, 
                             height = 2, font = ("Roboto", 11), command = Insertor, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 165, y = 135)
    BotonImplicacion = tkinter.Button(Inicio, text = "→", width = 5, 
                                      height = 2, font = ("Roboto", 11), command = Insertimpli, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 251, y = 135)
    BotonIgual = tkinter.Button(Inicio, text = "=", width = 5, 
                                height = 2, font = ("Roboto", 11), command = impresion, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 336, y = 135)
    
    #Divisior
    Division = tkinter.Label(text = "-"*71, bg = "#252525", fg = "#A2A09D").place(x = 0, y = 195)
    
    #Verificar si dos son iguales
    separacion = tkinter.Label(Inicio,text = "Comparación de proposiciones", font = ("MS Sans Serif", 15), bg = "#252525", fg = "#D5D5D5").place(x = 115, y = 225)
    
    Comparacion_de_proposiciones = tkinter.Text(Inicio, width = 30, border = 0,
                                                height = 2, font = ("MS Sans Serif", 12))
    Comparacion_de_proposiciones.place(x = 125, y = 260)
    
    #Botones de proposiciones primitivas
    BotonP = tkinter.Button(Inicio, text = "P", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertp2, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 77, y = 310)
    BotonQ = tkinter.Button(Inicio, text = "Q", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertq2, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 165, y = 310)
    BotonR = tkinter.Button(Inicio, text = "R", width = 5 , 
                            height = 2, font = ("Roboto", 11), command = Insertr2, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 251, y = 310)
    
    ##Botones de conjunciones
    BotonNot = tkinter.Button(Inicio, text = "Not", width = 5, 
                            height = 2, font = ("Roboto", 11), command = Insertnot2, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 336, y = 310)
    BotonAnd = tkinter.Button(Inicio, text = "And", width = 5, 
                            height = 2, font = ("Roboto", 11), command = Insertand2, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 77, y = 365)
    BotonOr = tkinter.Button(Inicio, text = "Or", width = 5, 
                             height = 2, font = ("Roboto", 11), command = Insertor2, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 165, y = 365)
    BotonImplicacion = tkinter.Button(Inicio, text = "→", width = 5, 
                                      height = 2, font = ("Roboto", 11), command = Insertimpli2, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 251, y = 365)
    BotonIgual = tkinter.Button(Inicio, text = "=", width = 5, 
                                height = 2, font = ("Roboto", 11), command = impresion2, bg = "#A2A09D", activebackground = "#D5D5D5").place(x = 336, y = 365)
    
      
    
    tkinter.mainloop() 
Ventana_principal()
