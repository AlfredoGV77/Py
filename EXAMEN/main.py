import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import re
from peso import *
from velocidad import *
from colores import *
from altura import *
from io import open

class FramePrincipal:
    def __init__(self, master):
            self.master = master
            master.title("GRAFICAS")
            master.config(bg="deep pink")
            master.geometry('500x500')
            #el titulo y su estilo
            self.titulo = Label()
            self.titulo.pack(anchor = CENTER)
            self.titulo.config(text="GRAFICAS", fg = "white", bg = "deep pink",font = ("Arial", 25))
            #el css de las instrucciones y pues rosita todo por que se ve bonitoo
            self.ins = Label()
            self.ins.pack(anchor = CENTER)
            self.ins.config(text="Por fa, presione un boton para seguir",fg = "white", bg = "deep pink",font = (" Fantasque Sans Mono", 15))
                                                
            self.reg = Button(self.master, text="GRAFICAS PESO", command= self.peso)
            self.reg.place(x=120, y = 100, width= 280, height=30)
            self.reg.config(fg = "white", bg="deep pink", font = ("Arial", 15),)

            self.rag = Button(self.master, text="GRAFICAS ALTURA", command= self.altura)
            self.rag.place(x=120, y = 200, width= 280, height=30)
            self.rag.config(fg = "white",bg="deep pink", font = ("Arial", 15),)

            self.rig = Button(self.master, text="GRAFICAS VELOCIDAD", command= self.velocidad)
            self.rig.place(x=120, y = 300, width= 280, height=30)
            self.rig.config(fg = "white",bg="deep pink", font = ("Arial", 15),)

            self.rog = Button(self.master, text="GRAFICAS COLORES", command= self.colores)
            self.rog.place(x=120, y = 400, width= 280, height=30)
            self.rog.config(fg = "white",bg="deep pink", font = ("Arial", 15),)
            
        
        
    def peso(self):
        new_window = Toplevel(root)
        new_window.geometry('500x280')
        new_window.config(bg = 'deep pink')
        self.titleAbsolute = Label(new_window)
        self.titleAbsolute.pack(anchor = CENTER)
        self.titleAbsolute.config(text = "Eliga la grafica",bg='deep pink', fg = "white", font = ("Arial", 16))
        self.PESOB = Button(new_window, text = "Barra", command = self.barra)
        self.PESOB.place(x = 100, y =80, width = 280, height = 30)
        self.PESOB.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.PESOP = Button(new_window, text = "Pastel", command = self.pastel)
        self.PESOP.place(x = 100, y =130, width = 280, height = 30)
        self.PESOP.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.PESOF = Button(new_window, text = "Frecuencia Abs", command = self.abs)
        self.PESOF.place(x = 100, y =180, width = 280, height = 30)
        self.PESOF.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.PESOPO = Button(new_window, text = "Poligono", command = self.poo)
        self.PESOPO.place(x = 100, y =230, width = 280, height = 30)
        self.PESOPO.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        


    def barra(self):
        pbarra()
        
    def pastel(self):
        ppastel()
        
    def abs(self):
        pFAcumulada()
        
    def poo(self):
        pesoPoligonos()

    
        
        
    def altura(self):
        new_window = Toplevel(root)
        new_window.geometry('500x280')
        new_window.config(bg = 'deep pink')
        self.titleAbsolute = Label(new_window)
        self.titleAbsolute.pack(anchor = CENTER)
        self.titleAbsolute.config(text = "Eliga la grafica",bg='deep pink', fg = "white", font = ("Arial", 16))
        self.VENTANA = Button(new_window, text = "Barra", command = self.barra2)
        self.VENTANA.place(x = 100, y =80, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Pastel", command = self.pastel2)
        self.VENTANA.place(x = 100, y =130, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Frecuencia Abs", command = self.abs2)
        self.VENTANA.place(x = 100, y =180, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Poligono", command = self.poo2)
        self.VENTANA.place(x = 100, y =230, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))


    def barra2(self):
        abarra()
        
    def pastel2(self):
        apastel()
        
    def abs2(self):
        aFAcumulada()
        
    def poo2(self):
        aPoligonos()

        
        
    def velocidad(self):
        new_window = Toplevel(root)
        new_window.geometry('500x280')
        new_window.config(bg = 'deep pink')
        self.titleAbsolute = Label(new_window)
        self.titleAbsolute.pack(anchor = CENTER)
        self.titleAbsolute.config(text = "Eliga la grafica",bg='deep pink', fg = "white", font = ("Arial", 16))
        self.VENTANA = Button(new_window, text = "Barra", command = self.barra3)
        self.VENTANA.place(x = 100, y =80, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Pastel", command = self.pastel3)
        self.VENTANA.place(x = 100, y =130, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Frecuencia Abs", command = self.abs3)
        self.VENTANA.place(x = 100, y =180, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Poligono", command = self.poo3)
        self.VENTANA.place(x = 100, y =230, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))


    def barra3(self):
        vbarra()
        
    def pastel3(self):
        vPastel()
        
    def abs3(self):
        vFAcumulada()
        
    def poo3(self):
        vPoligono()
        
        

    def colores(self):
        new_window = Toplevel(root)
        new_window.geometry('500x280')
        new_window.config(bg = 'deep pink')
        self.titleAbsolute = Label(new_window)
        self.titleAbsolute.pack(anchor = CENTER)
        self.titleAbsolute.config(text = "Eliga la grafica",bg='deep pink', fg = "white", font = ("Arial", 16))
        self.VENTANA = Button(new_window, text = "Barra", command = self.barra4)
        self.VENTANA.place(x = 100, y =80, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Pastel", command = self.pastel4)
        self.VENTANA.place(x = 100, y =130, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Frecuencia Abs", command = self.abs4)
        self.VENTANA.place(x = 100, y =180, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))
        
        self.VENTANA = Button(new_window, text = "Poligono", command = self.poo4)
        self.VENTANA.place(x = 100, y =230, width = 280, height = 30)
        self.VENTANA.config(fg = 'white',bg='deep pink', font = ("Arial", 16))


    def barra4(self):
        cbarra()
        
    def pastel4(self):
        cpastel()
        
    def abs4(self):
        cFAcumulada()
        
    def poo4(self):
        cPoligonos() 
        
    
                               
                                                           
root = Tk()
root.resizable(False, False)
miVentana =FramePrincipal(root)
root.mainloop()
