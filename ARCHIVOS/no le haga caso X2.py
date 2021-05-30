from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as MessageBox
import tkinter as tk
from tkinter import ttk

from Persona import Persona


import string
alfabeto = list(string.ascii_lowercase.upper())
alfabeto2 = list(string.ascii_lowercase)
numeros=["0","1","2","3","4","5","6","7","8","9","0"]
alfabeto+=numeros#+alfabeto2
 
index=Tk()
index.title("LOGIN")
index.geometry("250x150")
index.resizable(width=False, height=False)
index.config( background="#ba55d3")

luser=Label(index, text="Ingrese nombre de usuario:", background="#ba55d3")
luser.pack()

var = tk.StringVar()
entry=ttk.Entry(index,textvariable=var)
entry.pack()


lpas=Label(index, text="Password:", background="#ba55d3")
lpas.pack()

pas=StringVar()
epas=Entry(index, width=30, textvariable=pas, show="*")
epas.pack()



inicia_sesion1=0
inicia_sesion2=0
posicion1=0
posicion2=1
lista_usuarios=[]
lista_contrasenas=[]


usuarios='user.txt'
with open(usuarios) as obj1:

    for line in obj1:
        texto=line.rstrip('\n')
        textocifrado=""
        for letra in texto:
            suma=alfabeto.index(letra)-2 
            mod=int(suma)%len(alfabeto)
            textocifrado=textocifrado+str(alfabeto[mod])
            if(len(textocifrado)==len(texto)):
                lista_usuarios.append(textocifrado)


contraseñas="contraseñas.txt"          
with open(contraseñas) as obj2:
    for line in obj2:
        line=line.rstrip('\n')
        lista_contrasenas.append(line)
        
print(lista_usuarios)
print(lista_contrasenas)




def datos():
    user2=var.get();
    user2=user2.upper()
    return user2

def datos2():
    pas2=pas.get()
    return pas2



def validarcontrasena1():    
    for usuario in lista_usuarios:
        if datos()==usuario:
            inicia_sesion1=1
            return inicia_sesion1

        
        
def validarcontrasena2():
    for contraseña in lista_contrasenas:
        if datos2()==contraseña:
            inicia_sesion2=1
            return inicia_sesion2 
        
        
def posicion1():
    posicion1=lista_usuarios.index(datos())
    return posicion1

def posicion2():
    posicion2=lista_contrasenas.index(datos2()) 
    return posicion2


def posiciones():
    if(posicion1()==posicion2()):
        return True
    else:
        return False
    
    
def ingresar():

    if validarcontrasena1()==1 and validarcontrasena2()==1 and posiciones()==True:
        MessageBox.showinfo("Holaa", "Bienvenido, amigue")
        import main

        
    else:
        MessageBox.showinfo("¿Quien eres?", "Te conozco?")
        
def registrar():
    import registrar
    
   
b1=Button(index, text="Entrar", command=ingresar)
b1.pack(side=BOTTOM)


b2=Button(index,text="Registrar", command=registrar)
b2.pack(side=BOTTOM)

index.mainloop()

